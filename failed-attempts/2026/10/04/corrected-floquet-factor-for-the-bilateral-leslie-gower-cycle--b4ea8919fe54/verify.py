from fractions import Fraction as F

p1 = F(9, 20)
p2 = F(2, 5)
h1 = F(30)
h2 = F(65)
tau1 = F(2)
tau2 = F(5)
yA = F(47)
yB = F(60)

xA = (1 + p1) * h1
xB = h2
xC = (1 - p2) * h2
xD = h1
yC = yB + tau2
yD = yA + tau1

x_endpoint = (xB / xA) * (xD / xC)
y_endpoint = (yB / yA) * (yD / yC)
assert x_endpoint == 1 / ((1 + p1) * (1 - p2))
assert y_endpoint == yB * (yA + tau1) / (yA * (yB + tau2))

true_factor = x_endpoint * y_endpoint
printed_factor = ((1 - p2) / (1 + p1)) * ((yA + tau1) * (yB + tau2) / (yA * yB))
ratio = (1 - p2) ** 2 * ((yB + tau2) / yB) ** 2
assert printed_factor / true_factor == ratio
assert (printed_factor == true_factor) == ((1 - p2) * (yB + tau2) == yB)
print("VERIFY_OK")
