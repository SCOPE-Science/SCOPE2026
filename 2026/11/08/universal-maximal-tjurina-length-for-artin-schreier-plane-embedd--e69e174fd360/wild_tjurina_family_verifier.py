"""Exact characteristic-p checks of universal Tjurina lengths.

The proof in the accompanying result is unrestricted; these are finite
independent Groebner-basis computations for various primes, exponents and
nonmonomial coefficients. Requires SymPy.
"""
import sympy as sp
x, z = sp.symbols('x z')
examples = [
    (2, 4, [1, 1, 0, 1]),
    (2, 8, [1, 1, 0, 1, 1, 1]),
    (3, 3, [1, 2, 1]),
    (3, 9, [1, 1, 2, 1, 1]),
    (5, 5, [2, 3, 1]),
    (5, 5, [0, 1, 0, 1]),
]
for p,q,coeffs in examples:
    m=len(coeffs)-1
    d=p*m
    assert q < d and coeffs[-1] % p
    G=sum((coeffs[j] % p) * x**(p*j)*z**(p*(m-j)) for j in range(m+1))
    f=z**(d-q)-G-x*z**(d-1)
    derivatives=[sp.Poly(sp.diff(f,v),x,z,modulus=p) for v in (x,z)]
    assert derivatives[0]==sp.Poly(-z**(d-1),x,z,modulus=p)
    assert derivatives[1]==sp.Poly(x*z**(d-2),x,z,modulus=p)
    J=sp.groebner([f,sp.diff(f,x),sp.diff(f,z)],x,z,order='lex',domain=sp.GF(p))
    leading=[h.LM(order='lex').exponents for h in J.polys]
    bx=min(i for i,j in leading if j==0)
    bz=min(j for i,j in leading if i==0)
    length=sum(1 for i in range(bx) for j in range(bz)
               if all(i<a or j<b for a,b in leading))
    assert length==(d-1)**2, (p,q,m,length,d,leading)
    print(f'char={p} q={q:<2} deg_g={m} plane_degree={d:<2} tau={length:<4} CHECKED')
print('ALL_EXACT_TJURINA_CHECKS_PASS')
