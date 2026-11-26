# Independent mathematical audit

## correctness

PASS

Reconstructed the proof of RESULT.md lines 19–55. Pointwise stabilizers act transitively on generic atoms and ordered distinct generic pairs, giving uniform arcs for each named interface and a separate off-diagonal bit. A named-to-named walk that visits generic atoms can replace everything between its first entry and last exit by two arcs through one generic vertex, even if the removed segment contains adjacent generic vertices. The typed shortest lengths are then the internal named length δ or β+2+α for named endpoints, and the first/last generic-visit shortcut gives 1+α or 1+β when exactly one endpoint is generic. Without an off-diagonal generic arc, a walk between two distinct generic endpoints has a named-only block joining F to B between its initial generic departure and first generic return; this costs at least 2+γ and any internal minimizer realizes it. Loops do not affect reflexive distances. In the disconnected generic case no named vertex can share the SCC of even one generic atom: mutual reachability through a named vertex would concatenate to a path between distinct generic atoms, by the uniform mixed formulas. Deleting repeats gives length at most m+1; the directed named chain between two distinct generic endpoints attains it for m≥1, and one arc attains it at m=0. Computing δ then vector and scalar minima is cubic in the size of the finite orbit description (constant at m=0). This is an all-m proof; the reported finite Floyd–Warshall checks were inspected but not rerun.

## originality

PASS

The distinguishing claim is an explicit exact distance profile with one min-plus correction to the internal named distances and the generic off-diagonal distance and SCC classification. Fixed-context reachability and a finite-step cutoff are credited as prior consequences. The strongest comparisons inspected do not supply the exact profile.

## value

PASS

This is a useful structural lemma for exact symbolic geodesics, not a new generic shortest-path algorithm. It reuses the internal named distance matrix and isolates precisely what anonymous transit changes: one separable correction, two endpoint profiles, and one effective off-diagonal distance. It also distinguishes a single generic SCC from genuinely singleton SCCs; an ordinary quotient by generic identity alone obscures the latter. The unbounded supported-graph family and exact boundary cases are the motivation, not recomputation of the known orbit cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
