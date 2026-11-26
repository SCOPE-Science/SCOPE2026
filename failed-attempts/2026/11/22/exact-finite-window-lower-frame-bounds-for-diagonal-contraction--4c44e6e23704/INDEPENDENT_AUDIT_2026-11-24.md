# Independent mathematical audit

## correctness

PASS

For ordered real rates and ordered time nodes, the exponential evaluation determinants never vanish by the Rolle-induction Chebyshev argument; their signs agree by the coalescent Vandermonde limit. Andréief's identity on the ordered simplex gives positive minors of K_T for all T>0. Gram positivity and the cofactor rule give the strict checkerboard inverse. For all-nonzero b, the Rayleigh quotient of the inverse frame matrix at Db is exactly s_T; a zero coordinate instead gives bound zero. For q_i=(R_T 1)_i/s_T, the difference diag(R_T 1)−R_T is a weighted graph Laplacian, hence positive semidefinite with kernel containing 1. Conjugation by diag(1/√q_i) shows the attaining inverse has largest eigenvalue s_T. Equality in the original Rayleigh quotient forces b_i²=q_i, and signs are a similarity. For small T the Taylor-coordinate Gram can be written as M diag(T^(k+1/2)) H_T diag(T^(k+1/2)) M^T where H_T→H, the positive Hilbert matrix, and M_{ik}=(−λ_i)^k/k!. In the inverse multiplied by T^(2n−1) only the (n−1,n−1) Hilbert-inverse corner survives. Lagrange leading coefficients give the β vector with factor (−1)^(n−1)(n−1)!; the reciprocal monic shifted-Legendre norm gives the remaining (2n−1) binom(2n−2,n−1)^2. The alternating β signs yield the two stated limits, and continuity of inversion at the positive Cauchy Gram gives the long-window result. For n=1 everything reduces to (1−e^(−2λ_1 T))/(2λ_1) and b=±1. Read but did not run the uploaded verifier; the all-horizon argument is analytical, not a numerical inference.

## originality

FAIL

The main all-horizon formula is a direct dense-uniform-sampling consequence of the distinct same-day discrete-orbit theorem f73c92c23f4a, not just an analogous formula. Its inverse-matrix proof implements the same checkerboard/Rayleigh/eigenvector reduction. Exact statement coverage is demonstrable without assigning within-day priority. The remaining long- and short-window statements are already covered by Chen–Belabbas and Trélat–Zuazua respectively; there is no supported distinct remainder in the frozen claim.

## value

FAIL

The continuous finite-window design is naturally motivated and the formula is useful, but the frozen standalone contribution adds no independent mathematical gap beyond the exact sampled-orbit design and the already established horizon limits: pass the Gram to its Riemann limit, apply the same signed-inverse scaling, and use the standard determinant sign for strictness. As an independent finding, a mechanically obtained invariant with no new threshold or optimization phenomenon does not meet the value criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
