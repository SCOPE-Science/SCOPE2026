"""Standalone numerical and symbolic diagnostics; asymptotic proof is in RESULT.md."""
import math

def run(x0,y0,nmax=200000):
    x,y=x0,y0
    u=x+y
    assert math.sin(u)!=0
    s=1 if math.sin(u)>0 else -1
    records=[]
    for n in range(1,nmax+1):
        xp=x+math.sin(x+y)
        yp=-x
        x,y=xp,yp
        u=x+y
        if n in (50000,100000,200000):
            records.append((n,n*u*u,x/math.sqrt(n),1/(u*u)-n/3-math.log(n)/5))
    assert (x>0)==(s>0)
    return records

for a,b in ((0.2,0.7),(-0.8,-0.5),(2.1,0.1)):
    rows=run(a,b)
    for n,nu2,scale,c in rows:
        assert abs(nu2-3)<0.02, (n,nu2)
        assert abs(scale-2*math.sqrt(3)*(1 if math.sin(a+b)>0 else -1))<0.04, (n,scale)
    assert abs(rows[-1][-1]-rows[-2][-1])<0.005,(a,b,rows)
    print('initial',a,b,rows)

# The defining transformation is exact; periodic exceptions are checked symbolically.
try:
    import sympy as s
    X,Y=s.symbols('X Y',real=True)
    U=X+Y
    xp=X+s.sin(U); yp=-X
    assert s.simplify(xp+yp-s.sin(U))==0
    assert s.simplify(xp-X-s.sin(U))==0
    for m in range(-3,4):
        assert s.simplify(s.sin(m*s.pi))==0
except ImportError:
    print('SymPy not installed; skipped optional symbolic identities.')
print('Diagnostics passed (finite tests are not the proof).')
