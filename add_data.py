# from market.models import Items, User
# from market import app
# from market import db
#
# with app.app_context():
#     pass
#     # item1 = Items(name='Phone', barcode='145235478956', price='100', description='A phone')
#     # item2 = Items(name='Laptop', barcode='547841235649', price='500', description='A laptop')
#     # db.session.add(item1)
#     # db.session.add(item2)
#     # db.session.commit()
#
#
#     # CREATE ______
#     # user = User()
#     # db.session.add(user)
#     # db.commit()
#     #
#     # # READ______
#     # # --------all_items
#     # result = db.session.execute(db.select(User).order_by(User.username)).scalars()
#     #     # -------particular item
#     # result = db.session.execute(db.select(User).where(User.username == "ashish")).scalar()
#
#         # UPDATE----------
#     # name = db.session.execute(db.select(User).where(User.username == "new")).scalar()
#     # name.username = "old"
#     # db.session.commit()
#
#         # DELETE -------
#     # object = db.session.execute(db.select(User).where(User.username == "new")).scalar()
#     # db.session.delete(object)
#     # db.session.commit()
#,
#
#
#         # db.session.add(item1)
#     # db.drop_all()
#     # db.create_all()
#     # db.session.commit()
#     # u1 = User(username="Ashitosh", e_mail="a@gmail.com", password="ashitosh")
#     # db.session.add(u1)
#     # # db.session.commit()
#     # item1 = Items(name='Phone', barcode='145235478956', price='100', description='A phone')
#     # item2 = Items(name='Laptop', barcode='547841235649', price='500', description='A laptop')
#     # # db.session.add(item1,item2)
#     # # db.session.add(item2)
#     # # db.session.commit()
#     # phone = Items.query.filter_by(name="Phone").first()
#     # # print(phone)
#     # # print(phone.owner)
#     # # phone.owner = User.query.filter_by(username="Ashitosh").first().id
#     # # db.session.commit()
#     # # print(phone.owner)
#     # user = User.query.filter_by(username="Ashitosh").first()
#     # print(user.items_owned)

