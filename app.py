from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Hotel, Booking
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'indistay_premium_2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

# Login Required Decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login first to book your stay!', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Database Initializer with 6-7 Hotels per Destination
with app.app_context():
    db.create_all()
    
    # Check if we need to seed data
    if not Hotel.query.first():
        destinations = {
            "Goa": ["Taj Exotica", "Goa Marriott", "W Goa", "Alila Diwa", "Caravela Beach", "Novotel Resorts", "Hard Rock Hotel"],
            "Jaipur": ["Rambagh Palace", "ITC Rajputana", "Fairmont Jaipur", "Chokhi Dhani", "Jai Mahal Palace", "Trident Jaipur", "Umaid Bhawan"],
            "Mumbai": ["The Taj Mahal Palace", "JW Marriott Sahar", "Trident Nariman Point", "The Oberoi", "Sahara Star", "Hotel Sahara", "Marine Plaza"],
            "Kerala": ["Kumarakom Lake Resort", "The Zuri", "Spice Village", "Elephant Court", "Vasundhara Sarovar", "Brunton Boatyard", "Fragrant Nature"],
            "Delhi": ["The Leela Palace", "ITC Maurya", "The Lodhi", "Shangri-La", "Taj Palace Delhi", "Radisson Blu", "The Claridges"]
        }

        hotels_to_add = []
        for city, names in destinations.items():
            for i, name in enumerate(names):
                hotels_to_add.append(Hotel(
                    name=name,
                    city=city,
                    price=3500 + (i * 1500), # Varied pricing
                    description=f"Experience the finest hospitality in {city}. This property offers premium rooms, authentic local cuisine, and world-class amenities."
                ))
        
        db.session.bulk_save_objects(hotels_to_add)
        db.session.commit()
        print("Successfully added 35 hotels to the database!")

# --- ROUTES ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered!', 'danger')
        else:
            hashed_pw = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(name=name, email=email, password=hashed_pw)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created! Please login.', 'success')
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['user_name'] = user.name
            flash(f'Welcome back, {user.name}!', 'success')
            return redirect(url_for('index'))
        flash('Invalid email or password', 'danger')
    return render_template('login.html')

@app.route('/hotels')
def hotels():
    city_query = request.args.get('city')
    if city_query:
        # Filter by city (Case-insensitive)
        hotel_list = Hotel.query.filter(Hotel.city.ilike(f'%{city_query}%')).all()
    else:
        hotel_list = Hotel.query.all()
    return render_template('hotels.html', hotels=hotel_list)

@app.route('/hotel/<int:id>')
def hotel_detail(id):
    hotel = Hotel.query.get_or_404(id)
    return render_template('hotel_detail.html', hotel=hotel)

@app.route('/book/<int:hotel_id>', methods=['POST'])
@login_required
def book(hotel_id):
    new_booking = Booking(
        user_id=session['user_id'],
        hotel_id=hotel_id,
        checkin=request.form.get('checkin'),
        checkout=request.form.get('checkout')
    )
    db.session.add(new_booking)
    db.session.commit()
    flash('BOOKING_CONFIRMED', 'success')
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    bookings = Booking.query.filter_by(user_id=user.id).all()
    return render_template('dashboard.html', user=user, bookings=bookings)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)