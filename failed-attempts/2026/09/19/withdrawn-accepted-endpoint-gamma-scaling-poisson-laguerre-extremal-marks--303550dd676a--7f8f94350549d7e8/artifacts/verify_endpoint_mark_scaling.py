from mpmath import mp

mp.dps = 50

# Verification 1: leading endpoint-tilt coefficient from h_d(z)=(1+sqrt(1+z))^d.
print('leading Taylor coefficient c_{1,d} = d*2^(d-2)')
for d in range(3, 9):
    c1 = d * 2**(d-2)
    alpha1_reduced = mp.mpf(d)  # after dividing by (2^d)^{(d-2)/d}
    print(f'd={d}: c1={c1}, reduced coefficient={alpha1_reduced}')

# Verification 2: endpoint Karamata/Gamma scaling for an explicit bounded law.
# Y=A-M has F_Y(y)=(y/A)^kappa on [0,A], hence C=A^{-kappa}.
A = mp.mpf('1.7')
kappa = mp.mpf('2.5')
C = A**(-kappa)
const = C * mp.gamma(kappa + 1) / (2*A)**kappa

def I(alpha, extra=mp.mpf('0')):
    # e^{-alpha A^2} E exp(alpha M^2 - extra*alpha*(A-M))
    # integrate in y=A-M.
    f = lambda y: mp.e**(-(2*A+extra)*alpha*y + alpha*y*y) * (kappa/A**kappa) * y**(kappa-1)
    return mp.quad(f, [0, A])

print('\nendpoint Laplace asymptotics')
print('target alpha^kappa * exp(-alpha*A^2) E exp(alpha*M^2) =', mp.nstr(const, 18))
for alpha in [20, 80, 320]:
    alpha = mp.mpf(alpha)
    scaled = alpha**kappa * I(alpha)
    print(f'alpha={int(alpha):4d}: scaled={mp.nstr(scaled,18)}, error={mp.nstr(scaled-const,8)}')

print('\ntilted scaled-gap Laplace transforms')
for t in [mp.mpf('0.5'), mp.mpf('2.0')]:
    target = (2*A/(2*A+t))**kappa
    print('t=', t, 'target=', mp.nstr(target, 18))
    for alpha in [20, 80, 320]:
        alpha = mp.mpf(alpha)
        val = I(alpha, t)/I(alpha, 0)
        print(f'  alpha={int(alpha):4d}: value={mp.nstr(val,18)}, error={mp.nstr(val-target,8)}')

# Verification 3: d=3 printed-shift constant for Q(ds)=2s/A^2 ds.
# Exact source formula (1.7) contains +log(gamma).  The polished expansion without
# this term therefore retains a constant error -log(gamma).
gamma = mp.mpf('2.3')
v3 = 4*mp.pi/3
A2 = mp.mpf('1.9')
EM2 = A2**2/2  # density 2s/A^2

def shifts(rho):
    L = mp.log(rho**3)
    alpha = 3*(v3*gamma)**(mp.mpf(2)/3)*L**(mp.mpf(1)/3)
    log_mgf = alpha*A2**2 - mp.log(alpha*A2**2) + mp.log(1-mp.e**(-alpha*A2**2))
    exact = L - alpha*EM2 + log_mgf + mp.log(gamma)
    corrected = L + alpha*(A2**2-EM2) - mp.log(alpha*A2**2) + mp.log(gamma)
    printed = corrected - mp.log(gamma)
    return exact, corrected, printed

print('\nd=3 Q(ds)=2s/A^2 ds shift check')
print('log(gamma)=', mp.nstr(mp.log(gamma), 18))
for rho in [10, 100, 10000]:
    exact, corrected, printed = shifts(mp.mpf(rho))
    print(f'rho={rho:5d}: corrected-exact={mp.nstr(corrected-exact,10)}, printed-exact={mp.nstr(printed-exact,18)}')
