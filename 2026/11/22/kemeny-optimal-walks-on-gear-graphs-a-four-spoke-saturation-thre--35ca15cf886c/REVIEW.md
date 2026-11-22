# Scientific review: Kemeny-optimal walks on gear graphs

## Correctness — PASS

The theorem concerns the entire convex feasible set of symmetric, irreducible, stochastic matrices on a gear graph, not an a priori two-parameter restriction. The inverse trace is strictly convex in the independent undirected edge weights; the unique optimum is therefore invariant under the graph's full dihedral symmetry. Positive-semidefinite monotonicity forces the alternating rim-edge weight to its vertex-capacity boundary. The remaining two-parameter spectrum separates into a three-dimensional radial block and \(n-1\) Fourier blocks, yielding an explicit strictly convex scalar objective. Jensen plus Cauchy–Schwarz prove its upper-endpoint derivative negative for all \(n\ge7\); exact rational evaluations handle \(n=4,5,6\); the \(n=3\) derivative has a unique interior root. The cyclic Poisson-kernel resolvent identity and a Riemann sum give the exact optimum and the baseline ratio. The standalone checker passed 528 finite assertions, including direct independent Laplacian eigenvalue calculations; those tests are supplementary, not an infinite proof.

## Originality — PASS with residual priority risk

Full-text primary comparisons included Boyd–Diaconis–Xiao (2004), whose target is second-largest eigenvalue modulus rather than Kemeny's inverse spectral trace; Boyd–Diaconis–Parrilo–Xiao (2007), whose graph-symmetry construction applies to a different objective; and Patel–Agharkar–Bullo (2014), whose general Kemeny-convexity/SDP framework does not give the explicit gear-graph optimum, threshold, or asymptotic constants. Gear-graph reference tables list unweighted Kirchhoff indices, not an optimal stochastic transition assignment. Other known wheel, helm and sunlet results concern genuinely different graphs: the inserted rim vertices in a gear graph have two cycle neighbors and are not pendant leaves. A search covering gear/bipartite-wheel/Jahangir terminology and Kemeny/symmetric-walk/maximum-degree alternatives found no statement equivalent to the complete theorem. This supports best-knowledge novelty, not a guarantee against unindexed or differently phrased literature.

## Value — PASS

Gear graphs are a standard infinite family of hub-and-ring networks with alternating degree classes. The result gives the globally optimal transition probabilities in every size, identifies an exact and qualitative holding-probability transition at four rim vertices, gives an exact spectral resolvent for the optimal Kemeny objective, and proves that a conventional maximum-degree allocation incurs a growing \(\sqrt n\)-order penalty. These are natural network-design outcomes, not a single arbitrary parameter evaluation or a numerical exercise. No claim of a paper-scale contribution is required or made.

## Boundaries and uncertainty

This is a uniform-stationary, symmetric-chain result and is not a theorem for arbitrary reversible stationary distributions or directed walks. The baseline comparison is max-degree weighting, not the global fastest-SLEM chain. Finite checks are not a substitute for the inequalities. Unindexed equivalent results and possible translations from general resistance formulas are residual originality risks. Independent audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
