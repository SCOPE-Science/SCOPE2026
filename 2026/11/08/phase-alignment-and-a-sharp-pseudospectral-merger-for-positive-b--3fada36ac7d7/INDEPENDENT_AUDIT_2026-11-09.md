# Independent mathematical audit

## correctness

PASS

On the Bernoulli Koopman space, coordinate sign functions give a reducing bilateral shift, hence full unit-circle spectral support. Direct integral over U transfers the infinite-operator resolvent to sup_{|eta|=r}||(M-eta I)^-1||. Exact upper-bidiagonal inverse entries have unique nonzero path; |d_i-eta|>=|d_i-r| and row/column signs factor at real r, so entrywise majorization yields equality at eta=r for operator 2-norm. For m=2, the smaller singular value on [a,b] maximizes at midpoint, with eps*=(sqrt((b-a)^2+gamma^2)-gamma)/2; monotonicity outside spectral circles and strict < for open pseudospectrum give two components at equality and merger only for epsilon>eps*. Spectrum itself is union of diagonal circles. Proof does not rely on the numerical diagnostic.

## originality

PASS

PASS with priority caveat. Duru et al. arXiv:2610.24853 Corollary 3.8 bounds spectral connected components but not exact resolvent norm nor pseudospectral merge; Trefethen–Contedini–Embree (2001) gives prior bidiagonal inverse and finite/infinite pseudospectral theory, not explicitly this Koopman constant-fiber radial formula in inspected material. Both classical ingredients openly credited. A general theorem on bidiagonal pseudospectra may imply this special case and remains a concrete risk.

## value

PASS

Spectrally distinct Koopman circles become pseudospectrally connected for a sharp computable perturbation size; exact radial reduction and coupling-dependent threshold are natural quantitative stability invariants of a nonnormal ergodic composition operator, not only finite-matrix numerics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
