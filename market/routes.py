from market import app, db, login_user, render_template, logout_user, login_required, current_user
from market.models import Items, User
from market.forms import Register_form, Login_form, Purchase, Sell
from flask import redirect, url_for, flash, request


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/Market', methods=["GET", "POST"])
@login_required
def market_page():
    purchase_form = Purchase()
    sell_form = Sell()
    if request.method == "POST":
        # ------PURCHASE---------------
        if purchase_form.validate_on_submit():
            purchased_item = request.form.get("purchased_item")
            purchased_item_obj = Items.query.filter_by(name=purchased_item).first()
            if purchased_item_obj:
                if current_user.can_purchase(purchased_item_obj.price):
                    purchased_item_obj.buy(current_user)
                    flash(f"Item bought {purchased_item_obj.name} for Rs.{purchased_item_obj.price}", category="success")
                else:
                    flash(f"Not enough money.", category="danger")

            # ------SELL ----
            sold_item = request.form.get("sold_item")
            sold_item_object = Items.query.filter_by(name=sold_item).first()
            if sold_item_object:
                if current_user.can_sell(sold_item_object):
                    sold_item_object.sell(current_user)
                    flash(f"Item sold: {sold_item_object.name} for Rs.{sold_item_object.price}",
                          category="success")
                else:
                    flash(f"Something went wrong with selling {sold_item_object.name}")

            return redirect(url_for("market_page"))
    if request.method == "GET":
        items = Items.query.filter_by(owner=None)
        owned_items = Items.query.filter_by(owner=current_user.id)
        return render_template('market.html', items=items, purchase_form=purchase_form, owned_items=owned_items,
                               sell_form=sell_form)


@app.route('/Registration', methods=["GET", "POST"])
def register_page():
    form = Register_form()
    if form.validate_on_submit():
        new_user = User()
        new_user.username = form.username.data
        new_user.e_mail = form.email.data
        new_user.hash_password = form.password1.data
        db.session.add(new_user)
        db.session.commit()
        flash(f"Successfully registered as {new_user.username}", category="info")
        login_user(new_user)
        return redirect(url_for('market_page'))
    # if form.errors != {}:
    #     for error_msg in form.errors.values():
    #         flash(f"There is an error : {error_msg}")
    return render_template('register_form.html', form=form)


@app.route('/Login', methods=["GET", "POST"])
def login_page():
    form = Login_form()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f"Successfully logged in as {attempted_user.username}", category="success")
            return redirect(url_for('market_page'))
        flash(f"Invalid credentials. Try again", category="danger")
    return render_template("login.html", form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash(message='You have been logged out', category="info")
    return redirect(url_for('home_page'))