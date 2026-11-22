"""Finite independent checks for cyclic-block idempotent centralizer formulas.
Only the public mathematical model and its checks are included here.
"""
from itertools import product
from collections import Counter, defaultdict
from math import comb, gcd

MAPS = ((0,0), (0,1), (1,0), (1,1))
ID = (0,1)
CONSTANTS = ((0,0),(1,1))
IDEM = (ID,*CONSTANTS)

def orbit_signature(w, dihedral=False):
    m=len(w)
    return min(tuple(w[(sgn*i+k)%m] for i in range(m)) for sgn in ((1,-1) if dihedral else (1,)) for k in range(m))

def d_vector(w):
    m=len(w)
    return tuple(sum(w[i]==1 and w[(i+k)%m]==0 for i in range(m)) for k in range(m))

def expected_profile(w):
    m=len(w); a=sum(w); out=Counter()
    for d in d_vector(w):
        for j in range(m-2*d+1):
            out[m+j]+=2**a*comb(m-2*d,j)
    return out

def direct_profile(e):
    m=len(e); out=Counter()
    for k in range(m):
      for choices in product(MAPS,repeat=m):
        works=True
        for i in range(m):
          h=choices[i]; f=e[i]; target=e[(i+k)%m]
          for x in (0,1):
            if h[f[x]]!=target[h[x]]:
              works=False; break
          if not works:break
        if works:
          rank=sum(len(set(h)) for h in choices)
          out[rank]+=1
    return out

def divisors(n):return [d for d in range(1,n+1) if n%d==0]
def phi(n):return sum(gcd(k,n)==1 for k in range(1,n+1))
def poly_mul(a,b):
    out=Counter()
    for x,v in a.items():
      for y,w in b.items():out[x+y]+=v*w
    return out

def poly_pow(a,n):
    out={0:1}
    for _ in range(n):out=poly_mul(out,a)
    return out

def closed_global(m):
    out=Counter()
    for L in divisors(m):
        base=Counter({j:comb(L,j)*2**(L-j) for j in range(L+1)})
        base[L]+=1
        power=poly_pow(base,m//L)
        for j,v in power.items():out[m+j]+=2**m*phi(L)*v
    return out

if __name__=='__main__':
    for m in range(1,6):
      aggregate=Counter()
      for e in product(IDEM,repeat=m):
        word=tuple(int(x==ID) for x in e)
        got=direct_profile(e)
        target=expected_profile(word)
        assert got==target,(m,e,got,target)
        aggregate.update(got)
      assert aggregate==closed_global(m),(m,aggregate,closed_global(m))
      print('exhaustive',m,'idempotents',3**m,'commuting pairs',sum(aggregate.values()), 'rank spectrum',sorted(aggregate.items()))
    # First non-rotation-equivalent equal-unindexed-spectrum pair at length 5.
    m=5
    A5={0,1}; B5={0,2}
    w5a=tuple(int(i in A5) for i in range(m))
    w5b=tuple(int(i in B5) for i in range(m))
    assert orbit_signature(w5a,True)!=orbit_signature(w5b,True)
    assert d_vector(w5a)!=d_vector(w5b)
    assert expected_profile(w5a)==expected_profile(w5b)
    assert sum(expected_profile(w5a).values())==208
    for m in range(1,5):
        seen={}
        for w in product((0,1),repeat=m):
            key=(sum(w),tuple(sorted(d_vector(w))))
            cl=orbit_signature(w)
            if key in seen: assert seen[key]==cl
            else: seen[key]=cl
    # First non-rotation-equivalent equal-resolved-spectrum pair at length 6.
    m=6
    A6={0,1,3}; B6={0,3,5}
    w6a=tuple(int(i in A6) for i in range(m))
    w6b=tuple(int(i in B6) for i in range(m))
    assert orbit_signature(w6a)!=orbit_signature(w6b)
    assert d_vector(w6a)==d_vector(w6b)==(0,2,2,1,2,2)
    assert sum(expected_profile(w6a).values())==768
    for m in range(1,6):
        seen={}
        for w in product((0,1),repeat=m):
            key=(sum(w),d_vector(w))
            cl=orbit_signature(w)
            if key in seen: assert seen[key]==cl
            else: seen[key]=cl
    # Explicit non-dihedral, equal-resolved-spectrum pair at length 8.
    m=8
    A={0,1,3,4}; B={0,1,2,5}
    wa=tuple(int(i in A) for i in range(m))
    wb=tuple(int(i in B) for i in range(m))
    assert orbit_signature(wa,True)!=orbit_signature(wb,True)
    assert d_vector(wa)==d_vector(wb)==(0,2,3,2,2,2,3,2)
    assert expected_profile(wa)==expected_profile(wb)
    assert sum(expected_profile(wa).values())==5504
    print('homometric',A,B,'centralizer',sum(expected_profile(wa).values()),'spectrum',sorted(expected_profile(wa).items()))
    # Verify there is no non-dihedrally equivalent homometric pair on fewer than 8 blocks.
    for m in range(1,8):
      witnesses={}
      for w in product((0,1),repeat=m):
        key=(sum(w),d_vector(w))
        cl=orbit_signature(w,True)
        if key in witnesses: assert witnesses[key]==cl,(m,key,w)
        else:witnesses[key]=cl
      print('small-homometry-cutoff',m,'subsets',2**m,'patterns',len(witnesses))
    # Exhaustively recompute the vector of local intertwiner ranks.
    patterns=((ID,ID),(ID,CONSTANTS[0]),(CONSTANTS[0],ID),(CONSTANTS[0],CONSTANTS[1]))
    target=({1:2,2:2},{1:1},{1:2},{1:1,2:1})
    for (src,dst),exp in zip(patterns,target):
      c=Counter()
      for h in MAPS:
        if all(h[src[x]]==dst[h[x]] for x in (0,1)):
          c[len(set(h))]+=1
      assert c==exp,(src,dst,c,exp)
    print('LOCAL_INTERTWINER_AND_CYCLIC_SPECTRA_CHECKS_PASSED')
