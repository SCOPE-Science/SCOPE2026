"""Exact characteristic-seven Cartier-profile checks for a cyclic genus-four cover.

Only Python's standard library is required.  The field F_49 is F_7[z]/(z^2+1).
All operations are exact finite-field arithmetic.
"""

P = 7
ZERO = (0, 0)
ONE = (1, 0)

def add(a, b): return ((a[0]+b[0])%P, (a[1]+b[1])%P)
def neg(a): return ((-a[0])%P, (-a[1])%P)
def sub(a,b): return add(a,neg(b))
def mul(a,b): return ((a[0]*b[0]-a[1]*b[1])%P,(a[0]*b[1]+a[1]*b[0])%P)
def pw(a,n):
    out=ONE
    while n:
        if n&1:out=mul(out,a)
        a=mul(a,a);n//=2
    return out

def inv(a):
    assert a!=ZERO
    return pw(a,47)
def polmul(a,b):
    out=[ZERO]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=add(out[i+j],mul(x,y))
    return out

def polpow(a,n):
    out=[ONE]
    for _ in range(n):out=polmul(out,a)
    return out

def rank(m):
    rows=[list(row) for row in m]
    n=len(rows); q=len(rows[0]); i=0
    for col in range(q):
        pivot=next((r for r in range(i,n) if rows[r][col]!=ZERO),None)
        if pivot is None:continue
        rows[i],rows[pivot]=rows[pivot],rows[i]
        v=inv(rows[i][col]);rows[i]=[mul(v,x) for x in rows[i]]
        for r in range(n):
            if r!=i and rows[r][col]!=ZERO:
                t=rows[r][col]
                rows[r]=[sub(x,mul(t,y)) for x,y in zip(rows[r],rows[i])]
        i+=1
        if i==n:break
    return i

def matmul(a,b):
    return [[sumfield([mul(a[i][k],b[k][j]) for k in range(len(b))])
             for j in range(len(b[0]))] for i in range(len(a))]

def sumfield(z):
    r=ZERO
    for a in z:r=add(r,a)
    return r

def coeff_polynomial(t):
    f=polmul([ZERO,sub(ZERO,t),ONE], [neg(ONE),ONE]) # x(x-t)(x-1)
    assert len(f)==4
    f2=polpow(f,2);f5=polpow(f,5)
    return f2[6],f2[5],f5[6],f5[13]

def matrix(t):
    c6,v,a,b=coeff_polynomial(t)
    assert c6==ONE
    # C is inverse-Frobenius-linear; seventh roots are seventh powers in F_49.
    m=[[ZERO for _ in range(4)] for _ in range(4)]
    m[2][1]=pw(a,7); m[3][1]=pw(b,7)
    m[0][2]=ONE;m[0][3]=pw(v,7)
    return m,a,b,v

def j_invariant(t):
    n=pw(add(sub(pw(t,2),t),ONE),3)
    d=mul(pw(t,2),pw(sub(t,ONE),2))
    return mul((4,0),mul(n,inv(d)))

def test():
    field=[(a,b) for a in range(7) for b in range(7)]
    roots=[]
    for t in field:
        if t in (ZERO,ONE):continue
        m,a,b,v=matrix(t)
        m7=[[pw(y,7) for y in row] for row in m]
        m2=matmul(m,m7)
        m3=matmul(m,[[pw(y,7) for y in row] for row in m2])
        r=(rank(m),rank(m2),rank(m3))
        assert r in [(2,0,0),(2,1,0)], (t,r)
        pval=add(a,mul(b,pw(v,7)))
        assert (pval==ZERO)==(r==(2,0,0))
        if pval==ZERO:
            j=j_invariant(t)
            assert j in ((4,0),(6,0)),(t,j)
            roots.append((t,j))
    assert len(roots)==9, roots
    assert sum(j==(6,0) for _,j in roots)==3
    assert sum(j==(4,0) for _,j in roots)==6
    print('CARTIER_CHAR7_49_EXACT_OK',len(field)-2,'smooth parameters;',len(roots),'square-zero;', 'j4=6, j6=3')

if __name__=='__main__':test()
