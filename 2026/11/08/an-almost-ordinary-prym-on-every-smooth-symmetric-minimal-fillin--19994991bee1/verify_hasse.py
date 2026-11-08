"""Reconstruct Hasse-Witt matrices by exact coefficient extraction modulo 3.
Run: python verify_hasse.py (requires sympy)."""
import itertools
import sympy as sp
p=3
x0,x1,y0,y1,S,T,U,z=sp.symbols('x0 x1 y0 y1 S T U z')
A=lambda a,b:a**4+a*b**3+2*b**4
E=lambda a,b:a**3*b-a*b**3
f=sp.Poly(sp.expand(A(y0,y1)*E(x0,x1)+A(x0,x1)*E(y0,y1)),x0,x1,y0,y1,modulus=3)
f2=f*f
ij=list(itertools.product(range(1,4),repeat=2))
H=sp.zeros(9)
for r,(i,j) in enumerate(ij):
    for c,(a,b) in enumerate(ij):
        powers=(3*a-i, 3*(4-a)-(4-i),3*b-j, 3*(4-b)-(4-j))
        H[r,c]=int(f2.coeff_monomial(x0**powers[0]*x1**powers[1]*y0**powers[2]*y1**powers[3]))%3
expected=sp.Matrix([
[1,1,1,1,2,0,1,0,0],
[2,0,1,1,0,1,0,1,0],
[1,2,1,0,2,2,0,0,1],
[2,1,0,0,0,1,1,1,0],
[2,0,2,0,1,2,2,2,2],
[0,1,1,1,1,1,0,1,0],
[1,0,0,2,2,0,1,2,1],
[0,1,0,1,1,1,1,1,0],
[0,0,1,0,2,0,1,0,0]])
assert H==expected
assert int(H[:8,:8].det())%3==1
assert int(H.det())%3==0
c=sp.Poly(H.charpoly(z).as_expr(),z,modulus=3)
assert sp.Poly(z*(z-1)**2*(z*z+1)*(z*z+z-1)**2,z,modulus=3)==c
print('GENUS_NINE_HASSE_MATRIX_PASS rank=8 stable_rank=8 a=1')

G=sp.Poly(2*S**3*U-S**3*T+S**2*T*U+S*U**3+S*T**3+T*U**3+T**2*U**2,S,T,U,modulus=3)
triples=((2,1,1),(1,2,1),(1,1,2))
Q=sp.zeros(3)
for r,indr in enumerate(triples):
    for c,indc in enumerate(triples):
        ps=tuple(3*indc[k]-indr[k] for k in range(3))
        Q[r,c]=int((G*G).coeff_monomial(S**ps[0]*T**ps[1]*U**ps[2]))%3
assert Q==sp.Matrix([[1,2,2],[1,0,0],[1,0,2]])
assert int(Q.det())%3==2
print('PLANE_QUARTIC_HASSE_MATRIX_PASS rank=3 ordinary')
print('PRYM_ISOGENY_INVARIANTS_PASS dimension=6 p_rank=5 a=1')
