"""Independent exact matrix-power and rank test for ternary second-order graph waves.
Run: python check_matrix.py
"""

def mul(a,b):
    n=len(a);m=len(b[0]);k=len(b)
    return [[sum(a[i][s]*b[s][j] for s in range(k))%3 for j in range(m)] for i in range(n)]

def power(a,k):
    n=len(a); out=[[int(i==j) for j in range(n)] for i in range(n)]
    while k:
        if k&1: out=mul(out,a)
        a=mul(a,a); k//=2
    return out

def rank(a):
    a=[row[:] for row in a]; nr=len(a); nc=len(a[0]); r=0
    for j in range(nc):
        piv=next((i for i in range(r,nr) if a[i][j]),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]
        if a[r][j]==2: a[r]=[(2*z)%3 for z in a[r]]
        for i in range(nr):
            if i!=r and a[i][j]:
                c=a[i][j];a[i]=[(u-c*v)%3 for u,v in zip(a[i],a[r])]
        r+=1
        if r==nr:break
    return r

def fixed_exponent(a,b,t):
    n=a+b;ab=a*b%3
    if ab==0:return (2*(n-2)+4*(t%3==0)) if t%4==0 else 0
    if ab==1:return (2*(n-2) if t%4==0 else 0)+(2 if t%3==0 else 1)*(1+(t%2==0))
    return (2*(n-2) if t%4==0 else 0)+(4 if t%8==0 else 0)

def matrix(a,b):
    n=a+b;s=2*n
    T=[[0]*s for _ in range(s)]
    for i in range(n):
        for j in range(n):
            if (i<a)!=(j<a):T[i][j]=1
        T[i][n+i]=2
        T[n+i][i]=1
    return T

count=0
for a in range(2,9):
    for b in range(2,9):
        T=matrix(a,b);n=len(T)
        for t in range(1,25):
            P=power(T,t)
            diff=[[(P[i][j]-int(i==j))%3 for j in range(n)] for i in range(n)]
            actual=n-rank(diff)
            expected=fixed_exponent(a,b,t)
            assert actual==expected,(a,b,t,actual,expected)
            count+=1
        bound=8 if a*b%3==2 else 12
        assert power(T,bound)==[[int(i==j) for j in range(n)] for i in range(n)]
print(f'PASS: {count} exact fixed-space dimensions on 49 parameter pairs; all 49 asserted global powers are identity.')
