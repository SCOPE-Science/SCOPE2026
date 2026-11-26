# Independent mathematical audit

## correctness

PASS

The token graph is the vertex-edge incidence graph of K_n. With omitted originals R of size at least two, every internal edge-vertex of R must be selected and these vertices suffice to dominate R. With one omitted original, an incident selected edge lets its other endpoint be deleted, so this case never gives a minimal state. With none omitted, the only minimal state is the all-original set U. Each exact internal-edge state D_R is minimal: dropping an edge leaves it undominated; dropping an original leaves an unselected edge from it to R undominated. The sizes start at b_2=n-1 and b_3=n and rise by r-1. At budget n, distinct minima indexed by pairs have union size n-|R∩R'|+2≥n+1, so no common size-n neighbor; every nonminimal size-n state attaches to exactly one minimum. U and any triples at that ceiling are isolated. At k≥n+1 a subceiling D_R with |R|≥3 can add an omitted original and delete its incident selected edge-vertices, reaching D_(R minus that original) with peak b_r+1. Pair minima connect to U with peak n+1. Thus all non-ceiling minima and all nonminimal states lie in one core; ceiling minima are isolated. This also covers n=2,3, empty budgets, and budgets beyond the vertex count. In the prose the n-3 exceptional budgets are the losses after first connectivity, not a count including the two initial nonempty disconnected budgets for n≥4.

## originality

PASS

The supported distinct claim is the all-budget ordinary-domination TAR component census and repeated losses after first connectivity. The minimum domination number, incidence-graph identification, static size counts and general reachability methods are not credited as new. No distinct covering claim was found in the inspected evidence.

## value

PASS

The count exposes an unbounded number of distinct connectivity losses caused by new maximal-budget minimal states, despite continued connectivity of the old core. This is a structural obstruction within a natural infinite graph family, not a static enumeration: it gives each exceptional budget, counts its isolated states, and separates first from permanent connectivity at linear versus quadratic scales.

The dated certificate retains the supplied scientific assessment, sources and limitations.
