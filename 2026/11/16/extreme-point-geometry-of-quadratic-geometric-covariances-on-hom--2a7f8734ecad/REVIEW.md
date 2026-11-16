# Scientific review

## Correctness — PASS
The domain is the infinite \((q+1)\)-regular tree, with \(q\ge2\), \(0<r<q^{-1/2}\), and arbitrary real \(a,b\). The derivation of the bounded adjacency resolvent, its first two parameter derivatives, and the exact degree-two numerator establishes positivity on **every** finite vertex configuration by the spectral theorem. The diagonal-normalization and distance-one/two evaluations establish an affine bijection with normalized nonnegative quadratics. The zero-order classification of nonnegative quadratics proves every claimed extreme point; the nonatomic spectral law proves finite-site strictness. Independent symbolic derivative identities and rational endpoint/notch examples were rerun from `verify_tree_quadratic.py`. Finite Gram tests are corroborative only.

## Originality — PASS relative to inspected literature
Kashaeva's 2026 paper develops heat kernels and spectral resolution of free-product Cayley graphs, including the regular tree; its main theorems concern heat kernels and Laplacian spectra, not the positivity region of distance-polynomial geometric kernels. Vergara (2019) gives the full radial positive-definiteness characterization in measure/trace-class terms, but its analyzed concrete profile is parity-selective, not the present quadratic-exponential family. A publicly available 2026 first-order regular-tree classification explicitly covers the \(b=0\) slice and critical/supercritical decay, but does not classify the two-parameter cone's continuum of exposed double-notch points or its extra two-edge extreme. The Euclidean quadratic-exponential positivity result concerns the different Euclidean Fourier transform. These comparisons are implications, not title matches. Unindexed older tree covariance formulas and general truncated-moment extremal arguments remain priority risks.

## Mathematical value — PASS
This result is a full and sharp nontrivial two-parameter covariance-validity classification for all regular-tree branching degrees at subcritical decay. It also identifies the *entire* extreme-point geometry, including a movable interior spectral notch not present in the first-order family, and proves all spectral-boundary kernels remain finite-site strictly positive. The classification is applicable to selecting valid radial covariance weights on tree-structured data rather than checking finite Gram tables. It does not merely tabulate a small arbitrary parameter slice.

## Scope and limitations
No claim beyond \(r<q^{-1/2}\); no assertion about irregular or finite trees, or sharp finite-volume smallest eigenvalue asymptotics. The Kesten spectral law and general radial-kernel positivity theory are credited prior work. The originality review is bounded and cannot replace independent priority verification.

Self-review: passed. Independent audit: not yet performed.
