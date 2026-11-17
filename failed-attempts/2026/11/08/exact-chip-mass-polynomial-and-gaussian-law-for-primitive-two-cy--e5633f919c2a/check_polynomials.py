from math import comb

def poly_add(a,b):
    out=a.copy()
    for k,v in b.items():out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}
def poly_mul(a,b):
    o={}
    for i,x in a.items():
        for j,y in b.items():o[i+j]=o.get(i+j,0)+x*y
    return o
def poly_shift(a,n):return {k+n:v for k,v in a.items()}
def mix(n):
    h={}
    for r in range(n//2+1):
        if (r-n)%2:continue
        # number of matchings on cycle of n edges
        v=n*comb(n-r,r)//(n-r)
        for j in range(n-2*r+1):
            k=n+r+j
            h[k]=h.get(k,0)+2*v*comb(n-2*r,j)
    return h
def trace(n):
    # λ+^n+λ-^n via t²=(z+z²)t+z³.
    p0={0:2};p1={1:1,2:1}
    for m in range(2,n+1):
        p0,p1=p1,poly_add(poly_mul(p1,{1:1,2:1}),poly_shift(p0,3))
    out=p1
    out=poly_add(out,{n:(-1)**n,2*n:(-1)**n})
    return out

for n in range(3,151):
    a=mix(n);b=trace(n)
    assert a==b,(n,a,b)
    assert a=={3*n-k:v for k,v in a.items()}
    lo=n+(n%2);hi=2*n-(n%2)
    assert set(a)==set(range(lo,hi+1))
    assert a[lo]==a[hi]==(2 if n%2==0 else 2*n)
    assert all(v>0 for v in a.values())
    # recurrence at z=1, Pell Lucas L(n)=2L(n-1)+L(n-2)
    L0,L1=2,2
    for m in range(2,n+1):L0,L1=L1,2*L1+L0
    assert sum(a.values())==L1+2*(-1)**n
print('INDEPENDENT_POLYNOMIAL_IDENTITY_SUPPORT_SYMMETRY_ENDPOINTS_PELL', 'n=3..150 PASS')
