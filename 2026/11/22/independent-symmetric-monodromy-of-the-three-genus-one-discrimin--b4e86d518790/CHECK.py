"""Finite-field witnesses for 3 discriminants of a triquadratic branch surface.

This script verifies degree and squarefreeness, not infinite monodromy;
the latter follows by the incidence and A2-degeneration proof.
Only Python's standard library is required.
"""
from random import Random
P = 101

def trim(a):
    a = [int(x) % P for x in a]
    while len(a)>1 and a[-1]==0: a.pop()
    return a or [0]

def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]=(z[i+j]+x*y)%P
    return trim(z)

def scale(a,c):return trim([c*x for x in a])

def sub(a,b):return add(a,scale(b,-1))

def derivative(a):return trim([i*a[i] for i in range(1,len(a))])

def rem(a,b):
    a=trim(a); b=trim(b)
    assert b != [0]
    iv=pow(b[-1],-1,P)
    while a != [0] and len(a)>=len(b):
        n=len(a)-len(b)
        c=a[-1]*iv%P
        for i,x in enumerate(b):a[n+i]=(a[n+i]-c*x)%P
        a=trim(a)
    return a

def gcd(a,b):
    while b != [0]: a,b=b,rem(a,b)
    return a

def disc(coeff,base):
    perm=[base]+[i for i in range(3) if i!=base]
    C=[[[0] for _ in range(3)] for _ in range(3)]
    for ijk,c in coeff.items():
        e=[ijk[j] for j in perm]
        t,u,v=e
        z=C[v][u]
        if len(z)<=t: z += [0]*(t+1-len(z))
        z[t] = (z[t]+c)%P
    # Here C[v][u] holds the coefficient of t^i in the v^v u^u term.
    Q=[[0] for _ in range(5)]
    for i in range(3):
        for j in range(3):
            Q[i+j]=add(Q[i+j],mul(C[1][i],C[1][j]))
            Q[i+j]=sub(Q[i+j],scale(mul(C[2][i],C[0][j]),4))
    a,b,c,d,e=Q[::-1]
    I=add(sub(scale(mul(a,e),12),scale(mul(b,d),3)),mul(c,c))
    J=scale(mul(mul(a,c),e),72)
    J=add(J,scale(mul(mul(b,c),d),9))
    J=sub(J,scale(mul(a,mul(d,d)),27))
    J=sub(J,scale(mul(mul(b,b),e),27))
    J=sub(J,scale(mul(mul(c,c),c),2))
    return sub(scale(mul(mul(I,I),I),4),mul(J,J))

def profile(coeff):
    out=[]
    for i in range(3):
        D=disc(coeff,i)
        out.append((len(D)-1,len(gcd(D,derivative(D)))-1))
    return out

rng=Random(125)
coeff={(i,j,k):rng.randrange(1,35) for i in range(3) for j in range(3) for k in range(3)}
assert profile(coeff)==[(24,0),(24,0),(24,0)]
print('General section: each degree-24 discriminant squarefree mod 101.')
coeff[(0,0,0)]=coeff[(0,1,0)]=coeff[(0,0,1)]=0
coeff[(0,2,0)]=1
coeff[(0,1,1)]=-2
coeff[(0,0,2)]=1
coeff[(0,2,1)]=1
coeff[(0,1,2)]=0
coeff[(1,0,0)]=1
assert profile(coeff)==[(24,1),(24,0),(24,0)]
D=disc(coeff,0)
assert D[:2]==[0,0] and D[2]!=0
# At (0,0,0) the vertical equation begins (u-v)^2+u^2 v;
# the total equation has nonzero t coefficient, giving an A2 projection cusp.
assert all(coeff[k]==v for k,v in {
    (0,0,0):0,(0,1,0):0,(0,0,1):0,
    (0,2,0):1,(0,1,1):-2,(0,0,2):1,
    (0,2,1):1,(0,1,2):0,(1,0,0):1
}.items())
print('Cusp section: discriminant gcd degrees (1,0,0), with exact t^2 multiplicity at t=0.')
print('All coefficient witnesses verified using exact arithmetic modulo 101.')
