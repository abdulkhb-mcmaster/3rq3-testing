from Tests.AddressClass import Address
from string import printable

address = Address()
street = address.streetnumber
streetname = address.streetname
city = address.city
provrince = address.provrince
postalcode = address.postalcode


def test_Street_number():
    if type(street) == int:
        assert address.isvalidStreet() == True


def test_street_name():
    if set(streetname).difference(printable):
        assert address.isvalidstreetname() == False
    else:
        assert address.isvalidstreetname() == True


def test_City():
    if type(city) == str:
        if set(city).difference(printable):
            assert address.isvalidcity() == False
        else:
            assert address.isvalidcity() == True
    else:
        assert address.isvalidcity() == False


def test_provrince():
    if type(provrince) == str:
        if set(provrince).difference(printable):
            assert address.isvalidprovrince() == False
        else:
            assert address.isvalidprovrince() == True
    else:
        assert address.isvalidprovrince() == False


def test_postal_Code():
    if len(str(postalcode)) == 6:
        if set(postalcode).difference(printable):
            assert address.isvalidpostalcode() == False
        else:
            assert address.isvalidpostalcode() == True
    else:
        assert address.isvalidpostalcode() == False
