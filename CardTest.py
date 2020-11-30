from Tests.CreditClass import Creditcard
# import datetime
from datetime import datetime

today = str(datetime.today())
today = today.split('-')

card = Creditcard()
number = card.number
pin = card.pin
date = card.date


def test_card_number():
    if type(number) == int:
        if len(str(number)) == 16:
            assert card.isvalid_number() == True
    else:
        assert card.isvalid_number() == False


def test_card_pin():
    if type(pin) == int:
        if len(str(pin)) == 3:
            assert card.isvalid_Pin() == True
    else:
        assert card.isvalid_Pin() == False


def test_card_date():
    mm, yy = date.split('/')
    if mm > today[1]:
        if yy > today[0]:
            assert card.isvalid_Date() == True


def isValid_Card():
    if test_card_number() and test_card_pin() and test_card_date():
        card.valid== True
        assert card.isValid() == True
    else:
        assert card.isValid() == False

