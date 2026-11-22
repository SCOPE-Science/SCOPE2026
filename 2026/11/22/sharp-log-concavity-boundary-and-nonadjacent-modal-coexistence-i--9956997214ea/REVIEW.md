# Scientific review: sharp mass-shape boundary in generalized Poisson–Lindley counts

## Correctness — PASS

The claim is reconstructed from the normalized Poisson–generalized Lindley mass law with \(\alpha>1\), \(t>0\), and full infinite nonnegative support. An exact positive-neighbor ratio yields a strictly concave quadratic that controls mass increases, and a separate monic quadratic controls the change of neighboring ratios. The sign of the latter at zero, together with its vertex, proves the stated necessary-and-sufficient log-concavity threshold for *all* integers. In the explicit case \(\alpha=5/3\), an exact cubic determines the nonadjacent global-modal tie. Rational endpoint signs, the quadratic's global shape and strict cubic monotonicity exclude every unexamined tail index. `VERIFY.py` passed 14,212 exact-rational diagnostics. Their finite range is not substituted for the analytical proofs.

## Originality — PASS, with historical risk

The 2023 source states unconditional log-concavity and unimodality rather than a restricted parameter region or nonadjacent global modes. The 2022 and 2024 works give equivalent/reused probability-generating or mass formulas but not the sharp curvature threshold or the global-modal switch. The 2025 comparative paper explicitly identifies the earlier (2010) model under a shape shift; this equivalence is acknowledged rather than treated as novel. Searches on semantic aliases, shifted parameters, modal coexistence and nearby Poisson-mixture results found no covering published theorem. Full text of the 2010 primary source was not retrievable through the available institutional channel, leaving historical-priority risk; its model formula is recoverable in the inspected 2022 and 2025 papers. Search silence is not proof of priority.

## Value — PASS

A published statistical analysis relies on a blanket mass log-concavity/unimodality assertion. The exact phase boundary specifies precisely where log-concavity can and cannot be relied on, while the nonadjacent equal-global-mode example shows a stronger structural failure, not a numerical anomaly. A sharp switch between counts \(2\) and \(0\) affects modal prediction and interpretations of count distributions. The result does not infer a nonmonotone hazard rate solely from failure of log-concavity and does not claim novelty for the family itself.

## Closest literature and limitations

The most relevant sources are Atikankul (2023; original mass expression and shape assertion), Mahmoudi–Zakerzadeh (2010; equivalent earlier family), Papageorgiou–Vardaki (2022; accessible explicit equivalent generating function), Irshad et al. (2024; later use of the same marginal), and Lawal (2025; explicit reparameterization). No proof of arbitrary hazard shape or generalized-regression properties is supplied. The original 2010 full text is an access-limited residual priority check. This is a mathematical self-contained proof, not an independent certification.

Self-review: passed. Independent audit: not yet performed.
