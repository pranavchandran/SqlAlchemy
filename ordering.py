from main import User, Session, engine


local_session = Session(bind=engine)

# ascending order
# for user in local_session.query(User).order_by(User.username):
#     print(user)

# descending order
for user in local_session.query(User).order_by(User.username.desc()):
    print(user)
