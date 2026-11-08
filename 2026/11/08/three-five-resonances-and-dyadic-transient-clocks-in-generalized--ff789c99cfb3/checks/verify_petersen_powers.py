"""Direct full-size binary matrix-power checks of the zero-primary Jordan formula."""

def rank_gf2(cols):
    basis={}
    for x in cols:
        while x:
            bit=x.bit_length()-1
            if bit not in basis:basis[bit]=x;break
            x^=basis[bit]
    return len(basis)

def make_cols(n):
    cols=[]
    for v in range(2*n):
        u=v%n;inner=v>=n
        out=0
        nei=([n+u,(u-1)%n,(u+1)%n] if not inner else [u,n+(u-2)%n,n+(u+2)%n])
        for w in nei:out^=1<<w
        cols.append(out)
    return cols

def mat_mult(A,B):
    C=[]
    for z in B:
        v=0
        while z:
            a=z&-z;v^=A[a.bit_length()-1];z-=a
        C.append(v)
    return C

def nullity_formula(n,k):
    h=n&-n
    return 2*min(k,2*h)*(n%3==0)+4*min(k,h)*(n%5==0)
for n in range(5,66):
    A=make_cols(n);P=[1<<i for i in range(2*n)]
    h=n&-n; limit=2*h+2
    for k in range(1,limit+1):
        P=mat_mult(A,P)
        nul=2*n-rank_gf2(P)
        expected=nullity_formula(n,k)
        assert nul==expected,(n,k,nul,expected)
    if n<20 or n%5==0 or n%8==0:print('OK',n,'2adic',h,'zero_dim',nullity_formula(n,2*h),'kernel',nullity_formula(n,1),'max_entry',2*h if n%3==0 else h if n%5==0 else 0)
print('MATRIX_RANK_CHECKS_OK')
