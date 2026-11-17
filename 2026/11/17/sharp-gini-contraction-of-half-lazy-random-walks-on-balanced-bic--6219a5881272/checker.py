from fractions import Fraction as Q
from itertools import product

def g(vals):
    return sum(abs(a-b) for i,a in enumerate(vals) for b in vals[i+1:])

def apply(m,vals):
    A=vals[:m];B=vals[m:]
    av=sum(A,Q(0))/m;bv=sum(B,Q(0))/m
    return [(x+bv)/2 for x in A]+[(x+av)/2 for x in B]

cutcount=0
for m in range(1,8):
    K=Q(0) if m==1 else Q(3*(m-1),2*(2*m-1))
    mx=Q(0)
    for bits in product([0,1],repeat=2*m):
        if min(bits)==max(bits): continue
        cutcount+=1
        f=[Q(i) for i in bits]
        val=g(apply(m,f))/g(f)
        mx=max(mx,val)
        r=sum(bits[:m]);s=sum(bits[m:]);k=r+s;d=abs(r-s)
        predicted=Q(m*k-r*r-s*s)+Q(d*(r*s+(m-r)*(m-s)),2*m)
        assert g(apply(m,f))==predicted,(m,r,s)
        assert val<=K,(m,r,s,val,K)
    assert mx==K,(m,mx,K)
print('EXACT_FULL_BINARY_CUTS_PASSED',cutcount)

orbitcount=0
for m in range(2,101):
    K=Q(3*(m-1),2*(2*m-1))
    for r in range(m+1):
        for s in range(m+1):
            k=r+s
            if k in (0,2*m):continue
            orbitcount+=1
            d=abs(r-s)
            v=Q(m*k-r*r-s*s)+Q(d*(r*s+(m-r)*(m-s)),2*m)
            assert v/Q(k*(2*m-k)) <= K,(m,r,s)
    assert Q(3*m,2*(2*m+1))>K
print('EXACT_ALL_CUT_ORBITS_AND_STRICT_MONOTONICITY_PASSED',orbitcount)
assert Q(3,4)-Q(3*99,2*(199))==Q(3,4*199)
print('SHARP_UNATTAINED_FAMILY_ENVELOPE_PASSED')
