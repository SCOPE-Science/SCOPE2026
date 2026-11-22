# Scientific review

## Correctness

PASS. A unitary length-\(m\) Fourier transform across the repeated three-node cells reduces the complete \(N\times N\) Fourier sampling matrix to identical \(3\times3\) Vandermonde fibers. Its gauged Gram matrix has one antisymmetric eigenvector and a quadratic symmetric block. The eigenvalue ordering is proved from \(a>0\), \(a-b>0\), and \(a+b=2a\cos\theta\); this gives exactly one upper-eigenvalue crossing at \(\varepsilon=1/4\). Taylor expansion proves the collision coefficients uniformly in grid size. Direct full-matrix moment checks agree with the bands at 88 finite test instances, but the proof is analytic.

## Originality

PASS relative to the examined primary work and available mathematical records. Chen--Lin--Zhang (arXiv:2608.21960, inspected full text, introduction, Theorems 1.2/1.4 and concluding comparisons) establish general nonuniform Fourier matrix estimates, not the present exact repeated triple-fiber spectrum. Strohmer--Tanner (SIAM J. Numer. Anal. 44, 2006, full accessible article, reconstruction and conditioning sections) address periodic nonuniform sampling broadly without the precise three-band or quarter-threshold statement. Closest publicly indexed comparisons cover alternating two-point perturbations, two-point collisions, or different frequency supports. The standard polyphase technique itself is classical, and the residual possibility of an unindexed equivalent three-channel calculation remains.

## Mathematical value

PASS. The complete three-band calculation applies simultaneously to all grid sizes divisible by three, singles out the exact spectral crossing at the quarter-grid perturbation, and identifies a sharp second-order singular-value collapse with its universal coefficient. The quadratic triple-cluster instability differs structurally from single-pair coalescence and directly quantifies Fourier interpolation noise amplification.

## Scope and risks

The calculation is limited to a symmetric, equal-weight, three-periodic sampling configuration and consecutive Fourier frequencies. It is not an optimal design theorem over all perturbations. Earlier polyphase-filterbank treatments may contain equivalent algebra without using the present terminology.

Self-review: passed. Independent audit: not yet performed.
