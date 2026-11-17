# Independent mathematical audit

## correctness

PASS

The right-node value-cardinal Hermite polynomial R_m(z)=z^m sum_{k=0}^{m−1} binom(m+k−1,k)(1−z)^k has degree 2m−1 and leading coefficient (−1)^{m−1}B_m; the left value cardinal has opposite leading coefficient. Under h=Y−X→0, uniform bounded jet errors give h^{2m−1}(P_m−f)(t)→(−1)^{m−1}B_m(ε_Y0−ε_X0)(t−X)^{2m−1}, since derivative-error terms are higher in h and f∈C^{2m} has uniformly bounded Hermite remainder. Thus |h|^{2m−1} E_m→B_m Z M_{2m−1}(X) uniformly. Integrate the iid knots via h=u/T^{1/(2m−1)}, use a bounded support in u from the deterministic scaled-error bound, and dominated convergence to get exact positive coefficient 2 B_m^{1/d}E[Z^{1/d}]∫ M_d(x)^{1/d} dx for tail T^{−1/d}, d=2m−1. Layer-cake yields E[E_m^p]<∞ iff p<1/d, including log divergence at boundary. Independent exact rational cardinal checks and m=1 numerical coefficient C1(Z=1)=0.79684325201043 corroborate pieces; they do not replace proof.

## originality

PASS

PASS best-of-knowledge with special-case caveat: generic two-node m=1 noise amplification is already a Lagrange/Vandermonde phenomenon, and published random Lagrange interpolation has collision/moment laws. For m≥2 confluent Hermite jets the exponent 1/(2m−1), exact global L2 coefficient for arbitrary bounded dependent jets (independent of knots), and complete moment threshold are not implied by reviewed Fourier-confluent singular-value bounds, Arnoldi stabilization, or Lagrange-only results. Gautschi's 1978 highly relevant inverse confluent-matrix paper was only available as abstract; authorized Oxford full text request explicitly failed due disconnected VPN, retained as risk, not automatic FAIL.

## value

PASS

PASS: Random near-colliding interpolation nodes cause a sharp, unavoidable heavy-tail error law for exact unregularized Hermite reconstruction. A precise L2 tail constant and all-order sharp integrability threshold are natural stability statistics, expose worsening ill-conditioning as derivative order grows, and are useful for identifying when noise moments cease to exist; more than a routine consequence of a single matrix inverse norm bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
