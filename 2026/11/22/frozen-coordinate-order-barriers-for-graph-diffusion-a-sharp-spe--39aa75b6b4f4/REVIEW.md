# Scientific review

## Correctness — PASS

The final assertion concerns finite coordinatewise old-state residual multipliers on connected symmetric weighted graph heat systems with uniform killing. For a nullcline state the update is exactly frozen at the affected coordinate. Taylor expansion of the true exponential gives the nonzero second derivative, and orthogonal projection of the squared-Laplacian row gives the **sharp** supremum coefficient. The positive nullcline is constructed explicitly. Spectral decomposition proves the all-vertex killing obstruction; symmetry, connectivity and the spectral theorem give the uniformly weighted clique if and only if classification for conservative systems. Distance-two walks prove the unweighted universal-vertex criterion. The two-eigenspace decomposition gives the exact killed-clique formula. The supplied verifier passed 12,445 finite checks independently of these analytic proofs. The finite checks do not prove the infinite claims. No hidden numerical constants or unproved hypotheses are required.

## Originality — PASS (best-knowledge, residual priority risk)

Hoang's August 2026 scheme (1.4)/(2.3) is indeed of the single-old-state residual form. Its Theorem 2.3 gives a denominator Taylor condition **only where the component residual is nonzero**, so it does not imply the present nullcline classification. Alalhareth et al. (2024), Theorem 1, similarly propose a coordinatewise Euler denominator and discuss the zero-component derivative by treating the frozen coordinate as exact; the present graph witness and weighted-graph spectral classification are not present in that work. The Anguelov–Lubuma (2022) scheme is two-endpoint nonlocal, outside the class. Related published-finding corpus graph heat positivity results concern other update functions and do not imply the nullcline obstruction or its complete graph classification. Searches for equivalent formulations, stronger coverage, tables and direct implication found no covering claim, but unpublished or unindexed equivalent work cannot be excluded. No independent novelty assessment is claimed.

## Value — PASS

The issue is intrinsic to one-evaluation positive dynamical discretizations: an instantaneous zero component residual can conceal nonzero local acceleration. The theorem characterizes *all* connected weighted undirected graphs for which the obstacle disappears at every vertex, with a sharp quantitative spectral-variance error and a universal obstruction under any positive killing rate. The exact positive exception and the two-vertex hyperbolic example distinguish model structure from a mere implementation or step-size defect. It tells method designers when a second stage, nonlocal endpoint evaluation, or different update structure is mathematically necessary. It is not a general convergence theorem for arbitrary nonlinear or multistage methods.

## Closest sources, scope and residual risks

Hoang (arXiv:2608.09141, §§1–2 and Theorem 2.3), Alalhareth–Gupta–Kojouharov–Roy (*Computation* 2024, Theorem 1), and Anguelov–Lubuma (arXiv:2207.11618, §2) were inspected in accessible full text. Related indexed graph-diffusion literature treats Padé and Runge–Kutta positivity rather than one-old-residual order barriers. The class requires finite multipliers, connected symmetric conductance graphs, and whole-positive-cone **local** order. Unindexed mathematical priority remains a risk. No claim is made about global order, infinite graphs, directed graphs, or other scheme families.

Self-review: passed. Independent audit: not yet performed.
