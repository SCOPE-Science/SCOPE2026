# Independent mathematical audit

## correctness

PASS

Decomposing the shifted Laplacian into the two shore-constant directions and their orthogonal complements gives within-shore entry κ and cross-shore entry χ, with χ/κ=1+μ/n. Each independent class probe contributes four times the sum over unordered within-class pairs. In the resulting cost, an exchange between two mixed classes at fixed class sizes strictly increases the sum of squared shore imbalances and lowers cost for θ>1. With only one mixed class, if both pure classes were on the same shore, moving the minority contribution of the mixed class into a pure class would save θn per transferred vertex against fewer than n new collisions. Thus the gain is D=ns−s²+(2−θ)ab, with s=a+b. For 1<θ<2 fixed s forces balanced a,b; a balanced positive choice at an integer nearest n/2 beats the pure gain, including s=2 for n=3. Values s≥n are worse (the successive differences are negative there), and s=1 is no better than the pure gain. Strictly decreasing differences give only adjacent interior ties. For θ≥2 the upper bound floor(n²/4) requires s nearest n/2, with ab=0 required only when θ>2. This also yields the unlabeled counting rules: a unique mixed class identifies its two subsets; in the even pure case the two equal halves are unordered. An independent exact-integer check grouped partitions by the two triples of shore counts, tested all feasible triples for n=3–12 at nine rational θ values each, and matched all optimizer signatures, including internal ties at (n,θ)=(6,3/2),(8,3/2),(12,5/4).

## originality

PASS

The per-partition variance identity and distance-based probing are established. Earlier bipartite work has a different action budget; same-budget split-graph and star results concern different cost matrices. The inspected sources do not determine the biclique threshold, staircase or complete equality families, including via the equivalent weighted three-cut formulation.

## value

PASS

The fixed three-action variance budget is operationally meaningful and exposes an exact reversal not seen at two actions on this graph. Weak screening forces a nonproper partition despite higher individual cross-shore pair costs; at and above critical screening the precise optimizer sets are different. Strict uncrossing and the discrete staircase give a usable characterization rather than just a numerical improvement or a single example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
