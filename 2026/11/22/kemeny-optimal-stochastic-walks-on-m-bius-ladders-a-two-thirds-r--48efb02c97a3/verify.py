"""Exact and numerical checks for Kemeny optimization on Möbius ladders.
No external dependencies; exact checks use fractions.Fraction.
"""
from fractions import Fraction as Q
from math import cos, pi, sqrt, exp, log

checks = 0

def check(cond, message):
    global checks
    assert cond, message
    checks += 1

def inverse_rational(a):
    n = len(a)
    rows = [[Q(v) for v in row] + [Q(i == j) for j in range(n)]
            for i, row in enumerate(a)]
    for j in range(n):
        piv = next((k for k in range(j, n) if rows[k][j]), None)
        assert piv is not None
        rows[j], rows[piv] = rows[piv], rows[j]
        factor = rows[j][j]
        rows[j] = [v/factor for v in rows[j]]
        for i in range(n):
            if i != j and rows[i][j]:
                factor = rows[i][j]
                rows[i] = [u-factor*v for u, v in zip(rows[i], rows[j])]
    return [r[n:] for r in rows]

def exact_kemeny(m, b):
    n = 2*m
    a = (1-b)/2
    M = [[Q(1,n) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if (i-j)%n in (1,n-1):
                w=a
            elif (i-j)%n==m:
                w=b
            else:
                continue
            M[i][i]+=w
            M[j][j]+=w
            M[i][j]-=w
            M[j][i]-=w
    Inv=inverse_rational(M)
    return sum(Inv[i][i] for i in range(n))-1

def exact_closed(m, sqrtnum, sqrtden):
    s=Q(sqrtnum,sqrtden)
    b=s*s
    r=(1-s)/(1+s)
    even=Q(m*m-1,6)/(1-b)
    odd=Q(m,2)/s * (1-r**m)/(1+r**m)
    return even+odd

def spectral(m,b):
    return sum(1/(2*a*(1-cos(pi*k/m))+b*(1-(-1)**k))
               for k in range(1,2*m) for a in [(1-b)/2])

def closed(m,b):
    s=sqrt(b)
    q=(1-s)/(1+s)
    Qm=exp(m*log(q))
    return (m*m-1)/(6*(1-b))+m/(2*s)*(1-Qm)/(1+Qm)

def derivative(m,b):
    s=sqrt(b)
    q=(1-s)/(1+s)
    Qm=exp(m*log(q))
    t=(1-Qm)/(1+Qm)
    return (m*m-1)/(6*(1-b)**2) - m*t/(4*b**1.5) + m*m*Qm/(b*(1-b)*(1+Qm)**2)

def optimizer(m):
    lo=1e-12
    hi=1-1e-12
    for _ in range(90):
        mid=(lo+hi)/2
        if derivative(m,mid)>0: hi=mid
        else: lo=mid
    return (hi+lo)/2

def run():
    for m in range(2,9):
        for u,v in [(1,2),(1,3),(2,3)]:
            b=Q(u*u,v*v)
            k=exact_kemeny(m,b)
            f=exact_closed(m,u,v)
            check(k==f, f'exact trace identity m={m}, b={b}: {k} != {f}')
    # Independent published unit-weight Kirchhoff-index table for m=3,...,8.
    # For a 3-regular graph Kemeny(P)=3 KirchhoffIndex/(2m).
    published_kf={3:Q(9),4:Q(134,7),5:Q(1135,33),
                  6:Q(725,13),7:Q(10367,123),8:Q(11732,97)}
    for m,kf in published_kf.items():
        check(exact_kemeny(m,Q(1,3)) == Q(3,2*m)*kf,
              f'published unweighted Kirchhoff table m={m}')
    for m in range(2,32):
        for b in [.02,.13,.25,1/3,.61,.87]:
            check(abs(spectral(m,b)-closed(m,b))<2e-9*(1+closed(m,b)), f'Fourier sum m={m}, b={b}')
    for m in range(2,28):
        for b in [.04,.18,.35,.6]:
            step=1e-6
            d=(closed(m,b+step)-closed(m,b-step))/(2*step)
            check(abs(d-derivative(m,b)) < 2e-5 * (1+abs(d)),f'derivative m={m}, b={b}')
    for m in range(2,20):
        b=optimizer(m)
        check(0<b<1,f'bound m={m}')
        check(abs(derivative(m,b))<1e-6*(1+m*m),f'stationarity m={m}')
        check(closed(m,b)<closed(m,max(b-1e-3,1e-10))+1e-9, f'left minimum m={m}')
        check(closed(m,b)<closed(m,min(b+1e-3,.999999))+1e-9, f'right minimum m={m}')
        if m>=4: check(b<1/3,f'interior law m={m}')
    for m in (2,3):
        check(abs(optimizer(m)-1/3)<1e-9,f'edge-transitive m={m}')
    c=(3/2)**(2/3)
    for m in (300,600,1200,2400):
        b=optimizer(m)
        check(abs(m**(2/3)*b/c-1) < .05,f'asymptotic rung law m={m}')
        minimum=closed(m,b)
        check(abs(minimum/(m*m/6)-1) < .11, f'asymptotic minimum m={m}')
        check(abs(closed(m,1/3)/minimum-1.5)<.2,f'uniform penalty m={m}')
        check(abs((minimum-m*m/6)/(.5*c*m**(4/3))-1)<.18, f'next order m={m}')
    print('PASS',checks,'exact rational and numerical checks')
    for m in [2,3,4,5,8,16,100,1000]:
        b=optimizer(m)
        print('m=',m,'b*=',format(b,'.12g'),'K*=',format(closed(m,b),'.12g'))

if __name__=='__main__':
    run()
