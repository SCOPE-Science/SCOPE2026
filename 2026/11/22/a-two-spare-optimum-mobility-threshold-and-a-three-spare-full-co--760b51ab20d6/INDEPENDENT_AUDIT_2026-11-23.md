# Independent mathematical audit

## correctness

PASS

A shortest cube path flips each used coordinate once; a path of length less than four extends along an unused coordinate. Thus the maximal geodesics are exactly the 192 unoriented antipodal paths. I generated their masks and marked every subset contained in a path complement by a Boolean subset transform; the unmarked masks are exactly the transversals. In ascending cardinality I marked the whole upset of each newly found inclusion-minimal set; the complete census and minimal census agree coefficient by coefficient with the frozen T and M, including totals 22499 and 460. For components I used the cover of the budgeted graph by upper stars of its inclusion-minimal sets: a star is connected by adding vertices from its root; two stars intersect exactly if their root union fits the cap; and every legal edge lies in a star because the smaller endpoint contains a minimal set. This independent component computation gave exactly 40 singleton components at 6, 160 singletons and 40 size-11 components at 7, 260 singletons and one size-3250 component at 8, and one component of size 9430 at 9. The budget-seven minima have ten neighbors each, and no two share a seven-set, so those components are stars. At budget eight, the singleton components are precisely the minimal eight-sets, so all forty six-sets connect. There are no minimal sets larger than eight, so any additional states at higher budgets can delete down into the connected budget-nine graph without violating feasibility. For optimum distances, I removed the eight-set vertices and replaced each feasible 7–8–7 segment between distinct seven-sets by an edge of weight two, keeping six–seven edges at weight one; this preserves distances between six-sets by expansion of the edges. Exact shortest paths in that graph reproduce the histogram (4:60, 6:160, 8:480, 12:80).

## originality

PASS

Credit the known minimum six and the forty optima in two families. The distinct contribution is the full transversal and minimality data, the first connected budgets for optima and for all feasible states, and constrained shortest distances. The checked literature and related records do not supply that joint census and dynamics.

## value

PASS

The four-cube is a standard small benchmark with already classified minimum covers. Under the natural detector addition/removal constraint, this result shows a real difference between mobility among the most economical configurations and mobility among all admissible configurations: isolated saturated minimal covers persist after the optima connect, and allowed relaxation of the cap first increases the component count. The exact constrained optimum metric quantifies the necessary detours; neither that metric nor the distinct thresholds is just a relabeling of the prior optimum census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
