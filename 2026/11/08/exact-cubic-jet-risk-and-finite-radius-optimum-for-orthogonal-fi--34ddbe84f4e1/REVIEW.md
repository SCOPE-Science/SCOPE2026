# Independent mathematical audit

## correctness

PASS

PASS: Antipodal central differences eliminate the arbitrary even term exactly and leave b·u+(h²/6)T[u³]. Orthogonally decompose T into trace t and harmonic trace-free H; the sphere fourth/sixth pairing contractions show E[UH(U³)]=0 and E[H(U³)²]=6||H||²/[d(d+2)(d+4)]. Frame columns are pointwise orthogonal, so ||Σu_a ψ(u_a)||²=Σψ(u_a)² even though columns are dependent. This yields mean w=b+h²t/[2(d+2)] and variance (d−k)||w||²/k+d h⁴||H||²/[6k(d+2)(d+4)], then the displayed risk quadratic in s=h². Its positive curvature W yields iff b·t<0 for k<d and exact optimizer/gap. Strong convexity follows Hessian lower bound (a−9/(4λ))I. The k=d zero-variance classification is H=0; k<d requires H=0 and w=0. Reconstructed moment contractions and checked exact rational radial example for d=3, k=1..3 across two rational orthogonal frames; package verify.py contains exact tensor and rational stencil tests. No assumption of independent frame columns is used.

## originality

PASS

PASS with careful credited special case: Oct26 published harmonic-cubic rigidity supplies the k=d,b=0 exact mean/variance and H=0 classification, not a general nonzero b, incomplete k-frame, or strictly positive optimal radius. Feng–Wang 2022/23 introduce precisely the Haar Stiefel central estimator, sphere moments, and general variance/bias BOUNDS rather than this exact cubic tensor resolved MSE and sign criterion. Different Oct13 forward-difference quadratic SGD risk and Nov2 two-step Haar coupling work use different objectives/estimators. Surviving claim is exact partial-frame risk geometry and finite-radius convex witness.

## value

PASS

PASS: Cubic truncation is the first nonlinear odd error in symmetric finite differences, and partial orthogonal frames are a natural query-budget regime. The exact trace/harmonic decomposition identifies which tensor contractions control variance and proves that a nonzero radius can improve MSE even with noiseless measurements. This is a meaningful finite-radius boundary theorem with a globally strongly convex witness, not a mere rephrasing of estimator bias bounds; the optimum is an oracle benchmark, not an automatic tuning algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
