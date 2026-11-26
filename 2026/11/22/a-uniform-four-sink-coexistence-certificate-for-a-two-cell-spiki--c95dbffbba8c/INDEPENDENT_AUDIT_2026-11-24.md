# Independent mathematical audit

## correctness

PASS

At T=1 the published Euler map gives exactly the displayed residual after subtracting (x,y). The changes of coordinate u=tanh(αx), v=tanh(αy) are continuous and strictly increasing for every α≥6. Positive exponential Taylor sums and the monotonicity of tanh and artanh give uniform endpoint bounds. The independent rational vertex-of-interval calculation in /workspace/review-evidence/replay.py 5 (output 5.txt) verifies all 36 prescribed strict face signs, with minimum certified margin 3/1000, and pairwise separation of the physical rectangles using enclosing intervals. Poincaré–Miranda gives interior zeros; no uniqueness or census is needed. For both possible orientations of a corner box, the two absolute Jacobian row sums are less than one, using the two thresholds 0.34 and 0.90 and monotonicity of αe^(−2αt). For mixed boxes, 1.7−3.89d_tiny>0, and det(I−J)≤1−(1.7−3.89·24/1999)·6(1−0.94²)<0; the eigenvalues are real and straddle 1. The positive determinant makes the smaller eigenvalue positive, so its modulus is less than 1. The inverse row norm in the central box is less than one, proving repulsion. Hyperbolic sinks have nonempty open basins, which cannot intersect since an orbit has at most one limit. The inequalities include α=6 and hold for the entire unbounded interval. The type counts are lower bounds and apply only to step T=1.

## originality

PASS

The supported distinct increment is a simultaneous rigorous lower certificate for nine hyperbolic equilibria, including four sinks, at every α≥6 for this exact published discrete map and Euler step. The original numerical examples and the continuous-time capacity/steepness results do not supply these quantifiers and stability conclusions. The same-day catalogue reflection is the assigned record, not separate priority evidence. This is a bounded comparison.

## value

PASS

An explicit uniform sufficient threshold establishes four open basins of attraction for a particular published discrete model, beyond the low-gain numerical examples and the bare possibility of high capacity. The robust coexistence regime and verified type composition are useful constraints on higher-gain bifurcation studies even without a full census or sharp threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
