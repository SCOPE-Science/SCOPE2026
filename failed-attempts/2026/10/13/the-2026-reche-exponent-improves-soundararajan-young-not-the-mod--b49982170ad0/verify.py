from decimal import Decimal, getcontext
getcontext().prec = 60

assert 1905 > 43*43
assert 9*1905 < 131*131

eta = (Decimal(1905).sqrt() - Decimal(27)) / Decimal(24)
lo = Decimal(2)/Decimal(3)
hi = Decimal(25)/Decimal(36)
assert lo < eta < hi
print("VERIFY_OK eta_1_6={} lower_gap={} upper_gap={}".format(eta, eta-lo, hi-eta))
