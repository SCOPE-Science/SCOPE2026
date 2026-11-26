# Independent mathematical audit

## correctness

PASS

The graph has four distinct open neighbors at each of its eighteen labelled vertices. I independently represented a valid code as a hitting set for the eighteen open neighborhoods and, for every distinct pair i,j, the clause {i,j} union (N(i) symmetric difference N(j)). The latter is vacuous if either vertex is selected and otherwise is equivalent to unequal signatures. This gives a different exact exhaustive predicate from the supplied programs. A row-major implementation filters all 262,144 subsets, then constructs every legal single-bit edge by removing one bit of the upper set, retaining it if the lower set passes and the upper size meets the budget. Sparse component and unweighted-distance calculations reproduce the entire degree-6-through-18 polynomial (total 103,056), the twelve alternating-column minima, and all component profiles for B=6 through 18. At B=8 there are two distinct components with six minima each; even smaller budgets cannot merge them. At B=9 there is a 22,415-state component with all minima and exactly sixty singleton states; at B=10 the 48,620 states form a single component. The clauses also show the predicate is upward closed; the independent census verifies that no inclusion-minimal code exceeds size nine. Thus a larger code can descend to size ten within the larger budget, in agreement with the explicit connectivity checks through B=18. At B=9 a state of size below nine can add a vertex, so isolates must have size nine. A size-nine isolate has no one-step deletion and, by upward closure, no valid proper subset. From each optimum the independent shortest paths give multiplicities 1,3,2,6 at distances 0,4,6,12. Same-parity minima differ by a transposition or three-cycle of omitted rows, so their symmetric difference has size four or six and a Hamming-length path through their union fits budget nine by upward closure. Opposite parities are disjoint and require at least twelve flips; the exhaustive distances attain that bound for every pair. I separately checked the provided thirteen masks for legality, capacity, the encoding, and opposite optimum endpoints; the witness alone would not prove the full profile.

## originality

PASS

Accept the distinct exact add/delete capacity classification and metric on C3 square C6, not the previously known scalar minimum or any part of the alternating construction already implied by the literature. The examined close matches either change the feasible predicate, graph or move rule, or concern only a scalar optimum. The possible extent of prior coverage of the twelve-minimum structure is left open rather than being used to establish novelty.

## value

PASS

The first period-six tight torus in the known scalar family is a natural benchmark for incremental detector placement, not an arbitrary small graph chosen only to compute a count. The gap between universal mobility of minimum placements and full feasible-state connectivity answers two practically and mathematically different reconfiguration questions. The sixty inclusion-minimal traps witness the distinction, and the shortest-path census sharpens what is achievable at the smaller threshold. It is a useful exact finite benchmark even without an extension to larger tori.

The dated certificate retains the supplied scientific assessment, sources and limitations.
