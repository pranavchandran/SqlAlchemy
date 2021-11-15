from main import User, Session, engine, Base


local_session = Session(bind=engine)

# return all users
users = local_session.query(User).all()

# for user in users:
#     print(user.username)


# query for one user
def get_user(username):
    return local_session.query(User).filter_by(username=username).first()


minna = get_user('minna')
print(minna.email)
