from fractions import Fraction
from itertools import combinations

def primes_upto(n):
    ps=[]
    for x in range(2,n+1):
        if all(x%p for p in ps if p*p<=x): ps.append(x)
    return ps
P=[p for p in primes_upto(383) if p%2]

def I(p,a):
    return sum(Fraction(1,p**j) for j in range(a+1))

def comps(total,k,prefix=()):
    if k==1:
        yield prefix+(total,); return
    for a in range(1,total-k+2):
        yield from comps(total-a,k-1,prefix+(a,))

def abundant(n):
    f=factor_from_small(n)
    sig=1
    for p,a in f.items(): sig*=sum(p**j for j in range(a+1))
    return sig>2*n

def factor_from_small(n):
    out={}; x=n
    p=2
    while p*p<=x:
        while x%p==0:
            out[p]=out.get(p,0)+1; x//=p
        p=3 if p==2 else p+2
    if x>1: out[x]=out.get(x,0)+1
    return out

# Global largest-prime bound: with largest prime >=389, exact maximal abundancy per support count r is <2.
bounds=[]
small=[3,5,7,11]
for r in range(1,6):
    best=Fraction(0); beste=None
    for exps in comps(5,r):
        primes=(small[:r-1]+([389] if r>1 else [])) if r>1 else [3]
        val=Fraction(1)
        for p,a in zip(primes,exps): val*=I(p,a)
        if val>best: best,beste=val,exps
    bounds.append((r,best,beste))
    assert best < 2, (r,best,beste)

# Exact exhaustive enumeration with monotone pruning for each ordered exponent composition.
actual=set()
for r in range(1,6):
  for exps in comps(5,r):
    def rec(pos,start,ratio,n):
        if pos==r:
            if ratio>2: actual.add(n)
            return
        for idx in range(start,len(P)-(r-pos)+1):
            p=P[idx]
            nr=ratio*I(p,exps[pos])
            opt=nr
            jj=idx+1
            for a in exps[pos+1:]:
                opt*=I(P[jj],a); jj+=1
            if opt<=2: break
            rec(pos+1,idx+1,nr,n*(p**exps[pos]))
    rec(0,0,Fraction(1),1)

isprime=lambda q: q in set(primes_upto(max(383,q) if 'q' in globals() else 383))
prime_set=set(primes_upto(383))
expected={945,1575,2205}
expected |= {9*5*7*q for q in prime_set if 11<=q<=103}
expected |= {9*5*11*q for q in (13,17)}
expected |= {3*25*7*q for q in (11,13,17)}
expected |= {3*5*49*q for q in (11,13)}
expected.add(3*5*7*121)
expected |= {3*5*7*11*q for q in prime_set if 13<=q<=383}
expected |= {3*5*7*13*q for q in prime_set if 17<=q<=61}
expected |= {3*5*7*17*q for q in (19,23,29)}
expected.add(3*5*7*19*23)

assert len(expected)==121, len(expected)
assert actual==expected, (len(actual),len(expected),sorted(actual-expected)[:5],sorted(expected-actual)[:5])
for n in expected:
    f=factor_from_small(n)
    assert n%2==1
    assert sum(f.values())==5
    sig=1
    for p,a in f.items(): sig*=sum(p**j for j in range(a+1))
    assert sig>2*n
assert min(expected)==945 and max(expected)==442365
print('VERIFY_OK count=121 min=945 max=442365 pmax_bound=383')
for r,b,e in bounds:
    print(f'BOUND r={r} max_at_q_ge_389={b.numerator}/{b.denominator} exps={e}')
