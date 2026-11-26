# Independent mathematical audit

## correctness

PASS

Exact inversion gives rows (3/2,1/2), (-9/2,5/2); squaring gives rows (0,2), (-18,4). Multiplication by diag(9,1) cancels both off-diagonals of the symmetric part and gives the two stated pressure blocks. The first block attains the lower weighted Rayleigh bound on a least eigenvector of P; the second strictly dominates that bound. Accretivity then gives the inverse norm bound. For any universal diagonal weight let alpha decrease to zero with scalar P=Q=1. The limiting symmetric part has zero first diagonal and off-diagonal d_1-9d_2, so nonnegative determinant requires d_1=9d_2. For the angle, first use the similarity by W^(1/2) to make the original weighted numerical range Euclidean. Its symmetric part is positive definite, so the extremal imaginary-to-real ratios are the generalized Hermitian eigenvalues of the skew part multiplied by -i against the symmetric part. Spatial congruence by P^(-1/2) times an orthogonal eigenbasis of P^(-1/2) Q P^(-1/2) preserves those ratios, without asserting simultaneous similarity of P and Q. Each reduced two-stage block has symmetric diagonal h_1=(3/2) alpha, h_2=(5/2) alpha+4 beta mu and skew off-diagonal t=(3/2) alpha+6 beta mu. Its signed extremizers have stage components proportional to (sqrt(h_2), ±i sqrt(h_1)) and give ±t/sqrt(h_1 h_2). Squaring gives 3(r+4)^2/[r(5r+8)]; differentiation gives -96(r+1)(r+4)/[r^2(5r+8)^2], so mu_max is decisive. The limits are sqrt(3/5) and divergence like sqrt(6/r). The Euclidean symmetric two-stage compression along a common spatial direction has determinant -u^2/4-26uw-64w^2, strictly negative. The symbolic checks and finite matrix design in the supplied checker are consistent with these derivations. The supplied checker was inspected, not run.

## originality

PASS

Ali–Kirby already give exactly the two-term inverse pressure-Schur operator template; earlier augmented-Lagrangian work has the same architecture. Credit is confined to the universal diagonal-weight uniqueness and sharp attainable field-of-values sector for arbitrary SPD pairs. The relevant passages inspected do not supply those conclusions, and exact prior construction of the operator is not evidence for a new surrogate.

## value

PASS

The exact operator is a published solver surrogate, not an arbitrary matrix slice. A researcher studying its iterative solution can distinguish a guaranteed pressure-block coercivity norm from the indefinite Euclidean metric, and use the sharp sector to locate the loss of a coefficient-uniform narrow angle. Universality of the weight and attainment of the sector edges preserve that information for spatial operators that need not commute. This is useful geometry of the surrogate itself even without a claim about the entire block solver.

The dated certificate retains the supplied scientific assessment, sources and limitations.
