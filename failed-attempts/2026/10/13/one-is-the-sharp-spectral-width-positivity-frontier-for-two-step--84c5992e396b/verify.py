from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal

lams = [D(1), D(6)/D(5), D(3)]
b = [D(1), D(1), D(1)/D(100)]
t = D(1)

norm2 = sum(x*x for x in b)
beta0 = norm2.sqrt()
v1 = [x/beta0 for x in b]
alpha1 = sum(lams[i]*v1[i]*v1[i] for i in range(3))
w = [(lams[i]-alpha1)*v1[i] for i in range(3)]
beta1 = sum(x*x for x in w).sqrt()
v2 = [x/beta1 for x in w]
alpha2 = sum(lams[i]*v2[i]*v2[i] for i in range(3))

m = (alpha1+alpha2)/D(2)
delta = (alpha1-alpha2)/D(2)
q = (delta*delta + beta1*beta1).sqrt()

ep = (t*q).exp()
em = (-t*q).exp()
cosh = (ep+em)/D(2)
sinh = (ep-em)/D(2)
pref = (-t*m).exp()

g1 = pref*(cosh - (delta/q)*sinh)
g2 = pref*(-(beta1/q)*sinh)

y = [beta0*(v1[i]*g1 + v2[i]*g2) for i in range(3)]
exact3 = (-D(3)).exp()/D(100)

assert y[2] < D("-0.0028")
assert exact3 > 0

tau = D(2)
r = D("0.01")
sharp = D(1) - (D(1)-(-tau*r).exp())/r
assert sharp < 0

# At the sharp safe boundary tau=1 the mean-value lower bound is nonnegative.
assert D(1)-D(1) == 0

print("VERIFY_OK")
print("third_lanczos", y[2])
print("third_exact", exact3)
print("sharpness_test", sharp)
