from fractions import Fraction
from math import comb

def catalan(n):
    return Fraction(comb(2*n,n),n+1)

# Catalan coefficient and ratio law, exact.
for n in range(0,30):
    A_n=catalan(n+1)
    A_np1=catalan(n+2)
    q=A_np1/A_n
    target=Fraction(4,1)-Fraction(6,n+3)
    assert q==target
    assert q < 4
    if n:
        prev=Fraction(4,1)-Fraction(6,n+2)
        assert q>prev
assert catalan(1)==1
assert catalan(2)==2

# Discrete positive relaxation spectrum: exact scalar moments on [0,tau].
tau=Fraction(5,1)
pts=[Fraction(1,2),Fraction(2,1),Fraction(5,1)]
wts=[Fraction(3,1),Fraction(4,1),Fraction(2,1)]
def moment(n):
    return sum(w*t**n for w,t in zip(wts,pts))

# Hausdorff finite differences.
for n in range(0,8):
    for r in range(0,7):
        h=sum((-1)**j*comb(r,j)*tau**(r-j)*moment(n+j) for j in range(r+1))
        assert h>=0

# Scalar Hankel quadratic forms on deterministic test vectors.
for m in range(0,5):
    for coeffs in ([Fraction(i+1,1) for i in range(m+1)],
                   [Fraction((-1)**i*(i+1),1) for i in range(m+1)]):
        h=sum(coeffs[i]*coeffs[j]*moment(i+j) for i in range(m+1) for j in range(m+1))
        hs=sum(coeffs[i]*coeffs[j]*(tau*moment(i+j)-moment(i+j+1)) for i in range(m+1) for j in range(m+1))
        assert h>=0 and hs>=0

# Adjacent ratios increase and remain below support edge when moments are nonzero.
qs=[moment(n+1)/moment(n) for n in range(25)]
assert all(qs[i+1]>=qs[i] for i in range(len(qs)-1))
assert all(q<=tau for q in qs)
print('VERIFY_OK')
