"""Independent finite-field checks of square-zero derivations of truncated polynomial algebras."""
from itertools import product
from collections import Counter

def gf_mul(a,b,q):
    if q == 2:return a & b
    if q == 4:
        v=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1: v ^= 1<<(i+j)
        if v&8: v^=0b1100
        if v&4: v^=0b0111
        return v
    raise ValueError(q)

def mul(a,b,n,q):
    out=[0]*n
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:n-i]):
                if y:out[i+j]^=gf_mul(x,y,q)
    return out

def apply_deriv(f,g,n,q):
    df=[0]*n
    for i in range(1,n,2):df[i-1]=g[i]
    return mul(f,df,n,q)

def mat_rank(cols,n,q):
    # Row reduction with lookup inverses in F2 or F4.
    rows=[[c[i] for c in cols] for i in range(n)]
    nc=len(cols);pivot=0
    for col in range(nc):
        row=next((r for r in range(pivot,n) if rows[r][col]),None)
        if row is None:continue
        rows[row],rows[pivot]=rows[pivot],rows[row]
        a=rows[pivot][col]
        ai=next(x for x in range(1,q) if gf_mul(a,x,q)==1)
        rows[pivot]=[gf_mul(ai,z,q) for z in rows[pivot]]
        for r in range(n):
            if r!=pivot and rows[r][col]:
                coeff=rows[r][col]
                rows[r]=[x ^ gf_mul(coeff,y,q) for x,y in zip(rows[r],rows[pivot])]
        pivot+=1
        if pivot==n:break
    return pivot

def expected(m,q):
    C=Counter({0:1})
    for r in range(1,m+1): C[r]+=(q-1)*q**(r-1)
    for b in range(1,m//2+1):
        w=(q-1)*q**(b-1)
        C[b]+=w*q**(b-1)
        for r in range(b,m-b+1):C[r]+=w*(q-1)*q**(r-1)
    return dict(sorted(C.items()))

def check(q,n):
    m=n//2
    C=Counter()
    valid=0
    for coeff in product(range(q),repeat=n):
        if n%2 and coeff[0]:continue
        f=list(coeff)
        if any(apply_deriv(f,apply_deriv(f,[int(i==j) for i in range(n)],n,q),n,q) != [0]*n for j in range(n)):
            continue
        cols=[apply_deriv(f,[int(i==j) for i in range(n)],n,q) for j in range(n)]
        rank=mat_rank(cols,n,q)
        C[rank]+=1; valid+=1
    target=expected(m,q)
    assert dict(sorted(C.items()))==target,(q,n,C,target)
    assert valid==q**m+(m//2)*(q-1)*q**(m-1)
    print('CHECK',q,n,'count',valid,'ranks',target)

if __name__=='__main__':
    for q,n in ((2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(4,2),(4,3),(4,4),(4,5),(4,6)):
        check(q,n)
    print('VERIFY_OK')
