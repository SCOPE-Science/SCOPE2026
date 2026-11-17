# Independent mathematical audit

## correctness

PASS

At A=diag(−1,0,1,2), w=cos εe2+sin εe4, u=−sin εe2+cos εe4 and W=[w,e3], A w=d w+b u with d=2sin² ε, b=sin 2ε; W*AW=diag(d,1). For the square Gaussian sketch G=Omega*W and h=Omega*u the reduced matrix is triangular with selected near-zero eigenvalue d+b(G−1h)_1. The nullspace of Gaussian [G,−h] is projective Haar, so G−1h has ratios of three independent standard circular complex Gaussians. The selected eigenvector z=−bZ2/((1−d)Z0−bZ1); (1−d)²+b²=1 makes the denominator independent standard Gaussian. Hence R=tX/(Y+tX), exact CDF x/(t+(1−t)x), F1/F2 moments, asymptotic mean 8ε²log(1/ε) and RMS 2ε. Independently integrated the exact moment density at t=0.16 to high precision. Claims concern specified branch and exact arithmetic only, not all selectors.

## originality

PASS

Shao studies the same square randomized Petrov–Galerkin/Rayleigh refinement with high-probability bounds, not the unconditional finite-angle CDF or sharp first and second moment scaling; oversampled sketched Ritz is different. A special-case exact law can provide a motivated, genuinely useful risk counterpoint.

## value

PASS

Unconditional risk is mathematically distinct from high-probability convergence guarantees for a widely relevant randomized eigensolver. A fully normalized exact finite-angle law and sharp logarithmic-mean versus linear-RMS penalties show what rare Gaussian sketches can do, on a simple but motivated interior-eigenvalue test. A small explicit model is sufficient because it isolates a genuine general-risk blind spot; no universal practical failure is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
