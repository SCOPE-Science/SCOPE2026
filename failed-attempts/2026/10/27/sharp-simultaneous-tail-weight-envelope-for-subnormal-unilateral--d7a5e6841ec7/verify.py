"""Independent finite exact-arithmetic spot checks of the stated moment envelope."""
from fractions import Fraction as F
from random import Random


def upper(u,v,k):
    x=u*(1-v)/(1-u)
    p=(u-x)/(1-x)
    return (p+(1-p)*x**(k+1))/(p+(1-p)*x**k)

def poly_product(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def poly_power_shift(x,ell):
    # Hermite interpolation polynomial Q_l(t)=t^l+(1-t)(t-x)^2 P_l(t,x)
    if ell==2: return [F(0),F(0),F(1)]
    P=[F(0)]*(ell-2)
    for r in range(ell-2):
        for j in range(r+1): P[r-j]+=F(j+1)*x**j
    c=poly_product([F(1),F(-1)],poly_product([x*x,-2*x,F(1)],P))
    c[ell]+=F(1)
    assert all(z==0 for z in c[3:]), (x,ell,c)
    assert sum(c[i]*x**i for i in range(3))==x**ell
    assert sum(i*c[i]*x**(i-1) for i in range(1,3))==ell*x**(ell-1)
    assert sum(c)==1
    return c[:3]

count=0
for x in [F(0),F(1,7),F(1,4),F(3,5),F(1)]:
    for ell in range(3,17):
        poly_power_shift(x,ell);count+=1
rng=Random(23041)
for trial in range(400):
    atoms=[F(rng.randrange(1,999),1000) for _ in range(rng.randrange(2,9))]
    probs=[F(rng.randrange(1,31),1) for _ in atoms]
    s=sum(probs);probs=[z/s for z in probs]
    mu=lambda k: sum(p*t**k for p,t in zip(probs,atoms))
    u=mu(1);v=mu(2)/u
    assert 0<u<=v<1
    for k in range(2,13):
        assert mu(k+1)<=upper(u,v,k)*mu(k), (trial,k)
        count+=1
    x=u*(1-v)/(1-u);p=(u-x)/(1-x)
    for k in range(2,13):
        a=p+(1-p)*x**k
        b=p+(1-p)*x**(k+1)
        assert b/a==upper(u,v,k)
        count+=1
print('PASS',count,'exact polynomial and moment checks')
