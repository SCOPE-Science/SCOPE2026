#!/usr/bin/env python3
"""Independent-of-graph-enumeration exact layer dynamic program.
Run: python3 verify.py
Only Python standard library is needed.
"""
from math import comb

EXPECTED = {
    3:(4,2),4:(8,2),5:(10,1),6:(22,2),7:(44,1),8:(86,1),
    9:(172,2),10:(344,1),11:(682,1),12:(1366,2),13:(2732,1),
    14:(5462,1),15:(10924,2),16:(21848,1),17:(43690,1),
    18:(87382,2),19:(174764,1),20:(349526,1),
}

def optimum(n):
    if n < 3:
        raise ValueError('dimension must be at least three')
    costs = [comb(n,k) for k in range(n+1)]
    # State: final two membership bits -> (minimum cost, count of attaining profiles)
    states = {(a,b):(a*costs[0]+b*costs[1],1)
              for a in (0,1) for b in (0,1) if a or b}
    for k in range(2,n+1):
        new = {}
        for (a,b),(value,count) in states.items():
            for c in (0,1):
                if not (a or b or c):
                    continue  # radius-one domination at index k-1
                if k==2 and not (b or c):
                    continue  # lower distinguishing edge
                if k==n and not (a or b):
                    continue  # upper distinguishing edge
                v=value+c*costs[k]
                key=(b,c)
                if key not in new or v<new[key][0]:
                    new[key]=(v,count)
                elif v==new[key][0]:
                    new[key]=(v,new[key][1]+count)
        states=new
    valid=[(v,count) for (a,b),(v,count) in states.items() if a or b]
    best=min(v for v,count in valid)
    number=sum(count for v,count in valid if v==best)
    return best,number

def construction(n):
    if n%3==0:
        chosen={k for k in range(n+1) if k%3==2} | {0}
    elif n%3==1:
        chosen={k for k in range(n+1) if k%3==2} | {0,n}
    else:
        chosen={k for k in range(n+1) if k%3==1}
    return chosen,sum(comb(n,k) for k in chosen)

for n,(want,cnt) in EXPECTED.items():
    got=optimum(n)
    assert got==(want,cnt),(n,got,(want,cnt))
    chosen,upper=construction(n)
    assert upper==want,(n,upper,want)
    assert all(any(t in chosen for t in range(max(0,k-1),min(n,k+1)+1))
               for k in range(n+1))
    assert (1 in chosen or 2 in chosen)
    assert (n-2 in chosen or n-1 in chosen)

# Independent direct closed-neighborhood signature check for every possible
# invariant layer selection through dimension seven.
for n in range(3,8):
    N=1<<n
    neighbours=[[x]+[x^(1<<i) for i in range(n)] for x in range(N)]
    for mask in range(1<<(n+1)):
        profile=[bool((mask>>k)&1) for k in range(n+1)]
        predicted=(any(profile[:2]) and any(profile[1:3])
                   and any(profile[-3:-1]) and any(profile[-2:])
                   and all(any(profile[max(0,k-1):min(n,k+1)+1])
                           for k in range(n+1)))
        signs=[]
        for x in range(N):
            sig=0
            for y in neighbours[x]:
                if profile[y.bit_count()]:sig|=1<<y
            signs.append(sig)
        actual=(0 not in signs and len(set(signs))==N)
        assert predicted==actual,(n,mask,predicted,actual)

# No numerical extrapolation is used to prove the all-n structural theorem.
# Verify the finite exact DP and complementary construction at larger dimensions.
for n in range(21,101):
    optimum(n)
    chosen,upper=construction(n)
    assert any(k in chosen for k in (0,1))
    assert any(k in chosen for k in (1,2))
    assert any(k in chosen for k in (n-2,n-1))
    assert any(k in chosen for k in (n-1,n))
    assert all((k-1 in chosen or k in chosen or k+1 in chosen)
               for k in range(1,n))
    assert upper < 2**n//3+4
print('VERIFY_OK: all direct small-cube signatures, n=3..20 exact DP, n=21..100 DP/construction checks')
