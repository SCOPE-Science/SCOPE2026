# Self-review

## Correctness — PASS

The central-section parametrization gives an exact ellipse-arc-plus-chord perimeter. The integral triangle inequality reduces its global optimization to a one-variable function with no interior minima, proving all equality cases. Direct Taylor expansions establish both local endpoint thresholds, and an explicit missing-arc integral gives the cap-contact \(3/2\) coefficient. A Python-standard-library checker performs 1344 numerical assertions, including polygonal boundary lengths calculated without the elliptic-integral formula. Numerical checks supplement rather than certify the analytic proof.

## Originality — PASS (provisional historical assessment)

The most relevant archival reference checked in material detail is Finch (arXiv:1212.5946, December 24, 2012), whose cylinder discussion concerns surface area, mean width, and the perpendicular elliptical perimeter of oblique cylinders. That does not imply the optimum over central plane sections of finite right cylinders. Dirksen (arXiv:1602.07854v1), inspected in full, supplies the sharp centered-cylinder **area** section formula and area maximum (Lemma 2.1, Theorem 3), but neither a perimeter extremum nor its equality and regularity classification. Published random-cylinder work instead studies affine cap incidence; a separate least-perimeter theorem concerns central sections of a **cuboctahedron**, not a cylinder. These full-text and claim-level comparisons distinguish the new functional and exact object. These do not dominate the present section-perimeter/equality/endpoint classification. Searches for alternative wordings and dominating results found no exact match, but an unlocated elementary or classical source remains a genuine priority risk. No external independent assessment is claimed.

## Value — PASS

This is a natural complete global minimization problem in finite-cylinder stereometry. Its two different sharp aspect-ratio transitions distinguish global optimality from local angular stability. The explicit nonanalytic onset at end-cap contact explains the geometry responsible for the change of boundary type. The claim does not rely on a contrived numerical slice or unsupported prospective applications.

## Limits

Only centered finite right circular cylinders; no general classification of interior stationary points, oblique cylinders, noncentral sections, or experimental robustness.

Self-review: passed. Independent audit: not yet performed.
