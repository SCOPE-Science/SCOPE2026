"""Finite checks of associative group-algebra retractions for D8 and Q8.
Python 3 standard library only. Run: python verify.py.
"""
from collections import Counter
from functools import lru_cache

def table(group):
    def mul(x,y):
        i,b=x&3,x>>2
        j,d=y&3,y>>2
        v=(i+(-j if b else j)+(2*b*d if group=='Q8' else 0))%4
        return v|((b^d)<<2)
    return [[mul(x,y) for y in range(8)] for x in range(8)]

def finite_field(q):
    assert q in (2,4)
    if q==2:
        return (lambda a,b:a&b)
    def times(a,b):
        z=0
        for i in range(2):
            for j in range(2):
                if a&(1<<i) and b&(1<<j):
                    k=i+j
                    z^=3 if k==2 else 1<<k
        return z
    return times

def sqzero_count(group,q):
    g=table(group); times=finite_field(q)
    counts=Counter(); c_ideal=set()
    # Elements in augmentation ideal. In char 2, first coordinate fixed by remaining seven.
    for z in range(q**7):
        v=[0]*8; aug=0; x=z
        for i in range(1,8):
            v[i]=x%q; aug^=v[i]; x//=q
        v[0]=aug
        result=[0]*8
        for i in range(8):
            if not v[i]:continue
            for j in range(8):
                if v[j]: result[g[i][j]]^=times(v[i],v[j])
        if any(result):continue
        # membership cA = coefficient pairing (0,2),(1,3),(4,6),(5,7)
        in_c=all(v[i]==v[i+2] for i in (0,1,4,5))
        counts['central' if in_c else 'noncentral']+=1
    expected=(q**4, 2*(q-1)*q**4 if group=='D8' else 0)
    got=(counts['central'],counts['noncentral'])
    assert got==expected,(group,q,got,expected)
    print('square_zero',group,q,got)

def hom_count_two(group):
    g=table(group)
    @lru_cache(None)
    def mul(a,b):
        z=0
        for i in range(8):
            if a>>i&1:
                for j in range(8):
                    if b>>j&1:z^=1<<g[i][j]
        return z
    def rank(vec):
        pivots={}
        for v in vec:
            while v:
                k=v.bit_length()-1
                if k in pivots:v^=pivots[k]
                else:
                    pivots[k]=v
                    break
        return len(pivots)
    units=[x for x in range(256) if x.bit_count()%2]
    hist=Counter(); total=0
    for u in units:
        u2=mul(u,u);u3=mul(u2,u)
        if mul(u2,u2)!=1:continue
        powers=(1,u,u2,u3)
        for v in units:
            if mul(v,v)!=(1 if group=='D8' else u2):continue
            if mul(v,u)!=mul(u3,v):continue
            total+=1
            images=[mul(powers[i&3], v if i&4 else 1) for i in range(8)]
            def evaluate(a):
                z=0
                for i in range(8):
                    if a>>i&1:z^=images[i]
                return z
            if evaluate(u)!=u or evaluate(v)!=v:continue
            hist[rank(images)]+=1
    expected={1:1,8:1}
    if group=='D8':expected[2]=2*2**5
    assert dict(hist)==expected,(group,dict(hist),expected)
    print('idempotent_maps',group,'GF2',dict(sorted(hist.items())),'all_homs',total)

def main():
    for group in ('D8','Q8'):
        hom_count_two(group)
        for q in (2,4):sqzero_count(group,q)
    print('VERIFY_OK')

if __name__=='__main__':main()
