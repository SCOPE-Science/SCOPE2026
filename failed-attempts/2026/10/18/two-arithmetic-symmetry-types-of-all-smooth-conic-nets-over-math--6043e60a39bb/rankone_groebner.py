"""Exact geometric double-line intersection certificates for two conic nets."""
import sympy as sp
u,v,w=sp.symbols('u v w')
representatives=[
 (1,0,0,4,3,3,0,1,0,3,1,0,0,0,1,1,0,0),
 (1,0,0,0,2,4,0,1,0,3,1,0,0,0,1,1,0,0),
]
for index,rep in enumerate(representatives):
    rows=[rep[k:k+6] for k in (0,6,12)]
    A,B,C,D,E,F=[u*rows[0][j]+v*rows[1][j]+w*rows[2][j] for j in range(6)]
    matrix=sp.Matrix([[2*A,D,E],[D,2*B,F],[E,F,2*C]])
    minors=[sp.expand(matrix.extract((a,b),(c,d)).det()) for a in range(3) for b in range(a+1,3)
            for c in range(3) for d in range(c+1,3)]
    first=list(sp.groebner([f.subs(u,1) for f in minors],v,w,order='lex',modulus=5))
    boundary=list(sp.groebner([f.subs({u:0,v:1}) for f in minors],w,order='lex',modulus=5))
    vertex=any(int(f.subs({u:0,v:0,w:1}))%5 for f in minors)
    print('class',index,'u=1 Groebner:',first)
    print('class',index,'u=0,v=1 ideal:',boundary,'u=v=0,w=1 not rank1:',vertex)
    assert boundary==[sp.Integer(1)] and vertex
    if index==0:
        assert first==[v+w**2-w+1,w**3-w**2+w+1]
        assert all((a**3-a**2+a+1)%5 for a in range(5))
    else: assert first==[sp.Integer(1)]
print('Geometric rank-one points: three for class 0 (degree-three closed point), zero for class 1.')
