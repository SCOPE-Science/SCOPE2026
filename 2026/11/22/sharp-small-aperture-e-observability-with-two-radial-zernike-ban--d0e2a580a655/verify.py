"""Recompute analytic identities and finite concentration matrices.
Requires Python 3, SymPy and mpmath. This program checks finite cases;
the general asymptotic assertion is proved in the accompanying result.
"""
import random
import sympy as s
import mpmath as mp

x,a,b,m,h,L1,L2,q=s.symbols('x a b m h L1 L2 q',real=True)
checks=0
p=(x-a)*(x-b)
D=s.integrate(p*p,(x,0,1))
assert s.simplify(D-(a*a*b*b-a*a*b+a*a/s.Integer(3)-a*b*b+4*a*b/s.Integer(3)-a/s.Integer(2)+b*b/s.Integer(3)-b/s.Integer(2)+s.Rational(1,5)))==0
checks+=1
E=s.integrate(p*p,(x,a-L1/2,a+L1/2))+s.integrate(p*p,(x,b-L2/2,b+L2/2))
assert s.simplify(E-(a-b)**2*(L1**3+L2**3)/12-(L1**5+L2**5)/80)==0
checks+=1
assert s.simplify(D.subs({a:m-h,b:m+h})-(s.Rational(1,80)+(m-s.Rational(1,2))**2/2-h*h/6+((m-s.Rational(1,2))**2-h*h)**2))==0
checks+=1
z=s.symbols('z',positive=True)
f=z**2-z/s.Integer(6)+s.Rational(1,80)
zstar=1/(4*s.sqrt(5))
assert s.simplify((f-z*s.diff(f,z))-(s.Rational(1,80)-z*z))==0
assert s.simplify(4*zstar/f.subs(z,zstar)-(30+18*s.sqrt(5)))==0
checks+=2
monic=x*x-x+s.Rational(1,6)
assert s.integrate(monic**2,(x,0,1))==s.Rational(1,180)
checks+=1

mp.mp.dps=65
rad=mp.power(5,mp.mpf('-0.25'))
xx=(1-rad)/2; yy=(1+rad)/2
C=(5+3*mp.sqrt(5))/2
polys=[[mp.mpf(1)],[ -mp.sqrt(3), 2*mp.sqrt(3) ],[mp.sqrt(5),-6*mp.sqrt(5),6*mp.sqrt(5)]]
def gram(intervals):
    G=mp.matrix(3,3)
    for i in range(3):
        for j in range(3):
            v=mp.mpf(0)
            for u,ui in enumerate(polys[i]):
                for w,wj in enumerate(polys[j]):
                    k=u+w+1
                    v+=ui*wj*sum((B**k-A**k)/k for A,B in intervals)
            G[i,j]=v
    return G
ident=gram([(mp.mpf(0),mp.mpf(1))]); assert mp.norm(ident-mp.eye(3))<mp.mpf('1e-60'); checks+=1
ratios=[]
for qstr in ['0.1','0.05','0.02','0.01','0.005','0.001','0.0001']:
    q0=mp.mpf(qstr); small=q0*q0; big=q0-small
    E=[(xx-small/2,xx+small/2),(yy-big/2,yy+big/2)]
    lam=min(mp.eigsy(gram(E),eigvals_only=True))
    ratios.append(float(lam/(C*q0**3)))
assert all(r<1.000001 for r in ratios) and ratios[-1]>.999
checks+=len(ratios)

random.seed(2701)
for it in range(200):
    q0=random.uniform(.0005,.20)
    l1=random.uniform(.03,.97)*q0; l2=q0-l1
    c1=random.uniform(l1/2,1-l1/2)
    c2=random.uniform(l2/2,1-l2/2)
    E=sorted([(c1-l1/2,c1+l1/2),(c2-l2/2,c2+l2/2)])
    if E[0][1]>=E[1][0]: continue
    Em=[(mp.mpf(str(A)),mp.mpf(str(B))) for A,B in E]
    lm=min(mp.eigsy(gram(Em),eigvals_only=True))
    assert lm <= C*mp.mpf(str(q0))**3+mp.mpf('2.25')*mp.mpf(str(q0))**5+mp.mpf('1e-45')
    checks+=1
print('TWO_BAND_RADIAL_CHECKS_PASS',checks)
print('ratios:',','.join(f'{r:.8f}' for r in ratios))
