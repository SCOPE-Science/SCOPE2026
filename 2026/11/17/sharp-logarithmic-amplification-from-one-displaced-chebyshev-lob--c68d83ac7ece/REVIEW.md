# Scientific review

## Correctness — PASS

The claim is reduced to the exact cardinal-basis identities (1)–(3). Their local angular scaling has a two-sided harmonic tail with the coefficient \(\frac2\pi|\sin(\pi u)||1-\tau/u|\); a uniform \(O(m^{-2}+n^{-1})\) error for intermediate indices makes the local \(O(1)\) remainder valid. The intact-grid logarithmic bound and the rank-one basis comparison exclude distant maximizers. Strict concavity of \(\sin(\pi v)+\tau\sin(\pi v)/v\) proves uniqueness and the critical-point formula. The result holds for any index sequence approaching a fixed interior proportion. A standard-library numerical checker passed 195 supplementary assertions. The proof, not those tests, supports the infinite claim.

## Originality — PASS, with priority limitations

The closest motivating source, Wu (arXiv:2606.23409), gives a worst-case logarithmic sufficient regime for mesh perturbations shrinking as \((n\log n)^{-1}\), and a two-node near-collision obstruction, but not the exact fixed-fraction *one-node* asymptotic. An inspected published single-erasure theorem has linear growth after deleting a sample and changing polynomial degree, not the asserted log coefficient with full interpolation degree. An inspected cyclic robust-interpolation certificate treats a different normed family. Searches for single-node displacement, aliases, sharp log coefficient, rank-one Lagrange updates, and dominant versions yielded no directly covering statement. Equivalent earlier interpolation-stability formulae are a remaining historical-priority risk; search absence is not a proof of novelty.

## Mathematical value — PASS

One miscalibrated sample at order of a complete angular cell is natural in stable polynomial interpolation, while existing worst-case perturbation bounds do not cover this regime. The finding establishes a sharp parameter-dependent quantitative invariant, shows a single finite defect can increase the logarithmic coefficient by a factor exceeding two, and identifies the unique limiting location of the maximally amplified data. It distinguishes a localized error from adverse globally distributed perturbations, without claiming a universal tolerance regime.

## Scope and limitations

Only one displaced bulk node, fixed \(0<\tau<1\), exact real samples, and ordinary sup-norm polynomial interpolation. No claim concerns multiple defects, endpoint defects, numerical rounding, or a uniform estimate near node collision. Full historical priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
