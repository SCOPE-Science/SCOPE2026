# Independent mathematical audit

## correctness

PASS

Discrete Fourier aliasing gives exact positive covariance eigenvalues λ_j=n(r^j+r^(n-j))/(1-r^n); the inverse is the inverse-DFT of their reciprocals. The unique farthest even- or paired odd-N modes dominate as r→0, giving parity (-1)^d r^-floor(n/2) and the stated coefficients. As r→1 the diagonally dominant Neumann expansion produces -δ^3/[4(1-cos(2πd/n))]+O_n(δ^4) for every nonzero distance. Thus even d changes sign and n=4 is first; n=2,3 have strict negative off-diagonals by compound symmetry. For n=4 and n=5 the explicit q2 factorizations reduce to polynomials in u=r+1/r with exactly one root u>2; q1<0, so the exact graph claim follows. Independent numerical direct covariance inversion vs Fourier diagonalization at n=4,5,7,10 and 3 radii, and independent q2 root/sign checks at n=4,5, agreed. These finite checks corroborate analytic endpoint limits and uniqueness calculations, not replace them.

## originality

PASS

The classical Poisson kernel Fourier series and circulant diagonalization are prior, as is circular Matérn conditional-autoregression theory for a different spectral family. No read primary or Resultary record implies the every-even-distance sign reversal for THIS stationary Poisson covariance, the sharp four-site onset, or exact n=4,5 cycle-graph thresholds. Best-of-knowledge priority only.

## value

PASS

The first sample size at which Gaussian conditional independences emerge as a covariance-scale parameter changes is mathematically natural; exact sign switches distinguish inverse covariance from marginal correlation. The n=4,5 closed thresholds and uniform even-distance onset give a finite structural classification with direct graphical interpretation, rather than a mere Fourier transform identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
