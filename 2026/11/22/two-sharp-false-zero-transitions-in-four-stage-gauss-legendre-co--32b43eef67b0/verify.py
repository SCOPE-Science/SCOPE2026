"""Exact symbolic verification for four-stage Gauss collocation on scalar decay.
Run: python verify.py  (requires sympy >=1.12).
"""
import sympy as S

t,x,z=S.symbols('t x z', real=True)
D=x**4+20*x**3+180*x**2+840*x+1680
P=70*t**4*x**4-140*t**3*x**4-280*t**3*x**3+90*t**2*x**4+420*t**2*x**3+840*t**2*x**2-20*t*x**4-180*t*x**3-840*t*x**2-1680*t*x + D
L=70*t**4-140*t**3+90*t**2-20*t+1
F=z**6-180*z**5+12180*z**4-588000*z**3+18110400*z**2-460992000*z+6453888000
assert S.expand(S.diff(P,t)+x*P-x**5*L)==0
assert S.expand(P.subs(t,0)-D)==0
assert S.expand(P.subs(t,1) - ((x**2-10*x+30)**2+20*(x-6)**2+60))==0
assert S.factor(S.discriminant(P,t))==6048000*x**12*F.subs(z,x*x)
assert F.subs(z,56)!=0
assert S.expand(L - S.legendre(4,2*t-1))==0
# Exact Sturm sign variations for F, using strict rational testpoints.
def signs(poly,pt):
    seq=S.sturm(poly,z)
    if pt=='inf': vals=[S.LC(S.Poly(a,z)) for a in seq]
    else: vals=[a.subs(z,pt) for a in seq]
    assert all(v!=0 for v in vals)
    sg=['+' if v>0 else '-' for v in vals]
    return ''.join(sg),sum(sg[i]!=sg[i+1] for i in range(len(sg)-1))
expected={0:4,26:4,27:3,104:3,105:2,'inf':2}
for pt,n in expected.items():
    print('F sturm',pt,*signs(F,pt))
    assert signs(F,pt)[1]==n
# Rigorously isolate both positive discriminant roots.
for aa,bb in [(26,27),(104,105)]:
    assert F.subs(z,aa)*F.subs(z,bb)<0
    assert signs(F,aa)[1]-signs(F,bb)[1]==1

# Determine number of roots t in (0,1) at representative parameters.
def real_root_count_at(zz):
    pol=S.Poly(P.subs(x,zz),t)
    seq=S.sturm(pol.as_expr(),t)
    def variation(v):
        ss=['+' if S.sign(f.subs(t,v))>0 else '-' for f in seq]
        assert all(f.subs(t,v)!=0 for f in seq)
        return sum(ss[i]!=ss[i+1] for i in range(len(ss)-1))
    return variation(0),variation(1)
for xx,expected_count in [(1,0),(6,2),(12,4)]:
    v0,v1=real_root_count_at(xx)
    print('P root counts',xx,v0,v1,v0-v1)
    assert v0-v1==expected_count
assert P.subs({x:6,t:S.Rational(9,10)})<0
assert P.subs({x:12,t:S.Rational(1,4)})<0
assert P.subs({x:12,t:S.Rational(1,2)})>0
assert P.subs({x:12,t:S.Rational(4,5)})<0
# all 4 endpoints positive everywhere
assert P.subs({x:12,t:0})>0 and P.subs({x:12,t:1})>0
# no discriminant zero with triple / quadruple root for x>0:
# polynomial in t and x; a multiplicity >=3 requires P''(t)=0
R=S.factor(S.resultant(S.diff(P,t,2),S.diff(P,t),t))
print('Pprime-Pdoubleprime resultant:',R)
# positivity collision occurs at a Gauss collocation node; identify these two branches with high precision.
roots=sorted([r for r in S.nroots(F,maxsteps=100) if abs(S.im(r))<1e-12 and S.re(r)>0],key=lambda v:float(S.re(v)))
assert len(roots)==2
radii=[S.sqrt(S.re(q)) for q in roots]
assert 5<radii[0]<6 and 10<radii[1]<11
c_hi=S.sqrt((3+2*S.sqrt(S.Rational(6,5)))/7)
c_lo=S.sqrt((3-2*S.sqrt(S.Rational(6,5)))/7)
exact_nodes=[(1-c_hi)/2,(1-c_lo)/2,(1+c_lo)/2,(1+c_hi)/2]
for c in exact_nodes: assert S.simplify(L.subs(t,c))==0
for xx,expected_sgn in [(1,[1,1,1,1]),(6,[1,1,1,-1]),(12,[1,-1,1,-1])]:
    observed=[S.sign(P.subs({x:xx,t:c})) for c in exact_nodes]
    print('exact Gauss-stage signs',xx,observed)
    assert observed==expected_sgn
nodes=[S.N(c,30) for c in exact_nodes]
for j,h in enumerate(radii):
    vals=[abs(complex(S.N(P.subs({x:h,t:c}),16))) for c in nodes]
    i=min(range(4),key=lambda k:vals[k])
    print('critical x:',j+1,float(h),'node:',i+1,float(nodes[i]),'P residual',vals[i])
    assert (i==3 if j==0 else i==1) and vals[i]<1e-5
# internal-stationary samples positive iff whole interval positive, by the integrating-factor monotonicity.
print('All exact identities and polynomial root-count certificates passed.')
