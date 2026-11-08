from itertools import permutations
from collections import Counter
from fractions import Fraction
from math import factorial

GENERIC = frozenset((3,5,7,10,11,12,13,14,15))
WITNESS=(3,2,5,9,1,6,4,8,7)

def masks(p):
    S=set()
    for i,vi in enumerate(p):
        m=0
        for j,vj in enumerate(p):
            if i==j: continue
            t=(0 if j<i else 2)+(0 if vj<vi else 1)
            m |= 1<<t
        S.add(m)
    return frozenset(S)

def ef2_signature(p):
    # Independent two-move EF computation: 1-move types after first pebble.
    return frozenset(frozenset(((0 if j<i else 2)+(0 if p[j]<p[i] else 1)) for j in range(len(p)) if j!=i) for i in range(len(p)))

def record_count(p):
    maximum=-1; r=0
    for v in p:
        if v>maximum:
            maximum=v;r+=1
    return r

def sign(p,i,j):
    return ((i>j)-(i<j),(p[i]>p[j])-(p[i]<p[j]))

def direct_two_round_game(p,q):
    # Brute-force Spoiler and Duplicator choices, not using masks.
    for a,b in ((p,q),(q,p)):
        for i in range(len(a)):
            def reply_ok(j):
                return (all(any(sign(a,i,k)==sign(b,j,l) for l in range(len(b))) for k in range(len(a)))
                        and all(any(sign(b,j,l)==sign(a,i,k) for k in range(len(a))) for l in range(len(b))))
            if not any(reply_ok(j) for j in range(len(b))):return False
    return True

small=[p for n in range(1,5) for p in permutations(range(1,n+1))]
for p in small:
    for q in small:
        assert direct_two_round_game(p,q)==(masks(p)==masks(q))
print('TWO_ROUND_EF_CHECKS_OK pairs=',len(small)**2)

assert masks(WITNESS)==GENERIC
assert len(GENERIC)==9
for n in range(1,9):
    total=factorial(n)
    masks_frequency=Counter()
    lowrec=0
    missing13=0
    bysig={}
    for p in permutations(range(1,n+1)):
        sig=masks(p)
        expected=frozenset(sum(1<<z for z in typ) for typ in ef2_signature(p))
        assert sig==expected
        bysig.setdefault(sig,0);bysig[sig]+=1
        masks_frequency.update(sig)
        lowrec+=int(record_count(p)<=2)
        missing13+=int(13 not in sig)
    if n>=2:
        H=sum(Fraction(1,j) for j in range(1,n))
        assert Fraction(lowrec,total)==(1+H)/n
        assert missing13>=lowrec
        # An exceptional second record must be a direct sum pivot.
        upper=sum(Fraction(1,n*__import__('math').comb(n-1,i-1)) for i in range(2,n))
        assert Fraction(missing13-lowrec,total)<=upper
    print('n=',n,'types=',len(bysig),'P(mask13 absent)=',Fraction(missing13,total))
print('ALL_FINITE_CHECKS_OK')
