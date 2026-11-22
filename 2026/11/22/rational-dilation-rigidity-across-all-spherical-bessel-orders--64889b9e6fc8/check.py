"""Supplementary finite algebra checks; proof is contained in RESULT.md."""
from sympy import I, Poly, Symbol, factorial, simplify, gcd, Rational
z = Symbol('z')
count = 0

def AB(n):
    c = [factorial(n+k)/(factorial(k)*factorial(n-k)*2**k) for k in range(n+1)]
    A = sum(c[k]*I**k*z**(n-k) for k in range(n+1))
    B = sum(c[k]*(-I)**k*z**(n-k) for k in range(n+1))
    return Poly(A,z,extension=I), Poly(B,z,extension=I)

for n in range(16):
    A, B= AB(n)
    assert A.degree()==n and B.degree()==n
    count += 2
    assert gcd(A,B).degree()==0
    count +=1
    assert A.LC()==1 and B.LC()==1
    count += 2
    assert A.eval(0) != 0 and B.eval(0) != 0
    count +=2
    if n>=1:
        assert A.nth(n-1)==I*n*(n+1)/2 and B.nth(n-1)==-I*n*(n+1)/2
        count+=2
    # Exact 1/z asymptotic of ratio B/A.
    if n>=1:
        assert simplify(B.nth(n-1)-A.nth(n-1))==-I*n*(n+1)
        count+=1

# For every tested pair and rational scale, the pole-degree and leading-
# coefficient necessary conditions exclude a rational-function identity.
# The proof handles every untested order and scale symbolically.
for n in range(12):
  for m in range(12):
    if n==m: continue
    for a in range(1,9):
      for b in range(1,9):
        assert not (a*n==b*m and a*a*n*(n+1)==b*b*m*(m+1))
        count+=1

# Direct rational identities for small data, as an independent spot check.
for n,m,a,b in [(1,2,2,1),(2,3,3,2),(0,3,2,3),(5,1,1,5),(3,3,1,1)]:
    A,B=AB(n); C,D=AB(m)
    q=Rational(a,b)
    left_num = (-1)**(n*a)*B.as_expr()**a
    left_den = A.as_expr()**a
    right_num = (-1)**(m*b)*D.as_expr().subs(z,q*z)**b
    right_den = C.as_expr().subs(z,q*z)**b
    identity=Poly(simplify(left_num*right_den-right_num*left_den),z,extension=I).is_zero
    assert identity == (n==m and a==b)
    count+=1
print('Supplementary exact algebra checks passed:',count)
