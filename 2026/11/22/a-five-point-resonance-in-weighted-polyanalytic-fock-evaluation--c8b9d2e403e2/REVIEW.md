# Self-review

## Correctness: PASS

The weighted kernel is a sum of two independently established positive reproducing kernels. The nonzero Gaussian factor reduces point orthogonality exactly to a two-root separation condition. For four sites, all eleven unlabeled edge-color classes have been checked by exact integer Gram determinants, and the six surviving geometries have positive-semidefinite rank-two realizations. The five-site upper bound and uniqueness are explicit classical planar two-distance facts, separately sourced. The formula and boundary cases \(\tau=0,1\) were individually checked, and the regular pentagon construction achieves five at \(\tau=3/5\).

## Originality: PASS (best-knowledge)

Fulsche–Hagger's published kernel formulas supply the analytic and true third-level components. Harborth–Piepmeyer and Nozaki–Shinohara supply the known geometric four/five-site constraints. The evaluated searches and comparisons in `AUDIT.json` did not find the positive two-level mixture's exact all-weight orthogonal-capacity classification. The closest indexed polyanalytic four-site result concerns the *full* order-three kernel, with a different Laguerre factor. The 1993 geometric chapter was accessible by abstract rather than full text; historical priority remains provisional and independent review is required before publication.

## Value: PASS

Orthogonal point evaluations give a sharp, coordinate-independent measure of perfect finite point-kernel separation. The theorem classifies that natural invariant across the entire nonnegative mixing parameter, showing an isolated rigid five-point resonance, three other four-point resonances, a three-point baseline, and loss of all orthogonality above the final threshold. It does not rely on arbitrary finite sampling radii and does not assert an infinite-dimensional tight-frame property.

## Verification and limitations

The standard-library `checker.py` passed exact determinant checks for all eleven graph classes and exhaustive graph-isomorphism coverage of all 64 edge colorings; numerical PSD and pentagon-distance diagnostics complement the analytic proof. No conclusion about arbitrary mixtures of Landau levels or perturbation stability is claimed. The five-point theorem rests on the cited classical classification, not the finite checker.

Self-review: passed. Independent audit: not yet performed.
