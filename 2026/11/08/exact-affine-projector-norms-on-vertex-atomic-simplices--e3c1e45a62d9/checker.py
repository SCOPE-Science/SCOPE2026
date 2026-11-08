"""Exact-rational checks for vertex-atomic affine least-squares projection on a simplex.
Run with Python 3 standard library: python checker.py
"""
from fractions import Fraction as F
from itertools import product

def inv(M):
    n=len(M)
    A=[[F(z) for z in row]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(M)]
    for k in range(n):
        q=next(i for i in range(k,n) if A[i][k])
        A[k],A[q]=A[q],A[k]
        pivot=A[k][k]
        A[k]=[v/pivot for v in A[k]]
        for i in range(n):
            if i!=k:
                p=A[i][k]
                A[i]=[a-p*b for a,b in zip(A[i],A[k])]
    return [row[n:] for row in A]

def formula(m,weights):
    c=F(m*(m+1)); r=[1/(1/c+w) for w in weights]
    z=c+sum(r)
    B=[[r[i]*F(i==j)-r[i]*r[j]/z for j in range(m)] for i in range(m)]
    plus=[]
    for i in range(m):
        b=B[i][i]
        ratio=F(1)
        for j in range(m):
            if i!=j:ratio*=b/(b-B[i][j])
        plus.append(b*(weights[i]+ratio/F(m)))
    return B,plus

def integral_1d_positive(values):
    a,b=values
    if a>=0 and b>=0:return (a+b)/2
    if a<=0 and b<=0:return F(0)
    if a>0:return a*a/(2*(a-b))
    return b*b/(2*(b-a))

def clip_positive_triangle(vals):
    # Coordinates on the standard reference triangle: vertices (0,0),(1,0),(0,1).
    V=[(F(0),F(0),vals[0]),(F(1),F(0),vals[1]),(F(0),F(1),vals[2])]
    out=[]
    for j in range(3):
        a=V[j-1];b=V[j]
        if (a[2]>0)!=(b[2]>0):
            t=a[2]/(a[2]-b[2])
            out.append((a[0]+t*(b[0]-a[0]),a[1]+t*(b[1]-a[1]),F(0)))
        if b[2]>0:out.append(b)
    if len(out)<3:return F(0)
    # Mean over reference triangle is 2 times integral over Cartesian triangle.
    res=F(0)
    for i in range(1,len(out)-1):
        a,b,c=out[0],out[i],out[i+1]
        cross=(b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1])
        area=abs(cross)/2
        res+=2*area*(a[2]+b[2]+c[2])/3
    return res

cases=0
for m in range(2,8):
    weightsets=[tuple(F(0) for i in range(m)),tuple(F(i+1,7+i) for i in range(m)),
                tuple(F(5,3) if i==0 else F(0) for i in range(m)),
                tuple(F(0) if i%2 else F(1,17) for i in range(m))]
    for w in weightsets:
        G=[[F(1+(i==j),m*(m+1))+(w[i] if i==j else 0) for j in range(m)] for i in range(m)]
        B,plus=formula(m,w)
        assert B==inv(G)
        for i in range(m):
            assert sum(B[i][j]*(F(1,m)+w[j]) for j in range(m))==1
            assert B[i][i]>0 and all(B[i][j]<0 for j in range(m) if i!=j)
            if m==2: cont=integral_1d_positive(B[i])
            elif m==3: cont=clip_positive_triangle(B[i])
            else: cont=None
            if cont is not None:assert plus[i]==cont+w[i]*B[i][i],(m,w,i,plus[i],cont+w[i]*B[i][i])
            assert plus[i]>=1
        cases+=1
print('EXACT_GRAM_INVERSES_AND_POSITIVE_CAP_INTEGRALS_OK',cases,'WEIGHTED_CASES')

for m in range(2,15):
    base=F(m**m,(m+1)**(m-1))
    for w in (F(0),F(1,100),F(1,5),F(5,2),F(100)):
        q=F(m)*w/(1+m*m*w)
        ws=(w,)+tuple(F(0) for i in range(m-1))
        _,plus=formula(m,ws)
        other=(m-q)**m/((m+1)**(m-1)*(1-q))
        at=1+(base-1)/(1+m*m*w)
        assert plus[0]==at,(m,w,plus[0],at)
        assert all(v==other for v in plus[1:])
        if w>0:assert other>base>at
print('EXACT_SINGLE_ATOM_FORMULA_AND_STRICT_RIGIDITY_OK')
print('ALL_SIMPLEX_ATOMIC_PROJECTION_CHECKS_PASSED')
