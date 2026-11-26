# Independent mathematical audit

## correctness

PASS

Normalize a nonzero trace-zero matrix by sign and scale so that a positive eigenvalue is 1 and the spectral norm is 1. If the total negative mass is m, then m >= 1. For 0 < p < 1 the negative side contributes at least m^p, with equality only for one negative eigenvalue, and equality in the full bound requires no other positive eigenvalues. For p > 1 and k negative eigenvalues it contributes at least k^(1-p)m^p >= (n-1)^(1-p); equality requires k=n-1 and equal negative eigenvalues. At p=1 the pth-norm power is 2m, with equality for one positive eigenvalue and any nonpositive remainder summing to -1, or the opposite sign. Thus the transition is between p<1 and p>1, with multiple possible ranks at p=1 and no rank change when n=2. Real trace pairing represents every hyperplane by a self-adjoint normal. An indefinite or singular normal admits a unit vector with zero quadratic form, hence an admissible rank-one projector of ratio 1. For a positive definite nonscalar normal, a minimum-eigenvector projector minus tI, t=lambda_min(A)/tr(A)<1/n, gives a larger ratio than trace zero for p>=1 because its spectral norm is 1-t and t/(1-t) is strictly increasing. For 0<p<1 the two extreme eigenvectors give a weighted difference of projectors with absolute eigenvalue ratio lambda_min(A)/lambda_max(A)<1, also strictly worse. A negative definite normal is handled by changing sign, and the full space has ratio 1. These arguments verify both real ambient-space cases and the codimension convention for all dimensions and exponents; the supplied unexecuted numerical diagnostic is not needed for the proof.

## originality

PASS

The searched full-matrix width theorems address a different domain and do not supply the exact self-adjoint result. The closest exact record reproduces the value on the traceless symmetric five-plane for n=3 and 0<p<=1, not the self-adjoint codimension-one optimum, its uniqueness, the p>1 formula, or the rank transition. Credit that partial overlap without inferring priority from the shared publication date.

## value

PASS

The one-measurement problem is the first Gelfand index at which real self-adjointness can improve the uniform ratio; it cannot improve the corresponding full-matrix index. Strict identification of the trace as the only optimal measurement up to rescaling, together with the change from concentrated to spread-out extremal spectra, gives a usable sharp norm geometry not provided by the isolated n=3 witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
