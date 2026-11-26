# Independent mathematical audit

## correctness

PASS

The quantifiers are graph-informed but matrix-blind: G has at least one edge, the edge coefficients have unit unordered squared energy, and each probe has the uniform full-cube marginal. For an arbitrary coupling put D_i=Z_iW_i and H_{ij}=(Z_iZ_j+W_iW_j)/2. Then E H_{ij}=0 and H_{ij}²=1_{D_i=D_j}. Concentrating the adversarial coefficient on any single edge gives a variance lower bound of 4 times the largest uncut probability for the induced cut law, irrespective of dependence between D and Z. Conversely, sample any cut independently of Z and multiply Z by its signing D to obtain W: both marginals are uniform, and for distinct unordered edges the sign monomials are orthogonal even if the edges meet at a vertex. The covariance is diagonal with exactly those uncut probabilities on the diagonal, so the edgewise lower bound is attained after optimizing over cut laws. Normalizing and de-normalizing a fractional cover gives the reciprocal max-min crossing probability; it is positive because independent uniform vertex signs cross each edge with probability 1/2. The graph is bipartite exactly when one cut can cross all edges, and fixed signings on a nonbipartite graph leave an edge with variance 4. Automorphism averaging gives the MaxCut ratio for edge-transitive graphs. The odd-cycle and complete-graph counts agree with the formulas; for the pendant triangle, uniform choice of the uncut triangle edge with the pendant always crossed gives exactly 4/3, not the uniform-edge average 1. A diagonal shift preserves the variance and permits positive definiteness. For the cited unscaled K₄ example, the single-probe error takes −4,0,12 with multiplicities 6,8,2 over 16 cube points; opposite quantile pairing attains 6, whereas the robust optimal cut law gives 8. These checks do not assert a lower bound for different marginals, weights, or adaptive schemes. The frozen finite verifier was inspected but not run; the variational identity has an analytical proof.

## originality

PASS

The supported distinct theorem identifies the graph-informed, matrix-blind minimax variance over all two-probe couplings with the known fractional cut-cover invariant. The cut LP and duality, shared-sign construction, and some dyadic complete-graph coefficients are already known. The inspected fixed-matrix, class-supported, and Hadamard results do not provide the all-couplings robust lower bound and matching unrestricted optimum for arbitrary known graphs.

## value

PASS

The theorem resolves a natural robust numerical-linear-algebra design problem exactly and gives a universally attaining sampler, even though arbitrary nonlinear probe couplings are allowed. It explains a sharp bipartiteness obstruction, a sizable improvement over fixed sign flips, and why ordinary MaxCut is insufficient in general. This is an optimization equivalence and structural lower bound, not merely an evaluation of the known LP or a computational-speedup claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
