# Scientific review: degree-one/three/five epidemic-size optimization

## Correctness — PASS

The object is the asymptotic giant-component fraction after independent bond thinning of the configuration model, not a finite epidemic's expected size. The standard generating functions are \(G_0(u)=u^3+tu(1-u^2)^2\) and \(G_1(u)=G'_0(u)/3\). At supercriticality, canceling \(1-u\) yields the strictly increasing implicit function \(T^{-1}=\Psi(u,t)\); the no-giant threshold is exactly \(T=3/(6+8t)\). Direct exact algebra factors the optimizer derivative as \((1+u)P(u,t)/(3\Psi_u)\). The polynomial's coefficient signs give one positive root in \((1/2,1)\) for each admissible \(t\). Its negative parameter derivative makes the root increase, and the corresponding transmission frontier decreases strictly; the derivative therefore crosses sign at most once and in the asserted direction. Endpoint and subcritical cases are covered. The standalone verifier passed 26,587 assertions including exact rational identities and independent root computations. Finite tests corroborate but do not establish the infinite-graph conclusion; that limit rests on the cited branching theory.

## Originality — PASS (self-review, priority not certified)

The full generating-function framework predates this finding. Leibenzon–Assaf (2023) describe a qualitative heterogeneity phase transition for network SIR sizes and a high-mean-degree approximation, but do not prove the exact all-transmissibility global optimizer on the fixed-mean distribution supported on \(\{1,3,5\}\). Britton–Trapman (2010/2012) optimize over *unrestricted* degree distributions and find a possible optimum with mass at zero and consecutive positive degrees, which does not imply a constrained three-odd-degree optimizer. Deijfen–Rosengren–Trapman (2017/2018) derive lower/upper bounds and show numerical dependence on low-degree masses, without the present two finite-degree algebraic thresholds. Published text and mathematical-record searches for the same degree law, its percolation/generating-function equivalents and broader extrema yielded no explicit covering statement. The principal residual risk is an unindexed treatment of the same restricted variation, or an unpublished implication from broader degree-ordering inequalities. Search absence is not proof of novelty.

## Value — PASS

Degree heterogeneity can help an epidemic start yet fragment its eventual reach. The smallest symmetric mean-preserving perturbation among three positive odd degree classes isolates that tension without changing average degree. The complete global phase diagram proves that the optimal variance passes through high, strictly interior and zero regimes with explicit algebraic thresholds, rather than merely illustrating the effect numerically. It can serve as a benchmark for constrained contact-degree design and a finite-degree counterpoint to large-mean-degree expansions. The exact family restriction is essential and reported openly; the result does not purport to optimize among arbitrary distributions.

## Closest sources and scientific limits

- A. Leibenzon and M. Assaf, *Heterogeneity can markedly increase final outbreak size in the SIR model of epidemics* (arXiv:2306.09024, 2023), full accessible article equations and phase-transition discussion.
- T. Britton and P. Trapman, *Maximizing the size of the giant* (arXiv:1010.0524, 2010), especially Theorem 4.1 on unconstrained thinned configuration-model optimization.
- M. Deijfen, S. Rosengren and P. Trapman, *The Tail does not Determine the Size of the Giant* (arXiv:1710.01208, 2017), especially Sections 1.1–1.4 and Theorem 1.1.

No independent external mathematical audit, full-database novelty certification, finite-network concentration estimate, or dependent-transmission extension is claimed.

Self-review: passed. Independent audit: not yet performed.
