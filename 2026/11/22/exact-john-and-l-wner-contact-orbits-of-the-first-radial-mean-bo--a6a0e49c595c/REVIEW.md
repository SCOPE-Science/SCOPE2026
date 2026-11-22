# Mathematical review: exact radial contacts of the three-cube

## Correctness

**PASS.** The first mean radial function is the normalized integral of the cube's product covariogram; the change of variables gives \(\rho=\sqrt{1+s^2+t^2}(6-2s-2t+st)/6\) on all unit directions. For its positive numerator \(H\), the only interior critical pair is \((2/3,2/3)\): the gradient difference factors as \((s-t)(D-S)\), with \(D-S>0\) inside, and the equal-coordinate equation factors as \((1-s)^2(3s-2)\). The four boundary edges have explicit one-variable derivatives, and the strict gap \(27-19652/729=31/729\) excludes body-diagonal minimizers. Thus all directions are covered analytically. Hyper-octahedral symmetry and uniqueness of John and Löwner ellipsoids show they are exactly the extreme radial balls. `verify.py` passed its exact rational and independent integral checks.

## Originality

**PASS, with historical-priority qualification.** Proposition 34 of Langharst–Manui–Zvavitch (arXiv:2601.20117v2) already contains the cube's radial integral and axial/diagonal evaluations; these are explicitly not claimed. The manuscript's Section 3.3 discusses ellipsoid-comparison lower bounds, not the sharp three-dimensional global angular optimizer. A separate general work on cube radial-mean gauge differentiability gives local regularity and exact representations but no sharp three-cube John orbit. The closest square result determines the planar contact-phase diagram, which does not imply the three-dimensional \(3:2:2\) orbit. The distinctive full-dimensional proof is a constrained two-variable extremization with a strict interior–boundary comparison. The original 1998 Gardner–Zhang work was bibliographically identified but its full text was not obtained; an unindexed equivalent calculation cannot be ruled out.

## Mathematical value

**PASS.** The John and Löwner ellipsoids are canonical affine-geometric invariants. Their sharp exact radii and contact sets for a fundamental test body quantify the anisotropy of the first radial-mean operator. The striking non-axis, non-diagonal orbit shows that looking only at high-symmetry directions misses the true extremum, albeit by a small strict amount. This makes the precise contact classification a useful benchmark for geometric tomography and ellipsoid bounds, rather than an arbitrary finite numerical slice. No general-dimension or all-parameter classification is asserted.

## Closest references and limits

- Langharst, Manui and Zvavitch, arXiv:2601.20117v2, Proposition 34: known full cube integral and special axial/diagonal radii; no complete three-dimensional global contact classification.
- Langharst, arXiv:2603.14134v5: general convexity of radial mean bodies; no Euclidean contact evaluation for the cube.
- Gardner and Zhang (1998): foundational definition/convexity; full primary text inaccessible in the current comparison.
- Published sharp differentiability-strata and planar-square contact results: local regularity and dimension-two contact geometry, not this three-dimensional orbit.

The source comparison cannot establish universal historical priority, and no independent mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
