# Scientific review

## Correctness — PASS

The one-step terminal-count Markov transition follows from uniform parent choice. The expectation, variance and regression factors are derived from exact conditional moments with the exceptional two-vertex initial state handled explicitly. Conditional independence at the fork gives the entire cross-branch covariance kernel; monotone common-uniform coupling proves cross-branch increasing-event association. The bivariate martingale expansion has bounded increments and predictable quadratic variation converging to the stated (possibly singular) Gaussian covariance matrix. The separate finite checker reproduces the resulting exact cross-time formulas and the inequality for every enumerated instance. Finite checks are supporting evidence, not the basis for the infinite theorems.

## Originality — PASS, with residual risk

Rácz–Sridhar (arXiv:2004.13537, original 2020 submission) defines the same forked shared-prefix uniform-attachment model, but its identified centrality/subtree detection results do not give the stated terminal-count cross-time covariance or increasing-event association. Janson (DOI:10.1002/rsa.20046) already proves marginal outdegree-zero normal laws and same-tree functional Gaussian limits; those are not new here, and the cubic behavior is compatible with his covariance kernel. Bäumler–Rácz–Ross–Sridhar (2026), Appendix A, establishes paired leaf-count Gaussian laws for a *different* time-homogeneous coupling that chooses aligned and independent parent attachments at each time with fixed probabilities, rather than making one deterministic fork. That earlier paired-leaf result is not claimed as new. The new scoped statement concerns exact finite cross-branch dependence in the shared-prefix model, rank one across arbitrary future times, and a global positive-association statement for terminal-count trajectories. Other compared findings concern distinct recursive-tree observables, especially root degree with leaves and root attachments with path length. Remaining risk: the full result might be an unlocated implicit consequence of a published general forked-Markov or tree-functional theorem, rather than a previously isolated theorem.

## Value — PASS

Shared ancestral growth followed by independent continuations is a natural correlated-network model. Quantifying which observables retain memory of that common history is necessary for interpreting simple summary statistics. An exact all-time rank-one dependence kernel and positive association give qualitative and quantitative structure, while the cubic attenuation of the limiting correlation establishes the precise signal retained by terminal counts; the endpoint Gaussian classification is also explicit. The distinction between rooted terminal vertices and unrooted leaves is essential.

## Limits

No claim is made about leaf counts in preferential attachment, arbitrary random seeds, unrooted-degree-one statistics, unlabeled-tree inference, optimal tests, or total-variation convergence. The qualitative association mechanism is standard for monotone one-dimensional Markov chains; its application is included as part of the full exact two-branch classification, not presented as a standalone general theorem. Historical novelty is provisional until additional specialist literature is checked.

Self-review: passed. Independent audit: not yet performed.
