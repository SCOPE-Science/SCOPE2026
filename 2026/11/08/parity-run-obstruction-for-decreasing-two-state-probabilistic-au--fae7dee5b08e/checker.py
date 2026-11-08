"""Finite independent checks of the two-parity run obstruction for decreasing binary-state stochastic maps."""
from fractions import Fraction as F
from itertools import product
from random import Random
from math import factorial,comb

def runs_once(xs):
    seen=set()
    for i,a in enumerate(xs):
        if i==0 or a!=xs[i-1]:
            if a in seen: return False
            seen.add(a)
    return True

def property_word(word):
    return runs_once(word[::2]) and runs_once(word[1::2])

def formula(q,n):
    def T(m):
        if m==0:return 1
        return sum(factorial(q)//factorial(q-r)*comb(m-1,r-1) for r in range(1,min(q,m)+1))
    return T((n+1)//2)*T(n//2)

def limits(maps,n,x0):
    mn=mx=x0
    for t in range(n):
        mn,mx=min(b+s*mx for b,s in maps),max(b+s*mn for b,s in maps)
    return mn,mx

def brute(maps,n,x0):
    out=[]
    for w in product(range(len(maps)),repeat=n):
        x=x0
        for a in w:
            b,s=maps[a]
            x=b+s*x
        out.append((x,w))
    hi=max(a for a,b in out)
    lo=min(a for a,b in out)
    return (lo,hi),[w for x,w in out if x==hi],[w for x,w in out if x==lo]

def main():
    rng=Random(74661)
    cases=0
    for q in range(2,5):
        for n in range(1,9):
            if q==4 and n>=8: continue
            words=list(product(range(q),repeat=n))
            assert sum(property_word(w) for w in words)==formula(q,n)
            for rep in range(20):
                # both matrix rows legal: f(0)=b, f(1)=c with b>c
                maps=[]
                for a in range(q):
                    b=F(rng.randint(12,40),50)
                    c=F(rng.randint(1,10),50)
                    maps.append((b,c-b))
                x0=F(rng.randrange(2))
                extrema,maxs,mins=brute(maps,n,x0)
                assert extrema==limits(maps,n,x0)
                if len(maxs)==1: assert property_word(maxs[0]), (q,n,maps,maxs)
                if len(mins)==1: assert property_word(mins[0]), (q,n,maps,mins)
                cases+=1
    print(f'VERIFY_OK {cases} random exact rational decreasing-map instances; exact parity-run enumeration q=2..4 n<=8 (q4<=7)')
if __name__=='__main__':main()
