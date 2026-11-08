"""Finite exact checks for bipartite edge-clock coverage. Run: python verify.py"""
from fractions import Fraction
from itertools import permutations, product
from math import comb, factorial

checks = 0

def exact_tie(a,b):
    """Exact probability that last isolated left/right vertices disappear together."""
    total = Fraction(0)
    for i in range(a):
        for j in range(b):
            exponent = a+b-1+i*(b-1)+j*(a-1)-i*j
            total += Fraction((-1)**(i+j)*comb(a-1,i)*comb(b-1,j), exponent)
    return a*b*total


def exact_joint_cdf(a,b,qu,qv):
    """P(all rows covered by u, all cols by v), q_u=e^-u, q_v=e^-v."""
    ans = Fraction(0)
    for i in range(a+1):
        for j in range(b+1):
            ans += (-1)**(i+j)*comb(a,i)*comb(b,j)*qu**(i*b)*qv**(j*a)/max(qu,qv)**(i*j)
    return ans


def exhaustive_tie(a,b):
    hist=[0,0,0]
    for order in permutations(range(a*b)):
        rows=[-1]*a; cols=[-1]*b
        for t,e in enumerate(order):
            i,j=divmod(e,b)
            if rows[i]<0: rows[i]=t
            if cols[j]<0: cols[j]=t
        x=max(rows); y=max(cols)
        hist[(x>y)-(x<y)+1] += 1
    return [Fraction(h,factorial(a*b)) for h in hist]


def exhaustive_joint(a,b,qu,qv):
    # Three disjoint states per edge: appeared by earlier time,
    # appeared between times, or not yet appeared by later time.
    early=min(1-qu,1-qv)
    late=abs(qu-qv)
    absent=min(qu,qv)
    weights=(early,late,absent)
    result=Fraction(0)
    for profile in product(range(3),repeat=a*b):
        # q_u >= q_v means u<=v (rows checked earlier).
        rows=set(); cols=set()
        for e,c in enumerate(profile):
            i,j=divmod(e,b)
            if c==0:
                rows.add(i);cols.add(j)
            elif c==1:
                if qu>=qv:cols.add(j)
                else:rows.add(i)
        if len(rows)==a and len(cols)==b:
            prod=Fraction(1)
            for c in profile:prod*=weights[c]
            result+=prod
    return result

for a,b in ((1,1),(1,2),(2,2),(2,3),(3,2),(2,4),(4,2),(3,3)):
    T=exact_tie(a,b)
    hist=exhaustive_tie(a,b)
    assert T==hist[1], (a,b,T,hist)
    assert sum(hist)==1
    checks+=2
    print('tie',a,b,str(T),'left-wins',str(hist[2]),'right-wins',str(hist[0]))
for a in range(1,4):
    for b in range(1,4):
        for qu,qv in ((Fraction(1,2),Fraction(1,4)),(Fraction(1,4),Fraction(1,2)),(Fraction(1,2),Fraction(1,2))):
            got=exhaustive_joint(a,b,qu,qv)
            pred=exact_joint_cdf(a,b,qu,qv)
            assert got==pred,(a,b,qu,qv,got,pred)
            checks+=1
for b in range(2,10):
    assert exact_tie(2,b)==Fraction(1,comb(2*b-1,b-1))
    checks+=1
print('PASS',checks,'exact finite checks (exhaustive edge orders, two-time edge histories, special formula)')
