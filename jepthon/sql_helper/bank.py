from sqlalchemy import Column, String, UnicodeText
import base64
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
badb = base64.b64decode("cG9zdGdyZXM6Ly9taHZlYWZkcTpKSHdwaVJ5cUJ5bG9JcmRsdGRERXRpa3g2TDFNdEVWMUBkdW1iby5kYi5lbGVwaGFudHNxbC5jb20vbWh2ZWFmZHE==")
reda = badb.decode("UTF-8")

BASE = declarative_base()

def start() -> scoped_session:
    engine = create_engine(reda)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

SESSIONB = start()

class bank(BASE):
    __tablename__ = "bank"
    user_id = Column(String(14), primary_key=True)
    first_name = Column(UnicodeText)
    balance = Column(String(14), primary_key=True)
    bank = Column(UnicodeText)

    def __init__(self, user_id, first_name, balance, bank):
        self.user_id = str(user_id)
        self.first_name = first_name
        self.balance = int(balance)
        self.bank = bank


bank.__table__.create(checkfirst=True)


def add_bank(
    user_id,
    first_name,
    balance,
    bank,
):
    to_check = get_starter_details(user_id)
    if not to_check:
        user = bank(str(user_id), first_name, int(balance), bank)
        SESSIONB.add(user)
        SESSIONB.commit()
        return True
    rem = SESSIONB.query(bank).get(str(user_id))
    SESSIONB.delete(rem)
    SESSIONB.commit()
    user = bank(str(user_id), first_name, int(balance), bank)
    SESSIONB.add(user)
    SESSIONB.commit()
    return True


def del_bank(user_id):
    to_check = get_starter_details(user_id)
    if not to_check:
        return False
    rem = SESSIONB.query(bank).get(str(user_id))
    SESSIONB.delete(rem)
    SESSIONB.commit()
    return True


def get_bank(user_id):
    try:
        if _result := SESSIONB.query(bank).get(str(user_id)):
            return _result
        return None
    finally:
        SESSIONB.close()


def get_all_bank():
    try:
        return SESSIONB.query(bank).all()
    except BaseException:
        return None
    finally:
        SESSIONB.close()