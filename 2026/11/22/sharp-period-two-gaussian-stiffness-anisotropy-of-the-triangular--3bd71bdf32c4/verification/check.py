"""Reproduce Gaussian two-coset shift energies and local stiffness comparisons.

Uses only Python's standard library. Finite truncations are numerical checks,
not substitutes for the infinite-product and monotonicity proof.
"""
from math import sqrt, exp, pi, fsum, isclose

S = sqrt(2.0 / sqrt(3.0))
A = sqrt(3.0) * S
B = S


def one_dim(length, alpha, shift=0.0, trunc=40):
    return fsum(exp(-alpha * (length * (j + 0.5) + shift)**2)
                for j in range(-trunc, trunc + 1))


def kappa_from_product(length, alpha, trunc=800):
    """Jacobi theta-4 logarithmic curvature from its product."""
    c = pi*pi/(alpha*length*length)
    return 8*pi*pi/(length*length)*fsum(
        exp(-(2*j-1)*c)/(1.0-exp(-(2*j-1)*c))**2
        for j in range(1,trunc+1) if (2*j-1)*c < 700
    )


def exact_hessian(alpha):
    z = one_dim(A,alpha)*one_dim(B,alpha)
    return (z*kappa_from_product(A,alpha), z*kappa_from_product(B,alpha))


def hessian_direct(alpha, trunc=40):
    da=fsum((4*alpha*alpha*(A*(j+0.5))**2-2*alpha)
             *exp(-alpha*(A*(j+0.5))**2)
             for j in range(-trunc,trunc+1))
    db=fsum((4*alpha*alpha*(B*(j+0.5))**2-2*alpha)
             *exp(-alpha*(B*(j+0.5))**2)
             for j in range(-trunc,trunc+1))
    return da*one_dim(B,alpha), db*one_dim(A,alpha)


def summed_cross_energy(alpha,va,vb,trunc=24):
    return fsum(exp(-alpha*((A*(j+0.5)+va)**2+(B*(k+0.5)+vb)**2))
                for j in range(-trunc,trunc+1)
                for k in range(-trunc,trunc+1))


def check():
    assertions=0
    # Area of the index-two sublattice equals two (density-one normalization).
    assert isclose(A*B,2.0,rel_tol=1e-14); assertions+=1
    assert isclose(A*A,3*B*B,rel_tol=1e-14); assertions+=1
    for alpha in [0.45,0.6,1.0,1.5,2.0,3.0,5.0,8.0,12.0,40.0]:
        l1,l2=exact_hessian(alpha)
        assert l1>3*l2>0, (alpha,l1,l2); assertions+=1
        d1,d2=hessian_direct(alpha)
        for observed,reference in [(d1,l1),(d2,l2)]:
            # Absolute error protects against cancellation in very soft modes.
            assert abs(observed-reference)<1e-9+2e-8*reference,(alpha,observed,reference)
            assertions+=1
    for alpha in [0.6,1.0,2.0,6.0]:
        for va,vb in [(0.0,0.0),(0.17*A,0.08*B),(-0.31*A,0.16*B)]:
            expected=one_dim(A,alpha,va)*one_dim(B,alpha,vb)
            observed=summed_cross_energy(alpha,va,vb)
            assert isclose(observed,expected,rel_tol=8e-13,abs_tol=8e-13)
            assertions+=1
    # Leading broad-Gaussian stiffness-ratio law.
    for alpha in [0.2,0.16,0.12]:
        strong,weak=exact_hessian(alpha)
        leading=(1.0/3)*exp((2*pi*pi)/(3*alpha*B*B))
        assert abs(strong/weak/leading-1.0)<0.01
        assertions+=1
    # Narrow-Gaussian ratio tends to its sharp bound 3 from above.
    ratios=[exact_hessian(alpha)[0]/exact_hessian(alpha)[1]
            for alpha in [10.,20.,40.,80.]]
    assert all(r>3 for r in ratios) and ratios==sorted(ratios,reverse=True)
    assert abs(ratios[-1]-3)<0.05
    assertions+=2
    print('PASS: %d numerical assertions; independent 2D sums, derivatives, and theta-product curvatures' % assertions)
    print('Sample eigenvalue ratios:',[(a,round(exact_hessian(a)[0]/exact_hessian(a)[1],9))
          for a in [0.5,1.,2.,5.,20.]])

if __name__ == '__main__':
    check()
