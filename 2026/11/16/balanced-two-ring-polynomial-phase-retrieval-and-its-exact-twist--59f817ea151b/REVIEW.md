# Scientific assessment

## Correctness — PASS

For every integer \(K\ge1\), the discrete Fourier transform on a \(2K\)-point angular grid recovers all modes below the top harmonic and folds only the positive and negative \(K\)-th harmonics into one real bin. Two nonresonantly rotated grids provide two independent real equations for the common, radius-normalized top coefficient. Modulus equality on two distinct full circles makes the rational quotient invariant under a nonunit positive dilation and hence constant. Exact ambiguity pairs demonstrate necessity in both failed geometries. The extreme-bin matrix has singular-value squares \(1\pm|\cos(K\delta)|\). Each step was reconstructed algebraically; the bundled `verify.py` checks \(432\) Hermitian interpolation instances independently of the rank-one proof and tests finite failure cases. No finite experiment is taken as proof of the universal theorem.

## Originality — PASS, historical priority provisional

The focal 2017 Pohl–Li–Boche presentation proves the known \(4K\)-evaluation count with an *unbalanced* \(2K+1\) plus \(2K-1\) allocation. Bodmann–Hammen (2013) uses intersecting circles and shared nodes, Philipp (2014) uses derivative measurements, and Chalendar–Partington (2024) treats continuous-circle modulus uniqueness. Their statements do not supply the necessary-and-sufficient twist criterion for two balanced \(2K\)-grids or the sharp Nyquist interpolation condition number. The proof deliberately credits the general two-circle uniqueness mechanism; an equivalent balanced-grid calculation under other Fourier/Vandermonde terminology is a residual bibliographic risk.

## Mathematical value — PASS

Balanced equiangular acquisition is a geometrically constrained phaseless-design question left open by the asymmetric \(4K\)-evaluation construction. The exact resonant rotations distinguish failing arrangements from all successful twists at the same radii and same number of observations; the singular-value law singles out optimal Nyquist angular staggering. This characterizes a natural measurement architecture rather than a random coefficient slice or a mere recomputation of the general \(4K\) count. It does not promise global nonlinear numerical stability.

Self-review: passed. Independent audit: not yet performed.
