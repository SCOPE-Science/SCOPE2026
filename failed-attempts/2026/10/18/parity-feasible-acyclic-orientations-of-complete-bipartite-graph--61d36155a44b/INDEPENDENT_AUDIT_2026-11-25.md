# Independent mathematical audit

## correctness

PASS

Necessity follows by the indegree sum and existence of a source. In the induction, deleting a zero-bit vertex as source toggles the opposite part, preserving feasibility because the edge count drops by the size of that part. For parts of size at least two, if deleting a zero on side A makes every remaining bit one, then A had only that zero and B was all zero. Deleting a zero on B instead turns all the originally odd A bits to zero and avoids the obstruction. If A was all one, deleting a zero from B also works. Stars are forced by the leaf bits and the global sum. The all-odd vector is globally feasible only for two even part sizes. For K(2,b), every simple directed cycle is a 4-cycle and exists precisely when both mixed columns occur. Thus odd columns use one common type, and the number of all-one columns fixes the row bits modulo two. If there are even columns, flipping one fixed even column pairs the assignments of the two row parities. This gives 2^(b−1) at t=0 and 2^(b−t) when 0<t<b. At t=b, the two mixed choices give the two distinct feasible row signatures if b is odd, or both give (0,0) if b is even. An independently written literal orientation census using Kahn sorting passed 1,580 signature checks (790 globally feasible) and 504 two-row fibre checks; scope was 1≤a≤3, a≤b≤5, plus K(2,6) and K(2,7). Replay: /workspace/branches/dacb3b45-e4a3-4449-b345-93da39a44d7e/biclique_parity_census.py with its settings documented in census-bounded.txt. The uploaded checker was inspected, not run. Finite evidence does not replace the proofs.

## originality

FAIL

The general existence result is stated identically in an independently indexed feasibility record. The two-row refinement is not covered by feasibility alone or by the poly-Bernoulli totals, but it is a mechanical restriction and parity marginal of the independently indexed complete three-row Walsh formula. That formula gives the two-row allowed-column product identity by forcing the third row to be a source. Neither component survives as a distinct exact result under the statement-and-implication standard. This is existing coverage, not a conclusion about historical priority, chronology of discovery or the correctness of the frozen result.

## value

PASS

Prescribed vertex parity is a natural constraint in acyclic orientation, and the full labelled fibre distribution answers a substantive counting question that existence or unrefined totals do not answer. The especially small all-odd boundary fibre explains an actual change in structure. This mathematical usefulness does not remove the demonstrated overlap with existing exact coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
