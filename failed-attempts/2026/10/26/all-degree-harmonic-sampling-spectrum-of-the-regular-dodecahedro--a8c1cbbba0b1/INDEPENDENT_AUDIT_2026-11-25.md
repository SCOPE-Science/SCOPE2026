# Independent mathematical audit

## correctness

PASS

On orthonormal vectors supported on antipodal pairs the parity-compatible matrix is twice the ten-axis kernel, and the opposite sector is zero. For the unsigned case, the matrix of the larger absolute angle has row sum 3 and obeys A_v^2=2I-A_v+J, so 3, 1 and -2 have multiplicities 1, 5 and 4 by the trace. For the signed case, B_u has eigenvalues 2 and -3 with multiplicities 6 and 4. The symmetric B_v obeys B_v^2=B_u+3I and commutes with B_u; it vanishes on the -3 space and has eigenvalues ±sqrt(5), each threefold by its zero trace, on the 2 space. These yield exactly the stated branch coefficients. Positivity also follows from the addition theorem, with E_l E_l*=(2l+1)G_l/20 for the specified evaluations. Independently reconstructed the exact angle matrices and their identities, and used the Rodrigues coefficient expansion, not the supplied recurrence, to exhaust degrees 0–185 with the stated eight rank deficiencies. The Laplace integral and sin(s)≥2s/pi on the half interval give |P_l(t)|≤sqrt(pi/[2l(1-t²)]); the maximum branch deviation is bounded by sqrt(pi/l)*(9/2+9/sqrt(8)), strictly less than one for l≥186 by the rational upper bound. Rank nine at 14 and rank ten from 15 onward therefore follow exactly.

## originality

FAIL

Two earlier exact findings cover the frozen claim. The 20-site finding 38363f24449f gives the very same unweighted Legendre Gram matrix, the same six parity branch formulas with the same multiplicities, the same complete ranks and final threshold 15, and an additional sharp all-degree interpolation bound. The earlier ten-axis finding 5142078e64c3 also gives all these branches after the antipodal factor of two and a known normalization change. These are direct statement-level comparisons to both prior findings, not judgments from catalogue similarity.

## value

FAIL

Exact-degree interpolation on a polyhedral vertex set is a worthwhile problem; in particular the last deficiency cannot be predicted just from the dimension. But both the spectra and threshold are already stated exactly for the same mathematical object; the twenty-site result additionally has a sharper scientific conclusion, an optimal uniform interpolation bound. The frozen finding isolates no independently useful new invariant or gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
