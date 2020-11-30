from Tests.PaymentClass import Payment

method = Payment()


def test_payment_method():
    if method.payment == "credit" or "debit":
        assert method.isCardPayment() == True
    elif method.payment == "cash":
        assert method.isCashPayment() == True
