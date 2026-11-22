"""Weighted three-coordinate state graph, independent of bit-level enumeration."""
from math import comb
from collections import Counter

def trans(a,b,s):
    x,c,y=s
    h=2*y-b
    if h>0: x1,c1=a-1,0
    elif h<0: x1,c1=0,1
    else: x1,c1=x,c
    h=2*(x+c)-a
    y1=b if h>0 else 0 if h<0 else y
    return(x1,c1,y1)

def theorem(a,b):
    ta=comb(a,a//2) if a%2==0 else 0
    tb=comb(b,b//2) if b%2==0 else 0
    total=2**(a+b)
    if a==1:return {('period',4):total,('at',0):4,('at',1):total-4}
    if a==2:
        v=2**b+tb
        return {('period',1):total,('at',0):v,('at',1):total-2*v,('at',2):v}
    osc=(2**a-ta)*(2**b-tb)//2
    n0=4+ta*tb
    n2=ta*(2**b-2-tb)+tb*(2**a-2-ta)
    return {('period',1):total-osc,('period',2):osc,('at',0):n0,('at',1):total-n0-n2,('at',2):n2}

def run():
    tested=0
    for a in range(1,41):
        for b in range(1,41):
            counts=Counter();orbits=set()
            for x in range(a):
                for c in (0,1):
                    for y in range(b+1):
                        z=(x,c,y);seen={};trail=[]
                        while z not in seen:
                            seen[z]=len(trail);trail.append(z);z=trans(a,b,z)
                            assert len(trail)<=5,(a,b,x,c,y)
                        t=seen[z];p=len(trail)-t
                        w=comb(a-1,x)*comb(b,y)
                        counts['at',t]+=w;counts['period',p]+=w
                        if t==0:orbits.add(tuple(sorted(trail[t:])))
            exp=theorem(a,b)
            assert counts==Counter(exp),(a,b,counts,exp)
            if a==1:assert len(orbits)==1
            if a==2: assert all(len(z)==1 for z in orbits)
            if a>=3: assert len(orbits)==(5 if a%2==0 and b%2==0 else 3)
            tested+=1
    print(f'QUOTIENT PASS: {tested} parameter pairs (1..40 by 1..40); weighted by exact binomial coefficients')
if __name__=='__main__':run()
