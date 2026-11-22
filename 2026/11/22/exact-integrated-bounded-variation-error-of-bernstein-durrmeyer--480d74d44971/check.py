"""Exact independent checks for the Bernstein--Durrmeyer BV error theorem."""
from fractions import Fraction as F
from math import comb
from random import Random


def beta_piece(n, k, s):
    # Integrate a Bernstein basis polynomial by its monomial expansion.
    return comb(n, k) * sum(((-1)**j * comb(n-k, j) * s**(k+j+1) / F(k+j+1)) for j in range(n-k+1))


def error_direct(n, s):
    # Cross-mass integral for the symmetric Durrmeyer kernel.
    a = [beta_piece(n, k, s) for k in range(n+1)]
    return 2 * (n+1) * sum(v*(F(1,n+1)-v) for v in a)


def error_binomial(n, s):
    # Independent binomial representation of the jump error.
    m = n+1
    probs = [comb(m,j)*s**j*(1-s)**(m-j) for j in range(m+1)]
    return sum(abs(j-k)*probs[j]*probs[k] for j in range(m+1) for k in range(m+1))/m


def sharp(n):
    m=n+1
    return F(comb(2*m,m),4**m)


def poly(n,x,s):
    # The Durrmeyer image at x of the step H_s, evaluated independently.
    return sum(comb(n,k)*x**k*(1-x)**(n-k)*(F(1)-(n+1)*beta_piece(n,k,s)) for k in range(n+1))


def main():
    count=0
    for n in range(16):
        target=sharp(n)
        assert error_direct(n,F(1,2)) == target == error_binomial(n,F(1,2)),(n,target)
        for s in [F(0),F(1,11),F(1,4),F(2,5),F(1,2),F(3,5),F(3,4),F(10,11),F(1)]:
            assert error_direct(n,s)==error_binomial(n,s),(n,s)
            assert error_direct(n,s)<=target,(n,s)
            if s not in (F(0),F(1),F(1,2)):
                assert error_direct(n,s)<target
            count+=1
    # Exact Markov normalization and reflection, independent polynomial expansions.
    for n in range(13):
        for x in [F(1,7),F(2,7),F(4,7),F(6,7)]:
            for s in [F(1,5),F(1,2),F(4,5)]:
                a=poly(n,x,s)
                assert 0<=a<=1
                assert a+poly(n,1-x,1-s)==1,(n,x,s)
    # Numerical signed-jump stress tests, independent direct integration by midpoints.
    rng=Random(1201)
    for trial in range(30):
        n=rng.randrange(1,9)
        jumps=sorted((F(rng.randrange(1,99),100),F(rng.randrange(-7,8),8)) for _ in range(4))
        tv=sum(abs(c) for _,c in jumps)
        if tv==0:continue
        approx=0.
        mesh=500
        coefficients = [(float(c),[float(F(1)-(n+1)*beta_piece(n,k,s)) for k in range(n+1)],float(s)) for s,c in jumps]
        for j in range(mesh):
            x=(j+0.5)/mesh
            basis=[comb(n,k)*x**k*(1-x)**(n-k) for k in range(n+1)]
            d=sum(c*(sum(b*t for b,t in zip(basis,coeff))-int(x>s)) for c,coeff,s in coefficients)
            approx+=abs(d)/mesh
        assert approx <= float(sharp(n)*tv)+1e-4,(trial,approx,float(sharp(n)*tv))
    print('EXACT_NORMALIZATION_BINOMIAL_BETA_SHARP_TESTS_PASS',count)
    print('SYMMETRY_AND_SIGNED_JUMP_TESTS_PASS',30)
    print('ALL_BERNSTEIN_DURRMEYER_BV_TESTS_PASS')


if __name__=='__main__':
    main()
