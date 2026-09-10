# A(2): admissible-basis engine. Sq exponents; reduce via Adem (mod 2, Lucas binom).
import sys
from functools import lru_cache
def binom2(n,k):
    if k<0 or k>n: return 0
    return 1 if (k & ~n)==0 else 0
def adm_step(a,b): return a>=2*b
def is_adm(m):
    return all(adm_step(m[i],m[i+1]) for i in range(len(m)-1))
def deg(m): return sum(m)
def reduce_mon(m):
    # m: tuple; returns dict {admissible tuple: coef}
    # find first inadmissible adjacent pair
    for i in range(len(m)-1):
        a,b=m[i],m[i+1]
        if b>0 and a<2*b:
            out={}
            for c in range(0, a//2 + 1):
                if binom2(b-c-1, a-2*c):
                    nm = m[:i]+(a+b-c, c)+m[i+2:]
                    nm = tuple(x for x in nm if x!=0)
                    for k,v in reduce_mon(nm).items():
                        out[k]=out.get(k,0)^v
            return {k:v for k,v in out.items() if v}
    return {m:1}
# enumerate admissible monomials with all entries < 8
basis=[]
def enum(acc, maxv):
    basis.append(tuple(acc))
    for v in range(1, min(maxv,7)+1):
        enum(acc+[v], v//2 if False else 0)
# admissible: next entry b must satisfy last>=2b i.e. b<=last//2
def enum2(acc):
    basis.append(tuple(acc))
    cap = 7 if not acc else acc[-1]//2
    for v in range(1, cap+1):
        enum2(acc+[v])
enum2([])
basis=sorted(set(basis), key=lambda m:(deg(m),m))
print("num admissible entries<8:", len(basis))
degs={}
for m in basis: degs[deg(m)]=degs.get(deg(m),0)+1
print("top deg:", max(degs), "degree dist:", sorted(degs.items()))
