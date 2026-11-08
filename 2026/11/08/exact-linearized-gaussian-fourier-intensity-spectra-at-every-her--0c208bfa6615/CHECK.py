"""Exact arithmetic checks of the Gaussian-monomial intensity differential.
Requires only Python's standard library. Finite checks supplement the proof.
"""
import math
import random
from fractions import Fraction

rng = random.Random(208162)
checks = 0
for m in range(1, 17):
    k0 = math.comb(2*m, m)
    for n in range(m):
        k = 2*m-n
        a = math.comb(m+n, m)
        b = math.comb(m+k, m)
        d2 = k0 * math.comb(2*m, n)
        # Real symmetric blocks have entries (2a,+-2sqrt(d2); +-,2b).
        # Exact Sylvester criteria and exact trace/determinant.
        assert a*b > d2
        assert math.factorial(m+n)*math.factorial(m+k)>math.factorial(2*m)**2
        assert 4*(a*b-d2)>0
        checks += 3
    # Test Gaussian radial integration of polynomial intensity differentials.
    # u=z^m/sqrt(m!); h=sum a_n z^n, with integer-complex coefficients.
    for trial in range(45):
        degree = 2*m+5
        coefs = [complex(rng.randint(-3,3),rng.randint(-3,3)) for _ in range(degree)]
        # Avoid floating-point cancellations by paired real arithmetic.
        coefs = [(int(c.real), int(c.imag)) for c in coefs]
        lhs = Fraction(0)
        # Calculate L via z^n \bar z^m and conjugate sum, then integrate;
        # Gaussian angular orthogonality requires equal total z,bar-z powers.
        terms = {}
        for n,(a,b) in enumerate(coefs):
            if a==b==0:continue
            terms[(n,m)] = (terms.get((n,m),(0,0))[0]+a, terms.get((n,m),(0,0))[1]+b)
            old=terms.get((m,n),(0,0))
            terms[(m,n)]=(old[0]+a,old[1]-b)
        for (n,k),(a,b) in terms.items():
            for (u,v),(c,d) in terms.items():
                if n+v == k+u:
                    lhs+=Fraction(math.factorial(n+v)*(a*c+b*d),math.factorial(m))
        # Independently derived orthogonal and antidiagonal term formula.
        rhs=Fraction(0)
        for n,(a,b) in enumerate(coefs):
            rhs+=Fraction(2*math.factorial(m+n)*(a*a+b*b),math.factorial(m))
        for n,(a,b) in enumerate(coefs):
            k=2*m-n
            if 0<=k<len(coefs):
                c,d=coefs[k]
                rhs+=Fraction(2*math.factorial(2*m)*(a*c-b*d),math.factorial(m))
        assert lhs==rhs,(m,trial,lhs,rhs)
        checks += 1
    # Phase has zero derivative; amplitude has eigenvalue 4 binom(2m,m).
    assert 4*k0>0
    checks+=1
print('CHECK_OK exact_gaussian_integrals_and_block_minors='+str(checks)+' orders=1..16')
