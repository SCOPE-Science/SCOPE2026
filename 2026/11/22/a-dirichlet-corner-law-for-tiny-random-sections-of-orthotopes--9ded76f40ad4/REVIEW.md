# Self-review

## Correctness — PASS

The claim specifies Euclidean-motion-invariant affine hyperplanes conditioned to intersect a nondegenerate axis-aligned box, with orientation and offset jointly sampled under the invariant measure. A generic near-support plane intersects an orthant simplex, giving the exact section-volume formula in inward offset depth. Brunn concavity, the inscribed-ball lower bound for central sections, and the diameter upper bound on width provide a **uniform** small-offset bound, justifying dominated convergence across directions with small normal coordinates. Standard gamma integrals then give the coefficient. The same dominated-convergence argument with bounded test functions gives the joint marked law; the density reweighting converts Dirichlet one-half to Dirichlet \(d/[2(d-1)]\), while endpoint symmetry gives uniform vertices and the exact depth-to-volume map yields the beta law. Strict arithmetic–geometric mean gives cube uniqueness. A separately implemented inclusion–exclusion section-volume computation, deterministic numerical quadrature and moment checks corroborate the proof but do not replace it.

## Originality — PASS with historical limitation

The most directly comparable full primary source is van der Jagt, Jongbloed and Vittorietti (2023, https://arxiv.org/abs/2305.02864). Its definitions, general absolute-continuity theorems and numerical-section-density sections were materially read. In Section 5 the authors discuss possible near-zero inverse-square-root behavior of the three-dimensional density and show numerical cubic histograms, but do not supply the present explicit dimension-dependent gamma constant, the complete marked conditional probability limit, or the sharp fixed-volume orthotope optimization. Those general results do not logically imply the numerical coefficient without a calculation. Paul's 1981 cube and dodecahedron study is plausibly related; only the accessible abstract was available, and it describes simulated histograms rather than these analytic laws. Coleman's 1981 box formula pertains to line intercept length rather than plane-section area. Related published central sections, polygon-count laws and shadow-volume results concern distinct statistics. Exact overlap is not proven absent; the inaccessible 1981 full paper remains a named priority risk.

## Mathematical value — PASS

The random-section area density near zero is explicitly identified as difficult for stereological estimation in the source paper, and exact coefficients were missing from its treatment of spatial boxes. The new sharp endpoint asymptotic resolves this concrete geometric-probability observable simultaneously across all dimensions and all box shapes. Its conditional direction and corner structure quantifies the rare mechanisms rather than only their rate. The volume-constrained cube extremality and side-sum universality are nontrivial consequences with immediate statistical and geometric interpretation. It does not require a full finite-threshold density or a general-polytope extension to be a meaningful theorem.

## Scope and remaining risks

Only fixed-dimensional, nondegenerate orthotopes and the small-section limit are proved. The known two-dimensional chord law is acknowledged. No independent expert audit has taken place. An earlier analytic equivalent not indexed by the searches, especially within the full Paul paper, remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
