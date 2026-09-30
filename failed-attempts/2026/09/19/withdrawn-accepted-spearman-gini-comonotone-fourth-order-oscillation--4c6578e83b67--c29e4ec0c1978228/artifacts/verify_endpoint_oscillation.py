from decimal import Decimal, getcontext
getcontext().prec = 80
D = Decimal
sqrt3 = D(3).sqrt()
A3 = (D(5) + D(3)*sqrt3)/D(2)
C0 = (D(78) + D(45)*sqrt3)/D(4)

def boundary(theta):
    N = int(theta)
    n = D(N)
    s = D(1)/theta
    L = D(1)/(D(2)*n)
    R = D(1)/(D(2)*(n+D(1)))
    ell = L if s >= L+R else R
    delta = s-D(2)*ell
    p = D(1)-D(2)*n*(n+D(1))*abs(delta)
    m = ell+n*(n+D(1))*delta*abs(delta)
    q = ell*(D(2)*m-ell) + D(2)/D(3)*n*(n+D(1))*abs(delta)**3
    c = (ell**2-s*ell-ell*p*delta)/D(2)
    alpha = (D(1)+(D(1)+D(2)*theta**2*c).sqrt())/D(2)
    t = D(1)/(theta+alpha)
    a = alpha*t
    z = theta*t
    G = D(1)-D(2)*a*a-z*z*m
    P = D(1)-D(2)*a**3-D(3)/D(2)*z**3*q
    return G,P

def psi(frac):
    d=min(frac,D(1)-frac)
    return C0+D(16)*d**3-D(24)*d**4

print('A3 =', A3)
print('C0 =', C0)
print('C0+1/2 =', C0+D('0.5'))
for frac_s in ['0','0.1','0.3','0.5','0.7','0.9']:
    f=D(frac_s)
    target=psi(f)
    print('\nphase', frac_s, 'target', target)
    for N in [100, 1000, 10000]:
        th=D(N)+f
        G,P=boundary(th)
        x=D(1)-G
        y=D(1)-P
        empirical=(y-D(3)/D(2)*x*x+A3*x**3)/(x**4)
        print(N, 'x=', x, 'c4=', empirical, 'err=', empirical-target)
