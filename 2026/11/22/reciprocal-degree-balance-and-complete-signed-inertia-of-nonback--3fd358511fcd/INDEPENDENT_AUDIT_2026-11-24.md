# Independent mathematical audit

## correctness

PASS

Checked the unnormalized directed-edge convention and the same-tail/head predecessor/successor counts. They give K=XWX^T−YWY^T with W=diag(d−2). An independent rank derivation uses orthonormal symmetric/antisymmetric vectors for each pair of arcs: K has zero diagonal blocks and off-diagonal block SWD^T, where S and D here are the unoriented and signed edge-by-vertex incidences. Connectivity gives im D^T=1^perp. The kernel of S is zero if nonbipartite and otherwise spanned by the bipartition sign b. Thus the block has rank n−1 except when b belongs to W(1^perp), precisely when 1^T W^(−1)b=0; then it has rank n−2. Block singular values give both signs. Independently checked the inverse-form radical argument in the record and the trace-square formula by X^TX=Y^TY=diag(d), X^TY=A. For the regular spectrum, each adjacency eigenvector at |lambda|<d generates a two-dimensional plane with the stated ± eigenvalues. At |lambda|=d, the overlap gives a one-dimensional common subspace, not a two-dimensional plane. If k is the count of these exceptional adjacency eigenvalues, that subspace contributes k zeros and the orthogonal complement contributes 2m−2n+k, yielding the stated 2m−2n+2k total. This clarifies the source's abbreviated attribution of zeros without changing its formula. Frozen script inspected only; its reported finite output is not the basis of acceptance.

## originality

PASS

The supported distinct part is the signed inertia classification for irregular graphs, including the exact balance exception. Prior incidence and standard projection tools cover structural inputs, and the trace and regular formulas are natural corollaries rather than separate priority claims. No inspected earlier or distinct indexed claim gives the irregular balance classification.

## value

PASS

The self-commutator measures nonnormality of a standard graph operator. The result determines its full signed rank profile in terms of elementary graph data, revealing an extra nullity jump among irregular bipartite graphs that regular formulas and bipartiteness alone miss. The balance test is operational without forming a 2m-by-2m matrix and distinguishes K_{3,4} from the balanced irregular K_{4,4} minus an edge. This structural payoff does not rely on treating the regular corollary as novel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
