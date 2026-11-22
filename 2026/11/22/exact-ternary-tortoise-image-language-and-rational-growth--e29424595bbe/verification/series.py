"""Independent integer arithmetic generating-function calculation of the target language."""
from itertools import product
from fractions import Fraction

def B(n):
    return 1 if n==0 else (1<<(n-1))+1

def A(n):
    # The nonempty-2 case is a free binary prefix, one separator, and
    # an arbitrary sequence of blocks (binary-image word, separator).
    # Compute the star factor H(z)=1/(1-z*B(z)).
    h=[1]
    for m in range(1,n+1):
        h.append(sum(B(j-1)*h[m-j] for j in range(1,m+1)))
    value=B(n)
    for j in range(0,n):
        value += (1<<j)*h[n-1-j]
    return value

known=[1,3,6,14,35,91,242,653,1780,4888,13496]
for n in range(len(known)):
    assert A(n)==known[n],(n,A(n),known[n])
    print(f'length={n}, rational_coefficient={A(n)}, test=PASS')
# Verify the polynomial identity Q(z) F(z)=P(z) directly in integers
# F(z)=(1-4z+2z^2+7z^3-6z^4-z^5)/((1-z)(1-2z)(1-4z+3z^2+z^3))
poly_num=[1,-4,2,7,-6,-1]
def multiply(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return r
Q=multiply(multiply([1,-1],[1,-2]),[1,-4,3,1])
# This polynomial identity is checked to order 40; coefficient formula itself is inductive.
f=[A(j) for j in range(41)]
for j in range(41):
    lhs=sum(Q[t]*f[j-t] for t in range(min(j,len(Q)-1)+1))
    assert lhs == (poly_num[j] if j < len(poly_num) else 0),(j,lhs)
print('integer rational-identity check passed through degree 40')
