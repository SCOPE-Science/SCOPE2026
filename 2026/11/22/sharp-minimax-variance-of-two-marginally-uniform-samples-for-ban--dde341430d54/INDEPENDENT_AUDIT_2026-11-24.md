# Independent mathematical audit

## correctness

PASS

Uniform marginals make each normalized test function centered with second moment one. For the √2-normalized sine and cosine at frequency k, the average cross-covariance is c_k=E cos(2πk(Y−X)); therefore the worst-direction variance is at least (1+max c_k)/2 even for nonstationary couplings. The nonnegative squared geometric sum of length m+1 has expectation m+1+2 sum_{k=1}^m(m+1−k)c_k. Since the positive weights sum to m(m+1)/2, max c_k≥−1/m. With a uniform independent nonidentity root offset the discrete Fourier sum gives −1/m in every occupied frequency, so the cross-covariance quadratic form is −||f||²/m, proving isotropic attainment. An optimal law has every c_k≤−1/m; strict positivity of the Fejér weights forces equality for each k and almost-sure vanishing of the kernel. Its zeros are exactly the required nonidentity roots. These are necessary constraints, not an asserted classification of all nonstationary couplings. For a constant shift at m≥2 the first two moment identities give 2/m²−1=−1/m, requiring m=2. At m=1 the half-turn annihilates the band, and at m=2 the 1/3 and 2/3 shifts attain the value. The uploaded diagnostic was inspected, not run. An independent check of the exact without-replacement variance representation for selected zero-sum populations is reproducible with python3 /workspace/reviews/evidence/reproduce.py, output 5; the all-coupling theorem is analytic.

## originality

PASS

The rotated root-grid sampler and its variance are recoverable from exact periodic-grid integration and classical finite-population correction; do not credit these in isolation. The distinct, supported result is that no Borel coupling of the two Haar marginals can do better for the entire real finite band, with a necessary root-support and cosine-moment condition for every optimizer. Nearby studies of spherical function recovery, Bayesian quadrature, and randomized lattices do not imply this minimax/rigidity claim.

## value

PASS

The exact tradeoff is useful at a fixed two-evaluation budget where independent samples are the natural baseline. It shows that changing dependence alone reduces worst-direction variance, quantifies the saving as 1/m of that baseline, and proves that beyond bandwidth two a fixed shift cannot attain it. The universal restrictions on optimal displacements add structural content even when the saving is small. The finding does not claim comparable gains outside the band or for other weighting schemes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
