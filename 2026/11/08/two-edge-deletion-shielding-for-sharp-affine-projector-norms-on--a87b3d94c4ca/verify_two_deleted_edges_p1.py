"""Exact all-parameter P1 projection certificate for a two-edge-deleted clique.
Run: python verify_two_deleted_edges_p1.py (requires SymPy >=1.12).
"""
from sympy import symbols, factor, together, fraction, Poly, cancel, Rational, zeros, Matrix
from itertools import combinations
q = symbols('q', integer=True, positive=True)
h = q*q+4*q+5
alpha=(6*q**3+31*q*q+57*q+35)/(2*(q+1)*(q+2)*h)
beta=(q*q+3*q+5)/(2*(q+1)*(q+2)*h)
gamma=(2*q+5)/(2*(q+1)*h)
delta=1/h
D=2*(3*q*q+11*q+14)/((2*q+5)*h)
E=2*(q+1)/((2*q+5)*h)
def cross(u,v): return (u*u+v*v)/(2*(u+v))
Ld=2*cross(alpha,gamma)+2*cross(beta,gamma)+q*cross(alpha,delta)+q*cross(beta,delta)+q*(gamma+delta)+q*(q-1)*delta/2
Lf=4*delta+4*cross(D,delta)+2*(q-1)*(delta+E)+(q-1)*cross(D,E)+(q-1)*(q-2)*E/2
Lone=(12*(q+2)**2+4*(q+2)+1)/(3*(q+2)*(2*q+5))
Lfull=(12*(q+2)**2+15*(q+2)+5)/(3*(q+3)*(2*q+5))

def verify_positive(expr, expected):
    num,den=fraction(factor(expr))
    p=Poly(num,q); coeff=p.all_coeffs()
    assert coeff==expected,(coeff,expected)
    assert Poly(den,q).all_coeffs() and all(c>0 for c in Poly(den,q).all_coeffs())
    print('POSITIVE_POLYNOMIAL_CERTIFICATE_OK',p.degree(),len(coeff))
    return num,den

A=[8,168,1730,11306,51503,170927,422275,781907,1077903,1080307,747720,320610,64194]
B=[16,248,1704,6794,17235,28625,30765,20259,7185,975]
C=[4,80,727,3956,14340,36508,67142,90356,88715,61554,27360,5850]
verify_positive(Ld-Lf,A)
verify_positive(Lone-Ld,B)
verify_positive(Ld-Lfull,C)

# Check derived entries by exact inversion of 2*degree+adjacency.
for Q in range(1,8):
    n=Q+4
    edges=[(i,j) for i,j in combinations(range(n),2) if (i,j) not in ((0,1),(2,3))]
    degree=[sum(i in e for e in edges) for i in range(n)]
    G=Matrix(n,n,lambda i,j:(2*degree[i] if i==j else (1 if (min(i,j),max(i,j)) in edges else 0)))
    Minv=6*G.inv()
    vals={t:cancel(z.subs(q,Q)) for t,z in [('a',alpha),('b',beta),('c',gamma),('d',delta),('D',D),('E',E)]}
    expect0=[vals['a'],vals['b'],-vals['c'],-vals['c']]+[-vals['d']]*Q
    expect4=[-vals['d']]*4+[vals['D']]+[-vals['E']]*(Q-1)
    assert list(Minv.row(0))==expect0
    assert list(Minv.row(4))==expect4
print('INDEPENDENT_EXACT_GRAM_INVERSES_OK',7)
# Independently integrate all signed edge kernels for seven labelled graphs.
def absolute_linear_integral(u,v):
    if u*v>=0: return (abs(u)+abs(v))/2
    return (u*u+v*v)/(2*(abs(u)+abs(v)))
for Q in range(1,8):
    n=Q+4
    edges=[(i,j) for i,j in combinations(range(n),2) if (i,j) not in ((0,1),(2,3))]
    deg=[sum(i in e for e in edges) for i in range(n)]
    G=Matrix(n,n,lambda i,j:(2*deg[i] if i==j else (1 if (min(i,j),max(i,j)) in edges else 0)))
    Minv=6*G.inv()
    norms=[sum(absolute_linear_integral(Minv[k,i],Minv[k,j]) for i,j in edges) for k in range(n)]
    assert norms[:4]==[cancel(Ld.subs(q,Q))]*4
    assert norms[4:]==[cancel(Lf.subs(q,Q))]*Q
    assert max(norms)==norms[0] and all(v<norms[0] for v in norms[4:])
print('DIRECT_LABELLED_KERNEL_ABSOLUTE_INTEGRALS_OK',7)
from sympy import limit, oo
assert limit(q*(Ld-Lfull),q,oo)==Rational(1,6)
assert limit(q**3*(Lone-Ld),q,oo)==Rational(2,3)
print('SHARP_FIRST_AND_THIRD_ORDER_ASYMPTOTICS_OK')
print('ALL_TWO_DELETED_EDGE_SPLINE_PROJECTION_CHECKS_OK')
