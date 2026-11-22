"""Finite reproducibility checks for a sharp erasure threshold on spherical polygon joins.
Uses only the Python standard library. Analytic proof is in RESULT.md.
"""
from itertools import combinations
from math import acos, cos, pi, sin, sqrt


def r_of_remaining(n, indices):
    ids = sorted(indices)
    assert ids
    gaps = [((ids[(i+1) % len(ids)] - ids[i]) % n) for i in range(len(ids))]
    if len(ids) == 1:
        gaps = [n]
    return cos(pi * max(gaps) / n)


def f(r, s):
    if r > 1e-12 and s > 1e-12:
        return r*s/sqrt(r*r+s*s)
    if r < -1e-12 and s < -1e-12:
        return -r*s/sqrt(r*r+s*s)
    return 0.0


def site_vertices(p, q, erase_a, erase_b):
    a = [(cos(2*pi*j/p), sin(2*pi*j/p),0.,0.) for j in range(p) if j not in erase_a]
    b = [(0.,0.,cos(2*pi*j/q), sin(2*pi*j/q)) for j in range(q) if j not in erase_b]
    return a+b


def angular_argmin(n, indices):
    ids = sorted(indices)
    assert ids
    if len(ids) == 1:
        return (2*pi*ids[0]/n + pi) % (2*pi)
    steps = [((ids[(i+1) % len(ids)]-ids[i])%n) for i in range(len(ids))]
    j = max(range(len(ids)),key=lambda t:steps[t])
    return ((2*ids[j]+steps[j])*pi/n)%(2*pi)


def witness(p,q,erase_a,erase_b):
    a = sorted(set(range(p))-set(erase_a))
    b = sorted(set(range(q))-set(erase_b))
    if not a or not b:
        return None
    r,s=r_of_remaining(p,a),r_of_remaining(q,b)
    ta,tb=angular_argmin(p,a),angular_argmin(q,b)
    ua=(cos(ta),sin(ta)); ub=(cos(tb),sin(tb))
    if r*s>1e-14:
        aa=abs(s)/sqrt(r*r+s*s);bb=abs(r)/sqrt(r*r+s*s)
    elif r <= 1e-12:
        aa,bb=1.,0.
    else:
        aa,bb=0.,1.
    return aa*ua[0],aa*ua[1],bb*ub[0],bb*ub[1]


# One-circle gap thresholds, all possible erasure sets, not just consecutive blocks.
for n in range(3,11):
    dn=n//2
    seen=0
    for count in range(n):
        values=[]
        for deleted in combinations(range(n),count):
            remaining=set(range(n))-set(deleted)
            value=r_of_remaining(n,remaining)
            values.append(value)
            predicted=cos(pi*(count+1)/n)
            assert value>=predicted-1e-12, (n,count,deleted)
            if count==dn and value< -1e-10:
                seen+=1
                assert abs(value-predicted)<1e-12
            if count<dn:
                assert value>=-1e-12
        assert len(values)>0
    assert seen==n,(n,seen)

# Exhaustive nine-site deletion census and exact worst-point witness checks.
p,q=4,5
counts={}
for k in range(5):
    outcomes=[]
    for gone in combinations(range(p+q),k):
        A=set(gone)&set(range(p))
        B={x-p for x in gone if x>=p}
        rem_a=set(range(p))-A
        rem_b=set(range(q))-B
        if not rem_a:
            assert rem_b
            mu=min(0.,r_of_remaining(q,rem_b))
        elif not rem_b:
            mu=min(0.,r_of_remaining(p,rem_a))
        else:
            mu=f(r_of_remaining(p,rem_a),r_of_remaining(q,rem_b))
            x=witness(p,q,A,B)
            pts=site_vertices(p,q,A,B)
            objective=max(sum(a*b for a,b in zip(x,y)) for y in pts)
            assert abs(objective-mu)<1e-12,(gone,mu,objective)
            assert abs(sum(t*t for t in x)-1)<1e-12
        outcomes.append(mu)
    counts[k]=(sum(z>1e-10 for z in outcomes),
               sum(abs(z)<=1e-10 for z in outcomes),
               sum(z< -1e-10 for z in outcomes))
assert counts=={0:(1,0,0),1:(5,4,0),2:(5,31,0),3:(0,84,0),4:(0,106,20)},counts

c=cos(2*pi/5)/sqrt(1+2*cos(2*pi/5)**2)
assert abs(acos(c)+acos(-c)-pi)<1e-14
assert abs(c-0.2831584861794965)<1e-14
# Every minimal four-erasure failure is two consecutive deleted vertices per factor.
negative=[]
for gone in combinations(range(9),4):
    a=set(gone)&set(range(4))
    b={z-4 for z in gone if z>=4}
    if len(a)==4 or len(b)==5:
        continue
    value=f(r_of_remaining(4,set(range(4))-a),r_of_remaining(5,set(range(5))-b))
    if value<-1e-10:
        negative.append(gone)
        assert len(a)==len(b)==2
        assert any(a=={j,(j+1)%4} for j in range(4))
        assert any(b=={j,(j+1)%5} for j in range(5))
        assert abs(value+c)<1e-12
assert len(negative)==20

print('One-circle threshold checks: n=3..10; all nonempty remaining subsets.')
print('Square-pentagon exact sign census:',counts)
print('Worst cosine at four erasures:',-c,'unique pattern count:',len(negative))
print('Complementary single-pentagon/four-erasure angles:',acos(c)*180/pi,acos(-c)*180/pi)
print('PASS')
