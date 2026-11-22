# Self-review

## Correctness — PASS

The proof shows that witness intersections are simultaneous prefix/suffix inequalities, yielding a consecutive block. For an interior block, avoiding its flanks is equivalent to disjointness of those flanking intervals; the converse chooses an interval endpoint immediately beyond each flank. Missing blocks correspond bijectively to nonconsecutive edges. Proper ordering makes the number of consecutive edges exactly \(m-c\), proving the cycle-rank identity for every \(m\ge1\). Chordality and absence of claws yield the path-forest equality criterion. The verifier corroborated the complete graded identity over 544 finite tests, but only the proof covers every size.

## Originality — PASS within inspected evidence

The 2015 interval-graph identifying-code bounds already give consecutive-block behavior and the quadratic extremal count; no novelty is claimed for either. The 2026 papers give general first-order type bounds and neighborhood-complexity results. The new claim is the precise failure criterion for each block and the nonconsecutive-edge bijection, including the graph-intrinsic cycle-rank defect and grade-by-grade polynomial. A mathematically equivalent earlier statement could remain in older interval-neighborhood work, so historical priority is provisional.

## Value — PASS

One-point quantifier-free type counts are a basic finite-model invariant; here all attainable type cardinalities and the exact obstruction to maximum capacity can be computed from one fixed proper interval representation. The cycle-rank identity is a structural, natural refinement of known quadratic growth and determines all equality cases within the proper-base family.

## Scope and residual limitations

The extension vertex may be any interval, so adding it need not preserve properness. Existing vertices and higher-rank complete types are not counted. Only the ungraded cardinality is expressly representation-independent. No independent mathematical or historical-priority audit was performed.

Self-review: passed. Independent audit: not yet performed.
