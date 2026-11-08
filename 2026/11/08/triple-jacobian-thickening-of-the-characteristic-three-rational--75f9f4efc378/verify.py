#!/usr/bin/env python3
"""Exact finite-field identities for the singular scheme of a tangential quartic."""
from itertools import product

P = 3
N = 3  # polynomial variables in each identity
def const(n):
    return {} if n % P == 0 else {(0,)*N: n % P}
def var(i):
    a = [0]*N
    a[i] = 1
    return {tuple(a): 1}
def add(a,b):
    out = a.copy()
    for k,v in b.items():
        out[k] = (out.get(k,0)+v)%P
        if out[k]==0: del out[k]
    return out
def neg(a):
    return {k:(-v)%P for k,v in a.items() if v%P}
def sub(a,b):
    return add(a,neg(b))
def mul(a,b):
    out = {}
    for k,v in a.items():
        for j,w in b.items():
            z = tuple(k[i]+j[i] for i in range(N))
            out[z] = (out.get(z,0)+v*w)%P
            if out[z]==0: del out[z]
    return out
def power(a,n):
    out=const(1)
    while n:
        if n&1: out=mul(out,a)
        a=mul(a,a)
        n//=2
    return out
def equals(a,b,label):
    assert a==b, label + ': '+str(sub(a,b))
    print(label+': OK')
def rank_mod(rows):
    mat=[r[:] for r in rows]
    if not mat:return 0
    nr=len(mat);nc=len(mat[0]);r=0
    for c in range(nc):
        z=next((i for i in range(r,nr) if mat[i][c]),None)
        if z is None:continue
        mat[r],mat[z]=mat[z],mat[r]
        inv=pow(mat[r][c],-1,P)
        mat[r]=[(a*inv)%P for a in mat[r]]
        for i in range(nr):
            if i!=r and mat[i][c]:
                q=mat[i][c]
                mat[i]=[(a-q*b)%P for a,b in zip(mat[i],mat[r])]
        r+=1
        if r==nr:break
    return r

def monomials(n,d):
    if n==1:
        yield (d,)
        return
    for i in range(d+1):
        for j in monomials(n-1,d-i):
            yield (i,)+j

a,u,z=var(0),var(1),var(2)
# Tangents to [1:a:a^2:a^3:a^4] in characteristic three.
T=[const(1),add(a,u),sub(power(a,2),mul(a,u)),power(a,3),add(power(a,4),mul(u,power(a,3)))]
Q=sub(mul(T[0],T[4]),mul(T[1],T[3]))
C=add(add(power(T[2],3),mul(power(T[1],2),T[4])),mul(T[0],power(T[3],2)))
equals(Q,{},'tangent quadric')
equals(C,{},'tangent cubic')

# Affine chart X0 != 0: a=X1/X0, z=X2/X0-a^2, u=X3/X0-a^3.
x1=a; x2=add(power(a,2),z); x3=add(power(a,3),u);x4=mul(x1,x3)
C0=add(add(power(x2,3),mul(power(x1,2),x4)),power(x3,2))
equals(C0,add(power(z,3),power(u,2)),'chart X0 cusp equation')
# Affine chart X4 != 0: a=X3/X4, z=X2/X4-a^2, u=X1/X4-a^3.
x3b=a;x2b=add(power(a,2),z);x1b=add(power(a,3),u);x0b=mul(x1b,x3b)
C4=add(add(power(x2b,3),power(x1b,2)),mul(x0b,power(x3b,2)))
equals(C4,add(power(z,3),power(u,2)),'chart X4 cusp equation')
# On the Jacobian subscheme u=0,z^3=0, and X4/X0=a^4.
X2=add(power(a,2),z);X3=power(a,3);X4=power(a,4)
equals(sub(mul(X2,X4),power(X3,2)),mul(power(a,4),z),'transition of nilpotent coordinate')
# At X0=X4=0 the CI equations force X2=0 and X1*X3=0.
# The only two geometric points there have independent Jacobian gradients.
def gradients(x):
    x0,x1,x2,x3,x4=x
    return [x4,-x3,0,-x1,x0],[x3*x3,2*x1*x4,0,2*x0*x3,x1*x1]
for label,x in [('E1',[0,1,0,0,0]),('E3',[0,0,0,1,0])]:
    gq,gc=gradients(x)
    assert rank_mod([[j%3 for j in gq],[j%3 for j in gc]])==2
    print('smooth exceptional point '+label+': OK')
# Degree-two and degree-three source-rank checks for the parameterization.
for d,expected in [(2,14),(3,29)]:
    mm=list(monomials(5,d));polys=[];trms=set()
    for exps in mm:
        res=const(1)
        for i,e in enumerate(exps):res=mul(res,power(T[i],e))
        polys.append(res);trms.update(res)
    matrix=[[p.get(t,0) for p in polys] for t in sorted(trms)]
    actual=rank_mod(matrix)
    assert actual==expected,(d,actual,expected)
    print('degree '+str(d)+' parameter rank '+str(actual)+': OK')
# The split rank-three algebra over P1 has weights 0,-4,-8.
for m in (0,1,2,3,4,5):
    euler=sum(4*m-4*j+1 for j in range(3))
    assert euler==12*m-9
    global_sections=sum(max(4*m-4*j+1,0) for j in range(3))
    print('twist',m,'Euler',euler,'h0',global_sections)
print('VERIFY_OK')
