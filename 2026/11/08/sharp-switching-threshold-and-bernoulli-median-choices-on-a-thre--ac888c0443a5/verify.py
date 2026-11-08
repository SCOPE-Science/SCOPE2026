"""Exact-rational reproducibility checks for the discrete-neighbor weighted-median path."""
from fractions import Fraction as F
from itertools import product


def update(a,c,b,s):
    # Edge weights for center 1/2,1/2; each leaf only observes center.
    # All three nodes update from old opinions synchronously.
    med = a if abs(c-a) <= abs(c-b) else b
    return (1-s)*a+s*c, (1-s)*c+s*med, (1-s)*b+s*c


def sign(w):
    return 1 if w>0 else -1


def check_family():
    count=0
    rates=[F(1,5),F(1,2),F(3,5),F(2,3),F(7,10),F(3,4),F(4,5),F(9,10)]
    starts=[(F(i,20),F(j,20),F(k,20)) for i in (2,6,10) for j in range(1,19,2) for k in (11,17,19) if i<k]
    for s in rates:
        q=1-s
        for a,c,b in starts:
            if a>=b: continue
            m=(a+b)/2;d=(b-a)/2; z=c-m; h=(c+m)/2
            for t in range(12):
                m1=(a+b)/2;d1=(b-a)/2;z1=c-m1;h1=(c+m1)/2
                assert (m,d,z,h)==(m1,d1,z1,h1)
                w=z/d
                e=sign(w)
                an,cn,bn=update(a,c,b,s)
                assert ((bn-an)/2)==q*d
                assert cn-(an+bn)/2 == (1-2*s)*z+s*e*d
                assert (cn+(an+bn)/2)/2 == h+ s*e*d/2
                assert (cn-(an+bn)/2)/((bn-an)/2) == (1-2*s)*w/q+s*e/q
                assert 0<=an<=1 and 0<=cn<=1 and 0<=bn<=1
                a,c,b=an,cn,bn
                m=(a+b)/2;d=q*d;z=(1-2*s)*z+s*e*(d/q);h=h+s*e*(d/q)/2
                count+=1
    return count


def check_invariant_cylinders():
    # At s=3/4: w -> 3 sign(w)-2w; inverse of each branch.
    # Every binary length-k cylinder has exact length 6/2^k.
    count=0
    for k in range(1,10):
        for word in product((-1,1), repeat=k):
            lo,hi=F(-3),F(3)
            for symbol in reversed(word):
                # inverse image of [lo,hi] on branch symbol
                xlo=(F(3)*symbol-hi)/2
                xhi=(F(3)*symbol-lo)/2
                assert xlo>= (0 if symbol==1 else -3)
                assert xhi<= (3 if symbol==1 else 0)
                lo,hi=xlo,xhi
            assert hi-lo == F(6,2**k)
            count+=1
    return count


def check_finite_switching():
    count=0
    for s in [F(1,3),F(1,2),F(3,5),F(2,3)]:
        q=1-s
        for n in range(-600,601,13):
            w=F(n,23)
            seq=[]
            for t in range(200):
                seq.append(sign(w))
                w=((1-2*s)*w+s*sign(w))/q
            assert len(set(seq[-40:]))==1, (s,n,seq[-40:])
            count+=1
    return count


def check_critical_witness():
    s=F(3,4);a=F(2,5);b=F(3,5);c=F(9,10)
    m=(a+b)/2;d=(b-a)/2;w=(c-m)/d
    assert w==4
    signs=[]
    for i in range(20):
        signs.append(sign(w))
        a,c,b=update(a,c,b,s)
        m=(a+b)/2;d=(b-a)/2;w=(c-m)/d
    assert signs == [1 if i%2==0 else -1 for i in range(20)]
    return len(signs)

if __name__=='__main__':
    n=check_family();m=check_invariant_cylinders();r=check_finite_switching();k=check_critical_witness()
    print(f'VERIFY_OK {n} rational recurrence identities; {m} exact cylinder lengths; {r} low-step switching trajectories; {k} alternating-witness steps')
