# Self-review

## Correctness — PASS

The two linear-center first integrals give the opposite intersection height \(2h_i-y\); entry direction gives the continuous folds \(g_i=h_i+s_i|y-h_i|\). Substituting the affine reset twice yields \(Q(u)=H+\sigma||u|+t|\) exactly. For a one-Lipschitz real map, \(Q(u)-u\) is nonincreasing: its two tail limits prove that a fixed point exists exactly for \(\Delta\le0\). Without a fixed point, the iterates diverge monotonically and eventually translate by \(\sigma\Delta\). With a fixed point, distances to it shrink monotonically. The omega limit is a one- or two-cycle, and finite-piece unit slopes force actual finite-time entry rather than mere asymptotic approach. The invariant-probability statements follow from recurrence. The standalone rational checker passed 7,000 exact composition cases and the indicated examples. None of the finite checks is used as a proof of the infinite theorem.

## Originality — PASS subject to priority risk

The closely related 2024 paper [1] contains the four-branch return map and a theorem ruling out **regular** limit cycles for unit-slope affine resets, but its inspected full-text portions do not give the all-initial-point finite-capture/ballistic dichotomy, critical scalar criterion or escape speed. Lawrence–Spingarn [3] concerns general nonexpansive piecewise isometries and an averaged fixed-point iteration; it does not state a sharp hybrid parameter boundary. Li–Liu [2] studies related impact hybrid systems but its complete text was inaccessible; no whole-paper noncoverage is asserted. Explicit indexed comparisons, including alternative forms of the double-fold map and wider nonexpansive-map statements, found no decisive equivalent or stronger published result. The general nonexpansive argument is standard; the claimed specific contribution is the exact hybrid classification, not discovery of nonexpansiveness.

## Mathematical value — PASS

The endpoint \(|a|=1\) is explicitly excluded from the regular-cycle theorem's hyperbolic conclusions. Its behavior could plausibly include nontrivial neutral dynamics. The result resolves the entire boundary for the natural return convention: every initial condition has finite transient to a period-at-most-two orbit or eventually constant escape velocity, and \(\Delta=0\) is a sharp, explicit separating hypersurface in parameters. An open interval of primitive two-cycles shows the period-two clause is substantive. The exact parameter test and absence of bounded nonperiodic return orbits are stronger than a generic fixed-point or low-entropy observation.

## Closest literature and risks

[1] Llibre–Santana, arXiv:2407.05151, Sections 2 and 4–7 (return formulas, affine regular-cycle restriction, quadratic-reset chaos). [2] Li–Liu, DOI 10.1016/j.cnsns.2022.107074 (bibliography and accessible abstract only, full text unavailable). [3] Lawrence–Spingarn (1987), DOI 10.1112/plms/s3-55.3.605 (accessible abstract only). [4] Nogueira–Pires–Rosales (2014), strict contractions, not unit-slope folds. Residual risk: historical equivalent in older hybrid-impact papers, and differences between physical-time hybrid solutions and section-return iterates. No claim of independently audited priority.

Self-review: passed. Independent audit: not yet performed.
