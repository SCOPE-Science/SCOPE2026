# Scientific review

## Correctness — PASS

The theorem is a consequence of the documented cumulative small-label recurrence. The polynomial comparison function is obtained by a formal generating-function solution. The exact removal of nested floors converts the integer count to a single floor with a weighted error term. A universal rowwise error bound and a separate estimate on the last logarithmically many diagonals give a vanishing correction at the critical fixed-row scale. Threshold asymptotics and the nonintegral staircase then follow. The attached executable independently checks the recurrence against actual sorted-label firing for small graphs and verifies the algebraic identities using rational arithmetic. Risks: the fixed-coordinate restriction is essential; finite checks alone would not prove uniformity.

## Originality — PASS (historical priority provisional)

The direct precursor, OEIS A397913, provides the exact floor recurrence and initial table, not a fixed-row scaling theorem. The fully inspected ordered-directed-graph paper (arXiv:2611.25137v1) rigorously proves the recurrence's reachability meaning and treats the exact boundary row and the first adjacent row, but does not obtain the all-fixed-row asymptotic or limiting nonintegral staircase. Directed-tree reachability and unlabeled lattice-firing results have different quantified objects. Searches of related mathematical records, published material and accessible historical claims did not locate equivalent higher-row results. This is not a proof of historical uniqueness, and unindexed work and the partly inaccessible OEIS full page remain priority risks.

## Value — PASS

The least-chip boundary is a natural invariant in labeled directed chip-firing, and the existing exact recurrence by itself conceals the growth regimes as a coordinate tends to infinity. The theorem gives an explicit polynomial correction to an exponential scale for every fixed row, a quantitative relative error, the sharp first-order ratio between adjacent rows, and a whole nonintegral threshold staircase. These quantify path merger effects and extend known one-row asymptotics to a complete infinite hierarchy, rather than producing a single additional table entry.

Self-review: passed. Independent audit: not yet performed.
