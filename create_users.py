from main import User, Session

users = [
    {"username": "Jerry", "email": "jerry@gmail.com"},
    {"username": "Tom", "email": "tom@gmail.com"},
    {"username": "minna", "email": "minna@gmail.com"},
    {"username": "paru", "email": "paru@gmail.com"},
]

session = Session()
# new_user = User(username='Mary', email='mary@gmail.com')
# session.add(new_user)
# session.commit()

for user in users:
    new_user = User(username=user['username'], email=user['email'])
    session.add(new_user)

session.commit()
