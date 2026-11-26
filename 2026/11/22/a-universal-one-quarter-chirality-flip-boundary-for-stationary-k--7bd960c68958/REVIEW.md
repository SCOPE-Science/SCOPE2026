# Independent mathematical audit

## correctness

PASS

The trapped stationary active position is a bounded exponential convolution, so the generator identities apply to the required angular monomials. The Fourier index q-p exactly compensates the positional monomial under rotations; the symmetric flip operator acts as 0 on the sign-even term and -2ell on the sign-odd one. The recursion has strictly positive determinant at every positive degree, and independent symbolic reconstruction through degree four reproduced the frozen rational identity and critical factorization (replay: independent_algebra.py in /workspace/branches/e35f2848-31a2-448f-9a63-69c8ba96e2f8/). As a separate algebraic cross-check on the boundary, set b_j=j+g+2ell, D_j=(j+g)b_j+W for j=1,3, L=H/(D_1^2 D_3). Integration of the six angular orderings with two positive and two negative charges gives S_22=2/(D_3 D_1) times [b_3 b_1 + {b_3 b_1(2+4g+2ell)-W(2b_3+2b_1+2+4g)}/(4L)]. Indeed the chronological Fourier resolvents use rates 3,2,1 and intermediate modes (1,2,1), (1,0,1), (1,0,-1) and their negatives. After subtracting 2(b_1/D_1)^2 the coefficient of W^2 over H is 3b_1-b_3-(1+2g)=4ell-1. Rotation gives projected second and fourth radial factors 1/2 and 3/8. The independent thermal Gaussian term contributes zero fourth cumulant. Positivity of H and C then makes the concave/linear/convex quadratic cases exhaustive, including the subcritical double root, critical B=0 and W=0. The quarter boundary governs the leading high-speed sign for ell not equal to 1/4; the finite-speed count also depends on g, as the formal three cases state. A zero does not imply Gaussianity.

## originality

PASS

The closest models in the checked primary sources each lack a decisive ingredient: the trap, a switching angular torque, or the fourth-order observable. Fixed-torque kurtosis and trapped telegraph-torque second-order calculations are credited. No checked source states or implies the exact trapped continuous-angle, symmetric-torque fourth-cumulant sign law.

## value

PASS

The theorem identifies a sharp, rotational-diffusion-independent high-speed boundary in a model with an independently changing torque sign, and classifies finite-speed reentrant positive kurtosis, tangency, and absence of a positive region. This is a complete sign diagram from a nontrivial fourth-order moment calculation; it is not a recomputation of known second-order observables. Invariance of the sign under independent translational diffusion gives an additional robust interpretation, without implying experimental detectability or classifying the complete density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
