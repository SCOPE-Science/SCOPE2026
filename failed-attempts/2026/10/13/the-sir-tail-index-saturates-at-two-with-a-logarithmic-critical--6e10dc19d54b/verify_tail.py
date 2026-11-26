import mpmath as mp

mp.mp.dps = 60

def survival(z, theta, q):
    a = theta/(z*z)
    s = q/2
    return s*(a**s)*mp.quad(lambda t: (1-mp.e**(-t))*t**(-s-1), [a, 1, mp.inf])

def density(z, theta, q):
    a = theta/(z*z)
    # Source formula: theta*q/z^3 * E_{q/2}(a), E_s(a)=int_1^inf exp(-a*u)u^-s du
    Es = mp.quad(lambda u: mp.e**(-a*u)*u**(-q/2), [1, mp.inf])
    return theta*q/(z**3)*Es

def surv_asym(z, theta, q):
    if q < 2:
        return mp.gamma(1-q/2)*(theta**(q/2))*(z**(-q))
    if q == 2:
        return theta*z**(-2)*mp.log(z*z/theta)
    return q*theta/(q-2)*z**(-2)

def dens_asym(z, theta, q):
    if q < 2:
        return q*mp.gamma(1-q/2)*(theta**(q/2))*z**(-q-1)
    if q == 2:
        return 2*theta*z**(-3)*mp.log(z*z/theta)
    return 2*q*theta/(q-2)*z**(-3)

theta = mp.mpf("1.7")
for q,z,tol in [
    (mp.mpf("1.0"), mp.mpf("1e5"), mp.mpf("0.01")),
    (mp.mpf("2.0"), mp.mpf("1e8"), mp.mpf("0.08")),
    (mp.mpf("3.0"), mp.mpf("1e5"), mp.mpf("0.02")),
]:
    s = survival(z,theta,q)
    f = density(z,theta,q)
    assert abs(s/surv_asym(z,theta,q)-1) < tol
    assert abs(f/dens_asym(z,theta,q)-1) < tol
    h = f/s
    assert abs((z*h)/min(q,mp.mpf(2))-1) < 2*tol

# Fractional moment formula checked by direct product-factor integration.
for q,r in [(mp.mpf("1.5"),mp.mpf("0.7")),(mp.mpf("3"),mp.mpf("1.5"))]:
    exact = theta**(r/2)*mp.gamma(1-r/2)*q/(q-r)
    ir = mp.quad(lambda x: x**r * 2*theta*x**(-3)*mp.e**(-theta/x**2), [0,1,mp.inf])
    betainv = mp.quad(lambda y: q*y**(q-r-1), [0,1])
    assert abs(ir*betainv/exact-1) < mp.mpf("1e-30")

print("VERIFY_OK")
