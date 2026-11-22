# Review of sharp swapped-axis ellipse-gauge moduli

## Correctness — PASS
For any real \(a\ge b>0\), the claimed constant is \(K=(a^2+b^2)/(2ab)\). The two support functions determine every exposed portion of the convex hull of the two ellipses. The curved arcs have gauge one; the only nontrivial exposed faces are four common-tangent segments. Strict convexity of the squared ellipse norm on each half segment shows that each face has its sole maximal-gauge point at the midpoint, whose gauge equals \(K\). Every normalized weighted sum of two unit-ball points is in that convex hull. Tangent uniqueness and strict convexity force equal weights and the exact contact-point equality cases. Direct radial reading of the arcs and segments verifies the displayed full convexified norm. No finite sample is used to prove universal statements.

## Originality — PASS (qualified)
Unser (arXiv:2611.06212v1, first public 4 November 2026) supplies a general nonconvex/quasi-norm framework but not this exact sharp constant, convexified norm, or all equality pairs. Kwun et al. (DOI 10.1186/s13660-016-1115-z) take the quasi-triangle modulus as an input rather than compute it for the ellipse union. The indexed published-finding corpus result on four-weight octagonal conic-spline gauges gives a sharp polyhedral formula, while the equal-area two-ellipse convex-hull result computes area, not the radial gauge or modulus. Related earlier polyhedral minimum-of-two-norm findings involve different unit balls and do not imply a formula for these smooth ellipses. No decisive identical or stronger source was found from actual searches and the inspected relevant papers; absence of indexed coverage does not establish absolute uniqueness. The octagonal full manuscript could not be materially inspected and is an explicitly recorded residual risk.

## Mathematical value — PASS
The minimum of two smooth anisotropic quadratic norms is a canonical nonconvex but homogeneous gauge, where the sharp binary quasi-triangle factor measures how much its union-of-ellipses ball fails convexity. The result determines the entire two-parameter family, its exact convexification, and every extremizing pair, with a quantitatively sharp quadratic onset and large-anisotropy regime. The full curved-arc/common-tangent analysis provides geometric structure absent from an isolated computation; it is not a routine point-evaluation or a reparameterization of the known polyhedral family.

## Independent limitations
Only the real planar swapped-axis family is asserted. The exact contact-geometry argument is the proof; the Python checks are reproducibility diagnostics rather than exhaustive verification. Bibliographic risk from unindexed Minkowski-gauge literature and unavailable relevant full text remains. This review is not independent validation.

Self-review: passed. Independent audit: not yet performed.
