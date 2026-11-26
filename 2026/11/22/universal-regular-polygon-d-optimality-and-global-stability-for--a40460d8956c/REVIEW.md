# Independent mathematical audit

## correctness

PASS

For p=q^2 and R=rho^2, Katori–Shirai's theta quotient and Frobenius identity give the asserted product of angle-dependent ratios: the extra theta argument is -r*R^N, the diagonal argument is R, and conjugate factors pair into squared moduli. The kernel is strictly positive definite on distinct nodes, also seen by restricting the Laurent quadratic form to the first N nonnegative exponents and applying Vandermonde. In the theta logarithm differentiation, the product factors give the difference of L-periodizations of sin(t)/(cosh(x)-cos(t)) at shifts 0 and a. Its Fourier transform follows by Abel-expanding in exp(-j|x|) and using the sine coefficients of the differentiated periodic resolvent for -d^2/dt^2+xi^2; at zero frequency the value is 2(pi-t). Poisson summation thus cancels the zero mode and combines opposite frequencies to give exactly the factor 4pi/L in v'. Termwise differentiation is justified by exponential decay locally in 0<t<2pi. The curvature series has nonnegative terms and h=1 gives exactly c_{q,rho}>0. The estimate is strict on every nontrivial interval since h=1 already has cosh>1 off t=pi. All k-th arcs average 2pi*k/N; counting both directions of each unordered pair introduces a factor 1/2, so strong Jensen yields c_{q,rho}/4 times the squared arc deviations. A nonregular configuration has unequal first gaps and gives strict inequality. The regular Gram matrix has Fourier eigenvalues N*A_j by residue classes, with absolute convergence since p<R<1; dividing by the common diagonal A gives the stated normalized maximum. This holds for r>0 and N>=2 on the prescribed interior circle, with no claim of sharpness of the stability coefficient. The supplied numerical script and verification notes were inspected without executing the uploaded script.

## originality

PASS

The theta factorization, general cyclic Jensen step, and analogous disk Szegő optimum and stability are established. The supported distinct content is the annular equal-radius theta-ratio curvature estimate for every admissible q and rho, and its fixed-circle weighted determinant consequence. The closest inspected formulas and disk theorem do not supply that annular estimate. Equivalent Green-function literature remains an explicitly bounded priority risk.

## value

PASS

For exact D-optimal sampling on a prescribed annular circle, the result gives the unique geometry, exact determinant and a uniform positive loss estimate with explicit domain dependence for any perturbation, independent of the boundary weight. The annular curvature estimate is the substantive addition to a known disk method. The theorem makes no claim of multi-radius optimality or a best possible stability coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
