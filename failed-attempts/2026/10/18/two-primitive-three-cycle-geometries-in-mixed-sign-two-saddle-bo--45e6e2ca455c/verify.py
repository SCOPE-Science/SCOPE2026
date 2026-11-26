"""Exact-algebra checks for prime-three cycles of the mixed-sign border-collision map.

Run: python verify.py (requires SymPy). Exact rational arithmetic only.
The symbolic identities supplement, but do not replace, the structural proof.
"""
import sympy as s
from fractions import Fraction

a,b,c,d=s.symbols('a b c d',real=True)
AL=s.Matrix([[a,1],[-b,0]])
AR=s.Matrix([[c,1],[-d,0]])
e=s.Matrix([1,0])
K=a*c+a*d+b*d-b+c+1
J=a*c+a+b*c+b*d-d+1
QL=a*a+a*b+a+b*b-b+1
QR=c*c+c*d+c+d*d-d+1
DL=1-a*a*c+a*b+a*d+b*b*d+b*c
DR=1-a*c*c+a*d+b*c+b*d*d+c*d
TL=a*a*c-a*b-a*d-b*c
SL=s.expand(1+TL+b*b*d)


def cycle(mats):
    P=s.eye(2)
    q=s.zeros(2,1)
    for A in mats:
        P=A*P
        q=A*q+e
    z0=(s.eye(2)-P).inv()*q
    pts=[z0]
    for A in mats[:-1]:
        pts.append(s.simplify(A*pts[-1]+e))
    return P,pts

P1,cs1=cycle([AL,AL,AR]); P2,cs2=cycle([AL,AR,AR]);
for P,cs,D,X in [(P1,cs1,DL,[K,J,QL]),(P2,cs2,DR,[QR,J,K])]:
    assert s.simplify((s.eye(2)-P).det()-D)==0
    assert all(s.simplify(cs[i][0]-X[i]/D)==0 for i in range(3))
    assert s.simplify(P.det()-(b*b*d if P is P1 else b*d*d))==0
assert s.simplify(s.trace(P1)-TL)==0
assert s.simplify(QL-(a*a+a*b+a+b*b-b+1))==0
assert s.simplify(QR-(c*c+c*d+c+d*d-d+1))==0
assert s.simplify(SL-(1+s.trace(P1)+P1.det()))==0

# Fixed one-piece maps are saddles for all parameters in the theorem;
# check explicit rational sample and the entire witness line identities.
v={a:s.Rational(5,4),b:s.Rational(1,5),c:-5}
assert s.simplify(DL.subs(v) - (129*(4*d+25)/400))==0
assert s.simplify(DR.subs(v) - ((d-25)*(4*d+25)/20))==0
assert s.simplify(K.subs(v) - ((29*d-209)/20))==0
assert s.simplify(J.subs(v) - (-(4*d+25)/5))==0
assert s.simplify(SL.subs(v)+(484*d+2425)/400)==0
assert s.simplify(TL.subs(v)+(20*d+113)/16)==0
assert s.simplify((b*b*d).subs(v)-d/25)==0
for dd in [s.Rational(-599,100),-s.Rational(11,2),-s.Rational(2425,484),-5,-4,-2,-s.Rational(1,1000)]:
    vv={**v,d:dd}
    assert all(s.factor(Q.subs(vv))>0 for Q in (QL,QR))
    assert K.subs(vv)<0 and J.subs(vv)<0
    assert DL.subs(vv)>0 and DR.subs(vv)<0
    assert s.factor(P1.det().subs(vv))<0 and s.factor(P2.det().subs(vv))>0
    for mats,coords in [([AL,AL,AR],cs1),([AL,AR,AR],cs2)]:
        points=[point.subs(vv) for point in coords]
        assert [s.sign(p[0]) for p in points] == ([-1,-1,1] if mats[1]==AL else [-1,1,1])
        for k,A in enumerate(mats):
            assert A.subs(vv)*points[k]+e==points[(k+1)%3]
# On the stability edge, -1 is a multiplier and the other is strictly inside the unit circle.
edge={**v,d:-s.Rational(2425,484)}
assert s.factor(s.det(-s.eye(2)-P1.subs(edge)))==0
assert 0<-s.Rational(2425,484)/25*-1<1 # positive second multiplier -delta on edge
# Independent exact checks away from the one-dimensional witness slice.
for aa,bb,cc,dd,expected in [
    (s.Rational(9,2),s.Rational(1,2),-s.Rational(33,10),-s.Rational(6,5),2),
    (s.Rational(21,10),s.Rational(2,5),-s.Rational(13,10),-s.Rational(4,5),0),
]:
    u={a:aa,b:bb,c:cc,d:dd}
    present=[K.subs(u)<0 and J.subs(u)<0 and DL.subs(u)>0,
             K.subs(u)<0 and J.subs(u)<0 and DR.subs(u)<0]
    assert sum(1 for flag in present if flag)==expected
    for flag,matrices,pts in zip(present,[[AL,AL,AR],[AL,AR,AR]],[cs1,cs2]):
        if flag:
            orbit=[z.subs(u) for z in pts]
            assert all(m.subs(u)*orbit[i]+e==orbit[(i+1)%3] for i,m in enumerate(matrices))
            assert all((orbit[i][0]<0)==(m==AL) for i,m in enumerate(matrices))
print('PASS: exact symbolic identities, seven stability-line samples, two generic-domain samples, and stability-edge multiplier')
