#!/usr/bin/env python3
"""Reproduce finite-field checks for the Pascal-line fiber theorem.
No external packages, no imported data, and no claims of infinite proof by sampling.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations

def cross(a,b,p):
    return tuple((a[(i+1)%3]*b[(i+2)%3]-a[(i+2)%3]*b[(i+1)%3])%p for i in range(3))

def primitive(v,p):
    for t in v:
        if t%p: return tuple((u*pow(t,-1,p))%p for u in v)
    raise AssertionError('vanishing Pascal line')

def formula(q,chi_neg3):
    # Multiplicity for EACH rational line of given conic-intersection type.
    S=((q-1)*((q-5)**2*(q-3)-2*(1+chi_neg3)))//12
    T=(q*(q-1)*(q-4)*(q-5))//12
    E=((q+1)*(q**3-7*q**2+15*q-13+2*(1+chi_neg3)))//12
    return {2:S,1:T,0:E}

def brute_all_prime(p):
    points=[(t*t%p,t,1) for t in range(p)]+[(1,0,0)]
    freq=Counter()
    for six in combinations(range(p+1),6):
        for rest in permutations(six[1:]):
            seq=(six[0],)+rest
            if seq[1]>seq[5]:continue
            pts=[points[i] for i in seq]
            sides=[cross(pts[i],pts[(i+1)%6],p) for i in range(6)]
            u=cross(sides[0],sides[3],p)
            v=cross(sides[1],sides[4],p)
            w=cross(sides[2],sides[5],p)
            line=primitive(cross(u,v,p),p)
            assert sum(line[i]*w[i] for i in range(3))%p==0
            freq[line]+=1
    typ=defaultdict(Counter)
    for line,m in freq.items():
        typ[sum(sum(line[i]*P[i] for i in range(3))%p==0 for P in points)][m]+=1
    chi=(-3%p)
    chi=-1 if pow(chi,(p-1)//2,p)==p-1 else 1
    expected=formula(p,chi)
    count_by_type={2:p*(p+1)//2,1:p+1,0:p*(p-1)//2}
    for t in [0,1,2]:
        if expected[t]: assert typ[t]=={expected[t]:count_by_type[t]},(p,t,typ[t],expected[t])
        else: assert not typ[t],(p,t,typ[t])
    assert sum(freq.values())==60*len(list(combinations(range(p+1),6)))
    return expected

def normalized_prime(p):
    U=[u for u in range(p) if u not in (0,1)]
    c=Counter()
    for y in U:
        for z in U:
            if y==z:continue
            inv=pow(z,-1,p)
            k=((y+z-1)*inv)%p
            for x in U:
                if x==y or x==z:continue
                d=((1+k*x)**2-4*x*y)%p
                ch=0 if d==0 else (1 if pow(d,(p-1)//2,p)==1 else -1)
                c[ch]+=1
    chi=1 if pow(-3%p,(p-1)//2,p)==1 else -1
    q=p
    AS=((q-5)**2*(q-3)-2*(1+chi))//2
    AT=(q-4)*(q-5)
    AE=(q-4)*(q*q-6*q+11)-AS
    assert all(c.get(t,0)==n for t,n in {1:AS,0:AT,-1:AE}.items()),(p,c,AS,AT,AE)
    return c

class GF25:
    # F_5[a]/(a*a-2), encoded a0+5*a1
    q=25
    @staticmethod
    def add(x,y):return ((x%5+y%5)%5)+5*((x//5+y//5)%5)
    @staticmethod
    def neg(x):return ((-x%5)%5)+5*((-(x//5))%5)
    @classmethod
    def sub(cls,x,y):return cls.add(x,cls.neg(y))
    @staticmethod
    def mul(x,y):
        a,b=x%5,x//5;c,d=y%5,y//5
        return (a*c+2*b*d)%5+5*((a*d+b*c)%5)
    @classmethod
    def pow(cls,x,n):
        r=1
        while n:
            if n&1:r=cls.mul(r,x)
            x=cls.mul(x,x);n//=2
        return r
    @classmethod
    def chi(cls,x):
        if not x:return 0
        return 1 if cls.pow(x,12)==1 else -1

def normalized_GF25():
    F=GF25; U=[x for x in range(25) if x not in (0,1)]
    count=Counter()
    for y in U:
        for z in U:
            if y==z:continue
            k=F.mul(F.sub(F.add(y,z),1),F.pow(z,23))
            for x in U:
                if x==y or x==z:continue
                tmp=F.add(1,F.mul(k,x))
                D=F.sub(F.mul(tmp,tmp),F.mul(4,F.mul(x,y)))
                count[F.chi(D)]+=1
    AS=((25-5)**2*(25-3)-2*(1+F.chi(2)))//2  # -3 equals 2 in F5
    AT=(25-4)*(25-5)
    AE=(25-4)*(25*25-6*25+11)-AS
    assert count=={1:AS,0:AT,-1:AE},(count,AS,AT,AE)
    return count

if __name__=='__main__':
    for p in (5,7,11,13):
        a=brute_all_prime(p)
        c=normalized_prime(p)
        print('ALL_LINES',p,a,'NORMALIZED',dict(c))
    for p in (17,19,23,29):
        print('NORMALIZED',p,dict(normalized_prime(p)))
    print('EXTENSION_FIELD',25,dict(normalized_GF25()))
    print('PASSED_EXACT_FINITE_CHECKS_NOT_INFINITE_PROOF')
