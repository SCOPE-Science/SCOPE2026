# Scientific review of matching-deletion stability

## Correctness
The specified real, equally weighted row-plus-column design has rank \(2n-1\) for all \(n\ge3\) and matching deletions \(0\le r\le n\). The Woodbury inverse yields the exact matrix in the result; the U, M and B sign sums prove the global \(\ell^\infty\) norm. The strict M gap is a positive sum of two squares, while the U/B gap is positive whenever U exists. Exact-rational independent Gram tests were performed for 22 small designs (466 observed cells). Remaining uncertainty lies in the usual human rechecking of the full universal algebraic classification; numerical tests alone cannot establish the infinite assertion.

## Originality
Searches compared the exact design and norm under names including two-way additive least squares, incidence-space projection, crown graph, matching deletion, maximum absolute hat-matrix row sum, and worst-case \(\ell^\infty\) amplification. Spielman--Srivastava (arXiv:0803.0929) supplies the general incidence projection, and Drineas--Mahoney (arXiv:1005.3097) identifies its leverage diagonal; neither inspected work gives the present complete exact row-sum formula, matched-deletion monotonicity and last-step ratio. Known results on additive product projections treat complete Cartesian-product sampling rather than matching-deleted sampling. Broader unindexed missing-data and statistical-design literature remains a publication-priority risk.

## Value
The natural two-way additive fit is a basic approximation operator for partially observed tables. Its exact uniform error amplification is not a diagonal leverage score. A full matching-deletion family supplies a nontrivial all-dimensional phenomenon: sequential deletion improves the worst-case observed-cell supremum norm and the very last deletion creates a quadratically larger improvement than each earlier step. The complete maximizing-cell classification and sharp positivity defect make the quantitative claim actionable as operator theory, not merely a routine low-dimensional matrix computation.

## Limits
The formula concerns equally weighted observed cells under one matching deletion pattern, with no extrapolation to missing cells or minimization over alternative projectors. The literature conclusion is qualified by the possibility of equivalent unindexed formulas; no independent verification is claimed.

Self-review: passed. Independent audit: not yet performed.
