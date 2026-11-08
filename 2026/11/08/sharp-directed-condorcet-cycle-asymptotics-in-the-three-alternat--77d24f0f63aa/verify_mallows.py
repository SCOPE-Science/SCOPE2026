"""Exact finite checks for the three-alternative Mallows majority-cycle law.

Uses only the Python standard library. Run: python verify_mallows.py
Finite checks complement, rather than replace, the infinite-electorate proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product
from math import comb, sqrt, pi

RANKINGS = tuple(permutations("ABC"))
COUNTER = 0

def check(condition, message="check failed"):
    global COUNTER
    COUNTER += 1
    if not condition:
        raise AssertionError(message)

def inversion_count(r):
    return sum(r.index("ABC"[i]) > r.index("ABC"[j])
               for i in range(3) for j in range(i+1,3))

def ballot_vector(r):
    return (int(r.index("A")<r.index("B")),
            int(r.index("B")<r.index("C")),
            int(r.index("C")<r.index("A")))

def weights(a,b):
    return [(ballot_vector(r),a**inversion_count(r)*b**(3-inversion_count(r)))
            for r in RANKINGS]

def weighted_cycle_count(n,a,b):
    """Weighted labeled profiles computed using a three-margin generating polynomial."""
    data=weights(a,b)
    states={(0,0,0):1}
    for _ in range(n):
        next_states=defaultdict(int)
        for (x,y,z),mass in states.items():
            for (dx,dy,dz),weight in data:
                next_states[(x+dx,y+dy,z+dz)]+=mass*weight
        states=next_states
    forward=sum(mass for (x,y,z),mass in states.items()
                if x>n//2 and y>n//2 and z>n//2)
    reverse=sum(mass for (x,y,z),mass in states.items()
                if x<=n//2 and y<=n//2 and z<=n//2)
    return forward,reverse,sum(weight for _,weight in data)**n

def brute_cycle_count(n,a,b):
    """Independent exhaustive labeled-profile enumeration; use only at small n."""
    data=weights(a,b)
    ans=[0,0]
    for profile in product(range(6),repeat=n):
        x=sum(data[i][0][0] for i in profile)
        y=sum(data[i][0][1] for i in profile)
        z=sum(data[i][0][2] for i in profile)
        mass=1
        for i in profile: mass*=data[i][1]
        if min(x,y,z)>n//2:ans[0]+=mass
        if max(x,y,z)<=n//2:ans[1]+=mass
    return tuple(ans)

def polyadd(u,v,sign=1):
    w=[0]*max(len(u),len(v))
    for i,x in enumerate(u):w[i]+=x
    for i,x in enumerate(v):w[i]+=sign*x
    while w and w[-1]==0:w.pop()
    return w

def polymul(u,v):
    w=[0]*(len(u)+len(v)-1)
    for i,x in enumerate(u):
        for j,y in enumerate(v):w[i+j]+=x*y
    return w

# Check both structural polynomial identities coefficient-by-coefficient.
q=[0,1];one=[1];t=[0,1];t2=polymul(t,t)
left=polymul(polyadd(one,[0,0,2]),polyadd([2],t2))
right=polymul(polyadd(polyadd(one,t),t2),polyadd(polyadd(one,t),t2))
expected=polymul(polyadd(one,t,sign=-1),polyadd(one,t,sign=-1))
expected=polymul(expected,polyadd(one,t2))
check(polyadd(left,right,sign=-1)==expected,"strict orientation gap identity")
left2=[1,2,-2,-1]
right2=polymul([1,-1],[1,3,1])
check(left2==right2,"Mallows remote-pair bias factorization")

for a,b in ((1,4),(1,2),(2,3),(3,4),(1,1)):
    q=Fraction(a,b)
    Z=(1+q)*(1+q+q*q)
    w=weights(a,b)
    check(sum(x for _,x in w)==b**3*Z,"normalization")
    p=q*q*(2+q)/Z
    check(p==Fraction(sum(weight for (ab,bc,ca),weight in w if ca),sum(weight for _,weight in w)),"remote-pair marginal")
    if a<b:
        check(p<Fraction(1,2),"remote-pair advantage")
        T=1+2*q
        delta=(1-q*q)/(2*T*(2+q))
        tilt=(1-p)/p
        QZ=sum(Fraction(weight,b**3)* (tilt if ca else 1) for (ab,bc,ca),weight in w)
        for idx in (0,1):
            expectation=sum(Fraction(weight,b**3)*(tilt if vec[2] else 1)*vec[idx]
                            for vec,weight in w)/QZ
            check(expectation==Fraction(1,2)+delta,"tilted adjacent majority margin")
        check(delta>0,"strict tilted gap")
    for n in (3,5,7,9,13,21,31):
        f,r,den=weighted_cycle_count(n,a,b)
        check(0<=f+r<=den,"finite probability range")
        tail=sum(Fraction(comb(n,k))*p**k*(1-p)**(n-k)
                 for k in range(n//2+1,n+1))
        check(Fraction(f,den)<=tail,"forward-cycle subset of remote reversal")
        check(f>=0 and r>=0,"orientation counts")
        if n in (3,5):
            bf,br=brute_cycle_count(n,a,b)
            check((f,r)==(bf,br),"independent enumerator mismatch")
        if a<b:
            # This is a finite diagnostic; the analytic proof supplies the limit.
            check(Fraction(f+r,den)>0,"positive chance of cycle")

print("PASS: %d exact coefficient / rational / exhaustive checks"%COUNTER)
print("Odd-electorate exact cycle probabilities and benchmark binomial tails:")
for a,b in ((1,2),(1,4)):
    q=Fraction(a,b)
    Z=(1+q)*(1+q+q*q)
    p=q*q*(2+q)/Z
    for n in (3,9,23,31):
        f,r,den=weighted_cycle_count(n,a,b)
        probability=Fraction(f+r,den)
        tail=sum(Fraction(comb(n,k))*p**k*(1-p)**(n-k)
                 for k in range(n//2+1,n+1))
        print("phi=%s n=%d cycle=%s tail=%s ratio=%.8f"%(
            str(q),n,str(probability),str(tail),float(probability/tail)))
