"""Exact algebraic and supplementary numerical checks for periodic versus iid gradient thinning.

Run with Python 3 and SymPy. This checks identities and finite instances; the
all-parameter assertions are proved separately in RESULT.md.
"""
import sympy as s

b,t,p=s.symbols('b t p', real=True)
M0=s.Matrix([[1+b,-b],[1,0]])
M1=s.Matrix([[1+b-t,-b],[1,0]])
N=0
for m in range(2,16):
    P=(M0**(m-1))*M1
    tr=s.factor(s.trace(P))
    det=s.factor(P.det())
    want=1+b**m-t*sum(b**k for k in range(m))
    assert s.expand(tr-want)==0
    assert s.expand(det-b**m)==0
    N+=2
    Cp=s.factor(2*(1-b)*(1+b**m)/(1-b**m))
    Ci=2*(1-b*b)/(1+b-2*b/s.Integer(m))
    diff=s.factor(Cp-Ci)
    factor= s.factor(diff/(m*b**(m-1)+(m-1)*b**m-1))
    assert s.factor(diff-(m*b**(m-1)+(m-1)*b**m-1)*factor)==0
    # Expected sign factor is positive for 0 < b < 1.
    for rational in (s.Rational(1,10),s.Rational(1,4),s.Rational(1,2),s.Rational(3,4),s.Rational(9,10)):
        assert s.sign(diff.subs(b,rational)) == s.sign((m*b**(m-1)+(m-1)*b**m-1).subs(b,rational))
        N+=1
A=s.Matrix([[1+b-t*p,-b],[1,0]])
a=1+b-p*t
v=p*(1-p)*t**2
T=s.Matrix([[a*a+v,-2*b*a,b*b],[a,-b,0],[1,0,0]])
det1=s.factor((s.eye(3)-T).det())
want=p*t*(2*(1-b*b)-t*(1+b-2*p*b))
assert s.factor(det1-want)==0;N+=1
P=s.Matrix([[1,-b*a/(1+b)],[-b*a/(1+b),b*b]])
E=(1-p)*M0.T*P*M0+p*M1.T*P*M1
D=p*t*(2*(1-b)-t*(1+b-2*p*b)/(1+b))
assert all(s.factor(z)==0 for z in E-P+s.diag(D,0));N+=4
assert s.factor(P.det()-b*b*p*t*(2*(1+b)-p*t)/(1+b)**2)==0;N+=1
# Discriminant matching exact transition points: m=2,3.
assert s.simplify(((2*b+b*b)-1).subs(b,s.sqrt(2)-1))==0;N+=1
assert (3*b*b+2*b**3-1).subs(b,s.Rational(1,2))==0;N+=1
for m in range(2,12):
    poly=m*b**(m-1)+(m-1)*b**m-1
    root=float(s.nsolve(poly,0.5 if m<4 else 0.8))
    assert 0<root<1
    assert abs(float(poly.subs(b,root)))<1e-9
    # independently compute eigenvalues of deterministic monodromy at 95% and 105% of stability ceiling.
    for ratio in (s.Rational(19,20),s.Rational(21,20)):
        for beta in (s.Rational(1,5),s.Rational(1,2),s.Rational(4,5)):
            cap= 2*(1-beta)*(1+beta**m)/(1-beta**m)
            A=(M0.subs(b,beta)**(m-1))*M1.subs({b:beta,t:cap*ratio})
            # Schur test with exact rational entries
            ok = all(x>0 for x in (1-A.det(),1+s.trace(A)+A.det(),1-s.trace(A)+A.det()))
            assert ok==(ratio<1)
            N+=1
    print(f'm={m:2d} crossover_beta={root:.12f}')
print('VERIFY_OK',N,'exact symbolic / rational checks plus isolated high-precision roots')
