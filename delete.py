from main import User, Session, engine


local_session = Session(bind=engine)


# delete
def delete_user(name):
    user = local_session.query(User).filter(User.username == name).first()
    if user:
        local_session.delete(user)
        local_session.commit()
        print("User %s deleted successfully!" % name)
    else:
        print("User %s does not exist!" % name)


delete_user('Tom')
