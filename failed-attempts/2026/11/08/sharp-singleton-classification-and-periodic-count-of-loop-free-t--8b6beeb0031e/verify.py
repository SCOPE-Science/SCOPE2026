#!/usr/bin/env python3
"""Reproducible exact checks of cyclic ternary two-gram uniqueness theorem."""
from itertools import product
from collections import defaultdict
from math import gcd, factorial
from functools import reduce
from fractions import Fraction

def canonical(s):
    return min(tuple(s[i:]+s[:i]) for i in range(len(s)))

def profile(s):
    e=[0]*9
    for i,x in enumerate(s): e[3*x+s[(i+1)%len(s)]]+=1
    return tuple(e)

def prediction(e):
    assert e[0]==e[4]==e[8]==0
    t=e[1]-e[3]
    assert t==e[5]-e[7]==e[6]-e[2]
    u=[min(e[1],e[3]),min(e[5],e[7]),min(e[6],e[2])]
    nz=[v for v in u if v>0]
    if not t:return len(nz)==1 or (len(nz)==2 and min(nz)==1)
    return len(nz)==0 or (len(nz)==1 and min(abs(t),nz[0])==1)

def gf_coefficient(n):
    v=3 if n>=2 and n%2==0 else 0
    v+=3 if n==4 else (6 if n>=6 and n%2==0 else 0)
    v+=2 if n>=3 and n%3==0 else 0
    v+=6 if n>=5 and n%2==1 else 0
    v+=6 if n>=8 and (n-8)%3==0 else 0
    return v

def direct(n):
    fibers=defaultdict(set)
    for t in product(range(3),repeat=n):
        if any(t[i]==t[(i+1)%n] for i in range(n)):continue
        fibers[profile(t)].add(canonical(t))
    for e,cs in fibers.items():
        assert (len(cs)==1)==prediction(e),(n,e,len(cs))
    return len([1 for cs in fibers.values() if len(cs)==1])

def phi(n):return sum(gcd(i,n)==1 for i in range(1,n+1))
def root_count(e):
    n=sum(e)
    M=[e[0:3],e[3:6],e[6:9]]
    nodes=[i for i in range(3) if sum(M[i])>0]
    r=nodes[0];other=nodes[1:]
    if len(nodes)==1:return 1
    L=[[sum(M[i][j] for j in range(3) if j!=i) if i==j else -M[i][j] for j in range(3)]for i in range(3)]
    tau=L[other[0]][other[0]] if len(other)==1 else L[other[0]][other[0]]*L[other[1]][other[1]]-L[other[0]][other[1]]*L[other[1]][other[0]]
    v=Fraction(n*tau)
    for i in nodes:v*=factorial(sum(M[i])-1)
    for x in e:v/=factorial(x)
    assert v.denominator==1
    return int(v)

def necklace_count(e):
    n=sum(e);g=reduce(gcd,e)
    return sum(phi(d)*root_count(tuple(x//d for x in e)) for d in range(1,g+1) if g%d==0)//n

def flow_profiles(n):
    for t in range(-n//3,n//3+1):
        if 3*abs(t)>n or (n-3*abs(t))%2:continue
        for u in range((n-3*abs(t))//2+1):
            for v in range((n-3*abs(t))//2-u+1):
                w=(n-3*abs(t))//2-u-v
                if t>=0:p=[t+u,t+v,t+w];m=[u,v,w]
                else:p=[u,v,w];m=[u-t,v-t,w-t]
                if t==0 and sum(x>0 for x in p)==0:continue
                yield (0,p[0],m[2],m[0],0,p[1],p[2],m[1],0)

def main():
    brute=0
    for n in range(2,11):
        c=direct(n);assert c==gf_coefficient(n),(n,c,gf_coefficient(n));brute+=1
    matrices=0
    for n in range(2,30):
        count=0
        for e in flow_profiles(n):
            num=necklace_count(e)
            assert (num==1)==prediction(e),(n,e,num)
            count+=int(num==1);matrices+=1
        assert count==gf_coefficient(n),(n,count,gf_coefficient(n))
    assert [gf_coefficient(n) for n in range(2,13)]==[3,2,6,6,11,6,15,8,9,12,11]
    print('PASS: direct exhaustive n=2..10 (%d lengths); exact Euler-tour and Burnside flow profiles n=2..29 (%d matrices); GF checks.'%(brute,matrices))
if __name__=='__main__':main()
