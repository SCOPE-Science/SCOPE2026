"""Exact finite checks supplementing an analytic theorem about scalar clipped gradients.

Run: python3 verify.py.  No external dependencies.
"""
from fractions import Fraction as Q
from itertools import product

def clip(v,c=Q(1)):
    return max(-c, min(c,v))

def field(x,atoms,c=Q(1)):
    return sum((p*clip(a*x,c) for p,a in atoms),Q(0))

def roots(atoms):
    knots=sorted(set([Q(0)]+[Q(1,1)/abs(a) for p,a in atoms]))
    test_roots=[]
    for lo,hi in zip(knots,knots[1:]):
        gl,gh=field(lo,atoms),field(hi,atoms)
        if gl==0 and lo>0:
            test_roots.append(lo)
        if gl*gh<0:
            test_roots.append((lo*gh-hi*gl)/(gh-gl))
    if field(knots[-1],atoms)==0:
        test_roots.append(knots[-1])
    return sorted(set(test_roots))

n=0
base=[(Q(1,5),Q(12)),(Q(2,5),Q(-3)),(Q(2,5),Q(1,2))]
assert sum(p*a for p,a in base)==Q(7,5); n+=1
assert sum(p*(1 if a>0 else -1) for p,a in base)==Q(1,5); n+=1
assert roots(base)==[Q(1,5),Q(1)]; n+=1
piece=[(Q(0),Q(0)),(Q(1,12),Q(7,60)),(Q(1,5),Q(0)),(Q(1,3),-Q(2,15)),(Q(1),Q(0)),(Q(2),Q(1,5)),(Q(3),Q(1,5))]
for x,y in piece:
    assert field(x,base)==y,(x,y,field(x,base)); n+=1
# Structural enumeration: all distinct magnitudes (3,2,1), sign patterns,
# rational positive probabilities with denominator 12; enforce positive
# true mean and positive far-field clipped sign.
for signed in product((-1,1),repeat=3):
    for b1 in range(1,11):
        for b2 in range(1,12-b1):
            b3=12-b1-b2
            if b3<=0: continue
            ps=[Q(b1,12),Q(b2,12),Q(b3,12)]
            aa=[signed[i]*Q(3-i) for i in range(3)]
            atoms=list(zip(ps,aa))
            if sum(p*a for p,a in atoms)<=0:continue
            if sum(p*s for p,s in zip(ps,signed))<=0:continue
            rr=roots(atoms)
            middle=ps[0]*signed[0]+ps[1]*signed[1]+ps[2]*signed[2]*Q(1,2)
            special=(signed==(1,-1,1))
            if middle<0:
                assert special and len(rr)==2,(atoms,rr,middle)
                r1=ps[0]/(ps[1]*Q(2)-ps[2])
                r2=(ps[1]-ps[0])/ps[2]
                assert rr==[r1,r2],(atoms,rr,r1,r2)
            elif middle==0:
                assert special and rr==[Q(1,2)],(atoms,rr)
            else:
                assert rr==[],(atoms,rr,middle)
            n+=1
# Verify a sharp generic example under non-unit clipping radii.
for c in (Q(1,3),Q(1),Q(5,2),Q(37)):
    for u in (Q(0),Q(1,13),Q(1,12),Q(1,8),Q(1,5),Q(1,4),Q(1,3),Q(1,2),Q(1),Q(3,2),Q(2),Q(3)):
        x=c*u
        if u<=Q(1,12): exp=Q(7,5)*x
        elif u<=Q(1,3): exp=c/Q(5)-x
        elif u<=2: exp=(x-c)/5
        else: exp=c/Q(5)
        assert field(x,base,c)==exp,(c,x,exp,field(x,base,c))
        assert field(-x,base,c)==-exp
        n+=2
# Pointwise deterministic contraction and sign checks on rational grid.
for et in (Q(1,100),Q(1,10),Q(1,2),Q(5,7)):
    for k in range(0,801):
        x=Q(k,200)
        nextx=x-et*field(x,base)
        if x<Q(1,5):
            assert 0<=nextx<=x
        elif x>Q(1,5) and x<Q(1):
            assert x<=nextx<=1
        elif x>1:
            assert 1<=nextx<=x
        n+=1
print('VERIFY_OK',n)
