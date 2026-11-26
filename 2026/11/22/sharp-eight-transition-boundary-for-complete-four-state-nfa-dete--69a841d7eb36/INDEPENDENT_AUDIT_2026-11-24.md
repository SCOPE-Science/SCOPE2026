# Independent mathematical audit

## correctness

PASS

Each labeled relation is one subset of 32 distinct triples. Enumeration by combinations of the 32 indices is exhaustive at each edge budget and does not rely on monotonicity under adding edges. For each relation the subset transitions are row unions with the empty set mapped to itself; breadth-first closure from {0} finds every and only reachable subset. For full reach, the least pair relation containing the acceptance-disagreeing pairs and closed under predecessor letters is exactly suffix distinguishability, by induction on suffix length. So all 120 unordered pairs must be marked for minimal complete DFA size 16. An original batched exact replay inspected all 15,033,173 relations over budgets 0–8, matching the binomial count at each. It found zero relations of full reach for each e<=7, 5,808 full-reach relations at e=8, and 56,544 full-minimal relation/final-set pairs at e=8, matching the complete mask profile including zero. The explicit witness separately reaches 16 and distinguishes all 120 pairs. Replay and logs: /workspace/branches/7807f1ca-cb75-497b-b490-3a8e52eeceb2/{recount.py,recount_full.log,replay_witness.py,replay_witness.log}. The frozen code and log were inspected but the frozen programs were not executed. The result is a minimum existence budget and an exact census there, not a statement that every eight-edge relation is extremal or about budgets above eight.

## originality

PASS

The classical subset bound and unrestricted existence of four-state binary full determinization are not new. The supported distinct claim is the edge-constrained cutoff together with the exact labeled boundary census, separating full reach from full minimality. No inspected comparison covers this combination or mechanically gives the threshold and counts.

## value

PASS

The invariant is the first edge budget at which the classical exponential worst-case is actually feasible under sparse nondeterminism, not simply the state count of a chosen witness. The complete boundary census distinguishes attainability of all subsets from retaining all of them after minimization and quantifies the role of accepting sets. This provides an exact small benchmark under a natural transition resource constraint, without extrapolating to larger automata.

The dated certificate retains the supplied scientific assessment, sources and limitations.
