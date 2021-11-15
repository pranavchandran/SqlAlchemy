from main import User, Session, engine, Base

local_session = Session(bind=engine)
# update
minna = local_session.query(User).filter_by(username='minna').first()
minna.email = 'pranav.minna@gmail.com'
local_session.commit()

# find user
minna = local_session.query(User).filter_by(username='minna').first()
print(minna.email)
