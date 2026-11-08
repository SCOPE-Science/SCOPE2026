#!/usr/bin/env python3
"""Finite checks for LETF- iterated-classicality ladder profiles.
No external packages. This checker confirms finite cases, not the universal proof.
"""
from itertools import product
from functools import lru_cache

def profiles(k):
    result=[]
    for bits in product((0,1), repeat=2*k):
        x=bits[::2]; y=bits[1::2]
        if all(not x[i+1] or x[i]!=y[i] for i in range(k-1)):
            result.append((x,y))
    return result

def monotone_tables(k):
    # A Boolean function is represented by its set of true assignments.
    assert k<=4
    n=1<<k
    masks=[]
    for f in range(1<<n):
        if all(not((f>>a)&1) or ((f>>b)&1)
               for a in range(n) for b in range(n) if (a & b)==a):
            masks.append(f)
    return masks

def signed_antichains(k):
    # Enumerate the admissible punctured signed-profile poset.
    pts=[]
    for bits in product((0,1), repeat=2*k):
        if any(bits) and all(not bits[2*i+2] or bits[2*i]!=bits[2*i+1]
                             for i in range(k-1)):
            pts.append(bits)
    n=len(pts)
    comparable=[]
    for a in pts:
        comparable.append(sum(1<<j for j,b in enumerate(pts)
                              if all(x<=y for x,y in zip(a,b))
                                 or all(x>=y for x,y in zip(a,b))))
    @lru_cache(None)
    def count(mask):
        if mask==0:
            return 1
        # An antichain either omits x or contains x,
        # in which case all points comparable with x are forbidden.
        best=max((j for j in range(n) if mask>>j&1),
                 key=lambda j:(mask&comparable[j]).bit_count())
        return count(mask&~(1<<best))+count(mask&~comparable[best])
    return count((1<<n)-1)

def check():
    for k in range(1,8):
        rows=profiles(k)
        assert len(rows)==4*3**(k-1), (k,len(rows))
        xset={x for x,_ in rows}
        assert len(xset)==2**k, (k,len(xset))
    counts={k:len(monotone_tables(k)) for k in range(1,5)}
    assert counts=={1:3,2:6,3:20,4:168}
    # Decompose monotone 5-variable functions into two monotone
    # 4-variable functions f0<=f1, count ordered comparable pairs.
    lower=monotone_tables(4)
    d5=sum(1 for a in lower for b in lower if (a & ~b)==0)
    assert d5==7581
    for k, count in {**counts,5:d5}.items():
        assert count-2 in {1,4,18,166,7579}, (k,count)
    signed={k:signed_antichains(k) for k in (1,2,3)}
    assert signed=={1:5,2:83,3:70806},signed
    # k=1 has no positive definition of bottom, so 5-1=4 classes.
    # Independently enumerate all positive monotone Boolean functions
    # on the four signed atoms at k=2, restricted to admissible profiles.
    pts=[]
    for bits in product((0,1),repeat=4):
        if not bits[2] or bits[0]!=bits[1]:
            pts.append(sum(z<<i for i,z in enumerate(bits)))
    restrictions={tuple(f>>t&1 for t in pts)
                  for f in monotone_tables(4)
                  if not (f&1) and (f>>15)&1}
    assert len(restrictions)==83
    print('LETF_LADDER_FINITE_CHECKS_OK','signed_quotients=4,83,70806', 
          'profiles='+','.join(str(4*3**(k-1)) for k in range(1,8)),
          'D1_to_D5='+','.join(str(counts[k]) for k in range(1,5))+','+str(d5))
if __name__=='__main__':
    check()
