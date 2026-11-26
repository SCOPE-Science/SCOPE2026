# Independent mathematical audit

## correctness

PASS

For a shell of radius t the restricted ultrametric has diameter at most t, and a last-common-ancestor height of (r-t)d(x,y)/2 above the leaves produces the required same-shell path cost, with a stem if the graft height L(t) exceeds the dendrogram height. Along the trunk H is strictly increasing. F=H+L and H-L=2rt, so pairs at distinct interior radii t<s give F(s)-2rt, exactly (r-s)s+2r(s-t); the equality d(x,y)=s follows from the strong triangle inequality in both directions. At the root the cost is F(t), and with an outside endpoint it is 2r(r-t) or 2r^2 from the root; all outside sites map to the same vertex. This accounts for the cutoff equality d(m,x)=r, singleton shells and the degenerate pair costs. The cut formula is a lower bound by conservation on every edge, and it is attained by decomposing the unique signed net tree flow into transport paths plus stationary mass. Any plan on the quotient tree vertices lifts by distributing each incoming and outgoing amount according to the original marginal masses in each fiber. Maximizing over centers then gives the stated metric without interchanging transport and maximization. The stated line counterexample has distinct largest and second-largest four-point sums (10 and 9).

## originality

PASS

The radial-tree representation of the specific localized cost is the distinct result; the cut formula for a known tree is established background. Neither the inspected original cost definition and auxiliary-Wasserstein realization nor the known cut formulas provide the identification needed here.

## value

PASS

The result converts a stability-related localized metric defined via a family of transport optimizations into weighted sums of observable mass imbalances in a natural hierarchical class. For a fixed support and scale the trees depend only on the metric and can be reused for arbitrary measure comparisons, which replaces an entire transport LP at each center by a subtree pass. The obstruction on the ordinary four-point line shows this representation is not merely a restatement for all finite inputs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
