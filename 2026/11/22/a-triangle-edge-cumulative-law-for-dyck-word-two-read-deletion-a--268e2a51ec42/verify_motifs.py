"""Independent constructive check of the canonical positive-vertex triangle bijection."""
from functools import lru_cache
from math import comb

@lru_cache(None)
def dyck(n):
    if n == 0: return ('',)
    return tuple('1'+a+'0'+b for j in range(n) for a in dyck(j) for b in dyck(n-1-j))

def height_vertices(w):
    h=0
    ans=[]
    for i,c in enumerate(w):
        if h>0: ans.append(i)
        h+=1 if c=='1' else -1
        assert h>=0
    if h>0: ans.append(len(w))
    assert h==0
    return ans

def motifs(n):
    out=set()
    for k in range(2,n):
        r=n-k
        a='10'*k; b='01'*k
        for outer in dyck(r):
            for cut in height_vertices(outer):
                left,right=outer[:cut],outer[cut:]
                for s in range(1,k):
                    for z in (a[:2*s]+b[2*s:], b[:2*s]+a[2*s:]):
                        tri=tuple(sorted((left+a+right,left+b+right,left+z+right)))
                        assert len(set(tri))==3
                        assert all(w in dyck(n) for w in tri) if n<=7 else True
                        assert tri not in out
                        out.add(tri)
    return out

if __name__=='__main__':
    for n in range(1,10):
        H = sum(len(height_vertices(w)) for w in dyck(n))
        assert H == comb(2*n+1,n-1)
        if n<=8:
            m=motifs(n)
            expected=sum(2*(k-1)*comb(2*(n-k)+1,n-k-1) for k in range(2,n))
            assert len(m)==expected,(n,len(m),expected)
            print(f'n={n} motifs={len(m)} H_n={H}')
    print('MOTIF_VERIFICATION_OK')
