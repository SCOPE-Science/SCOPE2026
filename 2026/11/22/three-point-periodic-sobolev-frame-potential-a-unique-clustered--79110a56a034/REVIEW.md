# Scientific review

## Correctness
The reproducing kernel follows from the normalized periodic Green equation \(-K''=\delta_0-1\). Three unordered pair correlations reduce the exact Gram-squared trace to a symmetric quartic in positive gaps summing to one. The boundary has a strict lower obstruction, and the cubic derivative equations force two gaps equal. The remaining stationarity polynomial has only the equilateral and \((1/6,1/6,2/3)\) candidates; their rational values distinguish the unique global optimizer. Direct matrix diagonalization establishes the stated Gram spectrum. The standalone exact-arithmetic checker corroborates the algebra without being used as an exhaustive proof over real gaps.

## Originality
A check of classical frame-potential literature, finite-dimensional Parseval-frame geometry, RKHS sampling literature, relevant publicly indexed mathematical records, and previously established related trace-operator statements did not identify the same optimal three-site periodic Green-kernel frame potential or an implication from a stronger theorem. The general Benedetto--Fickus result permits arbitrary unit vectors and yields an orthogonal benchmark, not the constrained node-placement optimum. Bodmann--Haas use a different Gram feasible set. The closest literature and concrete comparisons are recorded in `AUDIT.json`. Historical indexing and inaccessible equivalents are residual risks; a negative search is not a uniqueness guarantee.

## Value
The squared Gram Frobenius norm is a canonical frame potential and measures aggregate squared sampling-vector correlation. The result gives the complete minimum for the smallest nontrivial three-site circular design, shows that equally spaced nodes are strictly suboptimal under this natural objective, and quantifies an exact factor-two reduction in the off-diagonal correlation energy. It distinguishes spectral-distribution design from worst-direction norm design, without claiming downstream reconstruction rates.

## Limits
Only three distinct, equally weighted sites in periodic mean-zero \(H^1\) are classified. No claim is made about other node counts or other criteria. No independent external mathematical validation has been completed.

Self-review: passed. Independent audit: not yet performed.
