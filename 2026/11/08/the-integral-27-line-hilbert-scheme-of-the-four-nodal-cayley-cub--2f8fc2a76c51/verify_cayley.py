#!/usr/bin/env python3
"""Exact arithmetic checks for the Cayley cubic line scheme.

No external packages are required. This verifies the displayed local maps,
Jacobian determinants, Grassmannian top Chern number, and finite-field examples.
The symbolic geometric classification and global flatness argument are in RESULT.md.
"""
from itertools import combinations, permutations, product
from math import prod

# Truncated integer algebra Z[u,v]/(u²,v²), basis (1,u,v,uv).
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def mul(a,b):
    return (a[0]*b[0], a[0]*b[1]+a[1]*b[0],
            a[0]*b[2]+a[2]*b[0],
            a[0]*b[3]+a[1]*b[2]+a[2]*b[1]+a[3]*b[0])
def smul(k,a): return tuple(k*x for x in a)
zero=(0,0,0,0); one=(1,0,0,0); u=(0,1,0,0); v=(0,0,1,0)
a=u; c=v; b=add(neg(u),smul(2,mul(u,v))); d=add(neg(v),smul(2,mul(u,v)))
edge_equations=[mul(a,b), add(add(a,b),add(add(mul(a,b),mul(a,d)),mul(b,c))),
                add(add(c,d),add(add(mul(a,d),mul(b,c)),mul(c,d))),mul(c,d)]
assert edge_equations == [zero]*4
print('EDGE_MODEL_OK: four equations vanish in Z[u,v]/(u²,v²), rank 4')

# Polynomial dictionary in variables S,T,a,b,c,d. Linear forms only.
N=6
def constant(n):return {(0,)*N:n} if n else {}
def variable(i):
    e=[0]*N;e[i]=1;return {tuple(e):1}
def padd(*args):
    out={}
    for P in args:
        for k,v in P.items():out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}
def pmul(A,B):
    out={}
    for x,a in A.items():
        for y,b in B.items():
            z=tuple(i+j for i,j in zip(x,y));out[z]=out.get(z,0)+a*b
    return {k:v for k,v in out.items() if v}
def pscale(n,A):return {k:n*v for k,v in A.items() if n*v}
def linear_form(v):return padd(*(pscale(c,variable(i)) for i,c in enumerate(v)))
# G has cubic four terms xyz+xyw+xzw+yzw.
def cubic(coords):
    return padd(*(pmul(pmul(coords[i],coords[j]),coords[k])
                  for i,j,k in combinations(range(4),3)))
def determinant(M):
    n=len(M);total=0
    for p in permutations(range(n)):
        sign=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        total+=sign*prod(M[i][p[i]] for i in range(n))
    return total

def vec(i):return [int(k==i) for k in range(4)]
def vecadd(A,B,k=1):return [a+k*b for a,b in zip(A,B)]
for ij in [(0,1),(0,2),(0,3)]:
    i,j=ij;k,l=[x for x in range(4) if x not in ij]
    U=vecadd(vec(i),vec(j),-1)
    V=vecadd(vec(k),vec(l),-1)
    A=vec(i);B=vec(k)
    coords=[]
    for h in range(4):
        sv=padd(pscale(U[h],variable(0)),pscale(V[h],variable(1)))
        av=padd(pscale(A[h],variable(2)),pscale(B[h],variable(3)))
        cv=padd(pscale(A[h],variable(4)),pscale(B[h],variable(5)))
        coords.append(padd(sv,pmul(variable(0),av),pmul(variable(1),cv)))
    G=cubic(coords)
    assert all(G.get((3-j,j,0,0,0,0),0)==0 for j in range(4)),ij
    # Four cubic coefficients in S,T; Jacobian in a,b,c,d.
    mat=[]
    for jcoef in range(4):
        row=[]
        for m in range(4):
            exp=[0]*6;exp[0]=3-jcoef;exp[1]=jcoef;exp[m+2]=1
            row.append(G.get(tuple(exp),0))
        mat.append(row)
    de=determinant(mat)
    assert abs(de)==1,(ij,mat,de)
    print('DIAGONAL_JACOBIAN_OK',ij,'det=',de)

# Top Chern number for Sym^3(S^*) over Gr(2,4): integrate by coefficient.
# Weights 3x,2x+y,x+2y,3y; integration [x^3 y^2](x-y)*c4.
def multiply2(A,B):
    out={}
    for (i,j),a in A.items():
        for (k,l),b in B.items():out[i+k,j+l]=out.get((i+k,j+l),0)+a*b
    return out
P={(0,0):1}
for W in ({(1,0):3},{(1,0):2,(0,1):1},{(1,0):1,(0,1):2},{(0,1):3},{(1,0):1,(0,1):-1}):
    P=multiply2(P,W)
assert P[(3,2)]==27,P[(3,2)]
print('CHERN_NUMBER_OK: integral c4 =',P[(3,2)])

# Enumerate every Gr(2,4)(F_p) point in its unique RREF basis.
def rref_lines(p):
    for i,j in combinations(range(4),2):
        pos=[(r,c) for r,pivot in enumerate((i,j))
             for c in range(pivot+1,4) if c not in (i,j)]
        for vals in product(range(p),repeat=len(pos)):
            M=[[0]*4 for _ in range(2)]
            M[0][i]=1;M[1][j]=1
            for (r,c),v in zip(pos,vals):M[r][c]=v
            yield M

def cubcoeff(M,p):
    # exact coefficients of F(S U+T V) mod p
    out=[0]*4
    for i,j,k in combinations(range(4),3):
        for choices in product((0,1),repeat=3):
            h=sum(choices)
            v=1
            for idx,t in zip((i,j,k),choices):v*=M[t][idx]
            out[h]+=v
    return [x%p for x in out]
for p in (2,3,5):
    lines=list(rref_lines(p));assert len(lines)==(p*p+1)*(p*p+p+1)
    got=[M for M in lines if cubcoeff(M,p)==[0]*4]
    assert len(got)==9,(p,len(got))
    print('FINITE_FIELD_EXHAUSTIVE_OK',p,'Grassmannian lines',len(lines),'Cayley lines',len(got))

print('ALL_CHECKS_PASSED')
