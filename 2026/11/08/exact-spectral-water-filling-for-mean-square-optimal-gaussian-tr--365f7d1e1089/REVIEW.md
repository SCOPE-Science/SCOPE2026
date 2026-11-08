# Scientific assessment of the Gaussian trace-subspace water-filling theorem

## Correctness

**PASS, self-review.** The squared-risk identity follows directly from the independent chi-square representation of Gaussian quadratic forms. The feasible Ritz eigenvalue intervals are necessary by Cauchy interlacing and sufficient by the real symmetric Fan–Pall theorem. The optimization is strictly convex on a box; a monotone scalar equation gives its sole minimizer, and monotonicity of the interval endpoints makes the clipped solution a feasible decreasing Ritz spectrum. The principal-subspace criterion follows from the box KKT conditions, explicitly exempting degenerate intervals. The exact low-rank counterexample is evaluated algebraically, not inferred from simulation. The verification program passed 5,060 checks from the package; it is not an exhaustive proof for arbitrary dimensions.

## Originality

**PASS, provisional historical priority.** The 2026 truncated infHutch construction specifies Gaussian probes on fixed finite-dimensional bases and discusses bias and variance, without giving the global design optimum across subspaces. Fan–Pall already characterizes feasible compression spectra, but does not optimize this estimator risk. The 2016 matrix-free trace work studies a deterministic compressed trace after randomized eigenspace extraction; Hutch++ uses exact low-rank trace plus unbiased residual probes. Neither comparison implies the present clipped-Ritz solution by itself. Search coverage includes direct formula synonyms, eigenvalue-interlacing/water-filling aliases, biased compression and general trace-estimation references. There is a residual chance that the convex risk optimization has appeared in an unindexed statistics or spectral-design source, and the conclusion must be revisited if such stronger coverage is located.

## Value

**PASS within the stated benchmark.** Choosing a sampling basis for truncated operator trace estimation naturally trades truncation bias against stochastic variance. The theorem completely solves the fixed-rank, fixed-probe-budget *oracle* design problem, including a sharp necessary-and-sufficient threshold for principal-eigenspace optimality. The exact rank-deficient witness shows that the seemingly perfect spectral capture can be uniformly suboptimal at every finite sample count. This gives a nontrivial design baseline against which heuristic sampling subspaces can be assessed. It does not yield a spectral-free practical algorithm, and it does not concern Hutch++'s unbiased complement estimator.

## Closest sources and limitations

The closest directly motivating source is Bujanović et al., arXiv:2608.28135, Section 3.3.1 (truncated Gaussian trace estimator). The spectral feasibility ingredient is the classical real Fan–Pall converse, restated by Holbrook et al., arXiv:1203.3908, Theorem 1. Related but noncovering algorithms appear in Saibaba et al., arXiv:1605.04893, and Meyer et al., arXiv:2010.09649. Scientific limits include reliance on a known spectrum for the oracle minimizer, independent Gaussian probes, squared risk and a deterministic fixed rank; the historical-originality conclusion is conditional on accessible literature.

Self-review: passed. Independent audit: not yet performed.
