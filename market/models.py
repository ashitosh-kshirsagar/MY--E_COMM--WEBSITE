from market import db, bcrypt, login_manager, UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=20), nullable=False, unique=True)
    e_mail = db.Column(db.String(length=30), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False, unique=False)
    budget = db.Column(db.Integer(), default=1000)
    items_owned = db.relationship("Items", backref="owner_of_item", lazy=True)

    @property
    def hash_password(self):
        return self.hash_password

    @hash_password.setter
    def hash_password(self, plain_password):
        self.password = bcrypt.generate_password_hash(plain_password).decode("utf-8")

    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password, attempted_password)

    def can_purchase(self, item_price):
        return self.budget >= item_price

    def can_sell(self, item_object):
        return item_object in self.items_owned


class Items(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False, unique=False)
    description = db.Column(db.String(length=1000), nullable=False, unique=False)
    owner = db.Column(db.Integer(), db.ForeignKey("user.id"))

    def __repr__(self):
        return f"Item {self.name}"

    def buy(self, user):
        self.owner = user.id
        user.budget -= self.price
        db.session.commit()

    def sell(self, user):
        self.owner = None
        user.budget += self.price
        db.session.commit()
