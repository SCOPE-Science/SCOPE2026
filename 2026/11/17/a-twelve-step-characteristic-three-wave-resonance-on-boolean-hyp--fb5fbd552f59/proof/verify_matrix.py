"""Exact characteristic-three rank checks for two-time-level waves on Boolean cubes.
Requires Python 3 standard library only. These computations corroborate, not replace, the proof.
"""
from math import comb

def rank_mod3(m):
    a = [[v % 3 for v in row] for row in m]
    rows, cols = len(a), len(a[0]); r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None: continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = 1 if a[r][c] == 1 else 2
        a[r] = [(inv*x)%3 for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                factor=a[i][c]
                a[i]=[(x-factor*y)%3 for x,y in zip(a[i],a[r])]
        r+=1
        if r==rows: break
    return r

def mul(a,b):
    size=len(a); out=[[0]*size for _ in range(size)]
    for i,row in enumerate(a):
        for k,x in enumerate(row):
            if x:
                for j,y in enumerate(b[k]):
                    out[i][j]=(out[i][j]+x*y)%3
    return out

def mm_identity(n): return [[int(i==j) for j in range(n)] for i in range(n)]

def transition(d):
    n=1<<d; m=2*n
    t=[[0]*m for _ in range(m)]
    for x in range(n):
        for b in range(d): t[x][x^(1<<b)]=1
        t[x][n+x]=2
        t[n+x][x]=1
    return t

def predicted(d,t):
    a=(2**d-(-1)**d)//3
    b=(2**d+2*(-1)**d)//3
    return 2*b*int(t%4==0)+a*int(t%2==0)*(1+int(t%3==0))+a*(1+int(t%3==0))

for d in range(0,6):
    t=transition(d); n=len(t); power=mm_identity(n)
    records=[]; first_identity=None
    for step in range(1,13):
        power=mul(power,t)
        if step in (1,2,3,4,6,12):
            mod=[[ (power[i][j]-int(i==j))%3 for j in range(n)] for i in range(n)]
            nullity=n-rank_mod3(mod)
            expected=predicted(d,step)
            assert nullity==expected,(d,step,nullity,expected)
            records.append((step,nullity))
        if first_identity is None and power==mm_identity(n): first_identity=step
    assert first_identity==(4 if d==0 else 6 if d==1 else 12),(d,first_identity)
    print(f'd={d} vertices={1<<d} global_period={first_identity} fixed_dimensions={records}')
print('PASS rank and sharp-period comparison, d=0..5')
