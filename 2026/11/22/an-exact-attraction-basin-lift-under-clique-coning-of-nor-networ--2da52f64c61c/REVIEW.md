# Independent mathematical audit

## correctness

PASS

Symmetry of adjacency gives A⊆f²(A) for every support A, and antitonicity gives the reverse comparison needed for f³=f. In an isolate-free graph only the empty support maps to the full support; the preimages of empty are exactly the total dominating supports. Hence the full principal basin has size T+1. Directly for arbitrary r, split a state into base support S and clique support U. If U is empty and S is nonempty, the next state is (f_H(S),∅); exactly the nonprincipal base basins avoid empty forever, preserving the trajectories and labelled basins. The empty state maps to all vertices. If U is nonempty, the update gives zero except when S is empty and U is a singleton, in which case it gives that same singleton. This proves the complete dictionary, including no external predecessors to the singleton fixed points, and adds precisely 2^{n+r}−2^n−r states to the original principal count. At r=1 the principal basin size 2^n+T(H) is already strictly above half, and the excess strictly grows on further lifts. Division by 2^{n+r} gives the claimed limit; r=0 reduces to the base. The example total-domination counts 4,9,11 give all the displayed basin sizes. RESULT.md lines 21–37 provide a replay via one hub. Both uploaded checkers were inspected, not executed. CHECKS.txt labels 262 as the random base count, but the code prints a count bounded by 150 there; 262 is the number of attachment experiments for 131 accepted random draws, consistent with the total 1890. This is a nonmaterial supporting-transcript discrepancy, not an all-size proof issue.

## originality

PASS

Pass is for the exact labelled nonprincipal basin transport under arbitrary clique coning on every isolate-free base, with the added basins identified. Do not credit the one-step NOR transient bound, the principal-basin count in isolation, maximal-independent-set counting, or the wheel specialization as separate original results. The wheel proof already contains the one-hub update and zero-hub confinement for its cyclic base; it is a close methodology overlap.

## value

PASS

Clique joining is a natural graph operation. Preserving the actual labelled basins of every old nonprincipal orbit, not just counting attractors or computing the principal mass, lets one transfer any base classification under arbitrarily many new vertices without recomputation. That structural information is what survives the known total-domination formula and the wheel example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
