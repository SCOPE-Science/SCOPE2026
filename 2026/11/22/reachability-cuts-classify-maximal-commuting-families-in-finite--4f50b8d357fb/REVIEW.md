# Independent mathematical audit

## correctness

PASS

In the absorbing-zero semigroup, two positive paths commute exactly when neither endpoint match permits concatenation: two nonzero reverse products would give a cycle. A stationary idempotent conflicts exactly with positive paths incident to its vertex. Any maximal commutative subsemigroup has zero; its positive sources S and targets T are disjoint. Saturation adds all positive paths from S to T and every stationary path outside their support, preserving closure (all positive products are zero). Per-vertex support is necessary and sufficient: a missing path either has a neutral endpoint, starts in T or ends in S, or was already included; a missing idempotent conflicts with a path at that vertex. This proves uniqueness and the size polynomial, including isolated vertices and parallel paths. For p:u→v the incompatible paths ending at u and starting at v are disjoint by acyclicity; for e_v remove the stationary path from each endpoint count. On the line, admissibility requires first active letter S and last T; counting words with fixed first and last positions gives (3ⁿ−2n−1)/4 before including the diagonal. The bound on sizes uses floor(m²/4)−m nondecreasing for m≥2, attained by a balanced cut when comparing with the diagonal; n=1 has only the diagonal. If L=n(n+1)/2, summing centralizer deficits on the line gives (L+1)²−n(n−1)−2Σ_i i(n−i)=(L+1)²−n(n−1)(n+4)/3, equivalent to the claimed formula. The remark about reversing words is unnecessary; reversal alone does not preserve admissibility. From /workspace, python3 reproductions/algebra.py semigroup independently reproduced ordered pair totals from multiplication for lines n=1–12 (first five 4,12,35,89,196) and maximal clique counts and sizes for n=1–5. The inspected frozen checker reports 79 cases with explicit paths; it was not executed in this review. Finite tests do not establish the uniform proof or extend it to cyclic quivers.

## originality

PASS

Pass the supported reachability-admissible classification and multiplicity-sensitive size and centralizer enumeration on arbitrary acyclic zero path semigroups, with the line formulas as specializations. The semigroup, endpoint obstruction and full matrix-unit rectangle mechanism are not new; closely related indexed classifications concern different ambient semigroups. No inspected statement supplies the conjunction claimed here.

## value

PASS

It classifies maximal commutative subsemigroups of a natural zero semigroup and separates two intrinsic invariants: family counts see only reachability, but family sizes see the number of distinct paths. The complete size distribution and element-centralizer counts answer more than a single small-case size calculation; the line formula demonstrates the resulting count on a standard example. The local mechanism is elementary, but the fully specified cut support and weighted census are useful structural information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
