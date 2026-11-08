#!/usr/bin/env python3
"""Exact small-size checks for symmetric-determinant Gauss geometry in characteristic two."""
import itertools
import sympy as s

def rank2(A):
    a=[list(row) for row in A]
    rows=len(a); cols=len(a[0]); r=0
    for j in range(cols):
        pivot=next((i for i in range(r,rows) if a[i][j]),None)
        if pivot is None: continue
        a[pivot],a[r]=a[r],a[pivot]
        for i in range(rows):
            if i!=r and a[i][j]:
                for k in range(j,cols):a[i][k]^=a[r][k]
        r+=1
        if r==rows:break
    return r

def det2(A):
    n=len(A);out=0
    for p in itertools.permutations(range(n)):
        q=1
        for i in range(n):q&=A[i][p[i]]
        out^=q
    return out

for n in (3,4):
    names=list(itertools.combinations_with_replacement(range(n),2))
    syms=s.symbols('x0:'+str(len(names)))
    X=s.Matrix(n,n,lambda i,j:syms[names.index(tuple(sorted((i,j))))])
    D=s.Poly(s.expand(X.det(method='berkowitz')),*syms,modulus=2)
    d=[D.diff(x) for x in syms]
    assert all(d[k].as_expr()==0 for k,(i,j) in enumerate(names) if i!=j)
    points=0;sing=0;rank_three=0;images=set()
    for bits in itertools.product((0,1),repeat=len(names)):
        if not any(bits):continue
        A=[[bits[names.index(tuple(sorted((i,j))))] for j in range(n)] for i in range(n)]
        rank=rank2(A)
        gradients=[int(di.eval(dict(zip(syms,bits))))%2 for di in d]
        if det2(A)==0:
            points+=1
            is_sing=not any(gradients)
            assert is_sing==(rank<=n-2),(n,bits,rank)
            sing+=is_sing
            if rank==n-1:
                rank_three+=1
                images.add(tuple(gradients[names.index((i,i))] for i in range(n)))
    assert len(images)==2**n-1
    print(f'n={n}: checked {2**len(names)-1} projective F2 matrices; determinant points={points}; singular points={sing}; smooth rank-{n-1} points={rank_three}; Gauss image all {len(images)} points of P^{n-1}(F2)')

# On a nonzero (n-2)x(n-2) pivot chart, det reduces to unit*(uw+v^2).
u,v,w=s.symbols('u v w')
q=u*w+v*v
assert [s.Poly(q,u,v,w,modulus=2).diff(z).as_expr() for z in (u,v,w)]==[w,0,u]
print('Schur normal slice: det=uw+v^2, characteristic-two Tjurina ideal=(u,w,v^2), transverse length=2')
a,b,c,d,t=s.symbols('a b c d t')
g=s.Matrix([[a,b],[c,d]])
alt=s.Matrix([[0,t],[t,0]])
trans=s.expand(g.T*alt*g)
assert s.Poly(trans[0,0],a,b,c,d,t,modulus=2).as_expr()==0
assert s.Poly(trans[1,1],a,b,c,d,t,modulus=2).as_expr()==0
assert s.expand(trans[0,1]-(a*d+b*c)*t)==0
print('Kernel frame change: alternating normal line transforms by det(g), giving nilradical det(K) tensor O(-1)')
# Degree of rank<=2 symmetric 4x4 forms via P(Sym^2 Q*) over Gr(2,4).
x,y,z=s.symbols('x y z')
h4=s.series(1/((1-2*x*z)*(1-(x+y)*z)*(1-2*y*z)),z,0,5).removeO().expand().coeff(z,4)
deg=s.Poly(((x-y)*h4).expand(),x,y).coeff_monomial(x**3*y**2)
assert deg==10
print('Schubert integral: degree of rank<=2 symmetric 4x4 locus=10; doubled Jacobian cycle degree=20')
print('ALL_CHECKS_PASSED')
