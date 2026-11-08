"""Independent bipartite-block algebra checks; no use of the direct checker."""

def gf_rank(rows):
    basis={}
    for r in rows:
        while r:
            i=r.bit_length()-1
            if i not in basis:
                basis[i]=r;break
            r^=basis[i]
    return len(basis)

def mm(a,b):
    ans=[]
    for ar in a:
        z=0
        while ar:
            j=(ar & -ar).bit_length()-1
            z^=b[j];ar&=ar-1
        ans.append(z)
    return ans

def tr(a,m):return [sum(((a[i]>>j)&1)<<i for i in range(m)) for j in range(m)]

def I(m):return [1<<i for i in range(m)]

def xor(a,b):return [x^y for x,y in zip(a,b)]

for d in range(2,8):
    even=[x for x in range(1<<d) if x.bit_count()%2==0]
    odd=[x for x in range(1<<d) if x.bit_count()%2==1]
    m=len(even)
    h=[sum(1<<j for j,v in enumerate(odd) if (x^v).bit_count()==1) for x in even]
    ht=tr(h,m)
    hh=mm(h,ht)
    expect=I(m) if d%2 else [0]*m
    assert hh==expect
    u=even.index(0);v=odd.index(1)
    h2=h[:];h2[u]^=1<<v
    assert (h2[u]>>v)&1==0
    k=mm(h2,tr(h2,m));kk=mm(tr(h2,m),h2)
    if d%2:
        assert gf_rank(h2)==m-1
        assert gf_rank(k)==m-1
        assert gf_rank(xor(k,I(m)))==2
        assert gf_rank(mm(xor(k,I(m)),xor(k,I(m))))==1
        assert gf_rank(mm(mm(xor(k,I(m)),xor(k,I(m))),xor(k,I(m))))==1
        assert gf_rank(xor(kk,I(m)))==2
        assert gf_rank(mm(xor(kk,I(m)),xor(kk,I(m))))==1
    else:
        assert gf_rank(h)==m//2
        assert gf_rank(h2)==m//2+1
    print('bipartite-block',d,'m',m,'rank-original',gf_rank(h),'rank-deleted',gf_rank(h2),'rank-square',gf_rank(k))
print('BLOCK_CHECKS_PASS')
