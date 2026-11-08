"""Independent reproducibility helper for algebraic identities and finite orbits.
Only the proof gives the asymptotic theorem; these computations are supplementary.
"""
import math
import sympy as sp

x,m,c,z=sp.symbols('x m c z', positive=True)
rho=(m-c)/(2*m)
r_b=4*m/(m+c)**2
F=r_b*x*(1-x)*(c+m*x)
assert sp.factor(F-x*(1-((x-rho)/(1-rho))**2)) == 0
assert sp.factor((F-x)/x+(x-rho)**2/(1-rho)**2)==0
assert sp.factor((F-rho)/(x-rho)-(1-x*(x-rho)/(1-rho)**2)) == 0


def orbit(r,eta,eps,zeta=None, x0=None):
    s=(r+math.sqrt(r*r+4*(1-r)**2))/2
    x0 = s+zeta*math.sqrt(eps) if zeta is not None else x0
    y=x0
    n=0
    while y>r-eta and n<5_000_000:
        y=y*(1-eps-(1-eps)*((y-r)/(1-r))**2)
        n+=1
    assert n < 5_000_000
    return n*math.sqrt(eps), s

for r in [.125,.25,.4]:
    s=(r+math.sqrt(r*r+4*(1-r)**2))/2
    assert r<s<1, (r,s)
    assert abs(s*(s-r)-(1-r)**2)<2e-15
    eta = r/5
    vals=[]
    for zeta in (-1,0,1):
        computed=[]
        for eps in (1e-5,1e-6,1e-7):
            val,_=orbit(r,eta,eps,zeta)
            computed.append(val)
        predicted=(1-r)/r*(math.pi/2-math.atan((2-r/s)*zeta/(1-r)))
        assert abs(computed[-1]-predicted)<.15, (r,zeta,computed,predicted)
        vals.append((zeta,computed,predicted))
    mid=(r+s)/2
    full=[orbit(r,eta,eps,x0=mid)[0] for eps in (1e-5,1e-6,1e-7)]
    expected=math.pi*(1-r)/r
    assert abs(full[-1]-expected)<.15, (r,full,expected)
    high=[orbit(r,eta,eps,x0=(1+s)/2)[0] for eps in (1e-5,1e-6,1e-7)]
    assert high[-1]<.15, (r,high)
    print(f'rho={r}, s={s:.12f}, crossover={vals}, full={full}, target={expected:.12f}, above_cutoff={high}')
print('VERIFY_OK exact_normal_form=1 exact_order_identity=1 exact_threshold_factor=1 crossover_profiles=9 full_passages=3 overpopulation=3')
