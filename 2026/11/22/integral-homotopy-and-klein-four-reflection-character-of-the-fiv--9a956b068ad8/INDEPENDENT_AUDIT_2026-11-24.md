# Independent mathematical audit

## correctness

PASS

Both original mathematical assertions are true. A fresh exact check in /workspace/branches/check_grid_independent.py uses bipartiteness and König's theorem: at most four vertices per color are allowed, and alpha equals face cardinality minus maximum matching size. This reproduces the eight-entry f-vector and 72,568 nonempty faces. The pivot matching gives 36,039 pairs; a separate complete directed DFS traverses 446,610 covers with no cycles and leaves one vertex and 489 seven-cells. An independent orbit-subset computation gives fixed-face counts (72568,252,444,212) and Lefschetz sums (−488,−30,−12,−14). In degree seven, traces are one minus those sums. For a fixed nonempty face using b orbits the orientation sign times simplicial parity is (−1)^(b−1), so the trace test correctly includes inversions. The four multiplicities are (137,123,114,115). The narrowed claim is reproduced by /workspace/repairs/2/check_grid_reflections.py, including its dual support check. Quotient ranks 260, 251, 252 and 137 follow by rational invariants after barycentric subdivision; these are ordinary orbit spaces. The verification checks no other grid, no integral lattice splitting, and no equivariant homotopy equivalence. Frozen scripts were inspected, not executed.

## originality

PASS

PASS for the repaired rational reflection character only. The original inclusion of the integral wedge as a novel result is not supported: the older publication names this exact case in Table 3 and specifies the lexicographic element matching, whose replay has critical cells only in dimension ten aside from the base vertex. The wedge for the robust complex then follows mechanically. The freeze is mathematically correct, but the original novelty scope is not passed. The complete corrected scientific files in /workspace/repairs/2 narrow the finding to the actual rational action and its quotient ranks; the known rank and mechanical wedge implication are background only.

## value

PASS

The single finite grid is a natural unresolved symmetry instance of the robust-clique problem, and row and column reversal form its natural full rectangular symmetry. The exact rational action distinguishes which cycles are invariant under each reflection and the half-turn; it also determines exact rational Betti ranks of the ordinary symmetry quotients. These concrete invariants are not available from the prior ordinary homotopy or rank, and are independently useful without a general-width theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
