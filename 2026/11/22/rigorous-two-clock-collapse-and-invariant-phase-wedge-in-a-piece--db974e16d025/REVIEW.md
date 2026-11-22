# Scientific review — sharp critical collapse

**Correctness (PASS).** The claim concerns exactly the critical maximal-value map. The nonlinear deviation recurrence is an algebraic restatement of the original update, not a linearization. Its ordered half-plane is invariant by explicit numerator factorizations. The larger deviation decreases strictly within two steps unless it is already zero; compactness proves convergence to the origin. At sufficiently small amplitude the transverse relative gap grows by at least \(39/32\) per step outside the passive wedge, forcing finite entry. A separate rational identity proves that the entire nonlinear wedge is forward invariant. The exact two-step recurrence and summable relative errors prove convergence to positive rescaled amplitudes, not just a rate guessed from linearization. On the invariant diagonal the reciprocal recursion is solved exactly. A pure-Python rational checker tests the nonstandard identities and boundary cases. No infinite assertion is inferred from finite enumeration.

**Originality (PASS under the inspected evidence).** Satur [1, Sections 3.2 and 5.2] proved global collapse and recorded \(3/4\) as a numerical/leading-order prediction, but explicitly did not prove the sharp rate for the nonlinear map. The present finite-entrance mechanism, exact invariant nonlinear wedge, and positive parity-resolved amplitude limits are not in that source. Simpson [2, Sections 1 and 3] provides general exponential-stability criteria for homogeneous approximations but does not directly imply either this exact rate or a two-phase limit for the particular piecewise rational map. Semantic and formula-based literature comparisons did not reveal an equivalent theorem; the possibility of an unindexed proof or an overlooked conjugacy remains.

**Mathematical value (PASS).** The main source explicitly left quantitative global collapse at its unique border-collision threshold as a problem beyond its qualitative theorem and numerical rate. Establishing the exact rate for **all** asymmetric initial states, with the exceptional diagonal rate and nontrivial limiting two-phase amplitudes, distinguishes full nonlinear orbit behavior from a heuristic linear approximation. The exact invariant wedge supplies a structural dynamical mechanism rather than a generic perturbation estimate.

**Scientific boundaries and risk.** The rate law is only for \(\alpha=2\), and phase/amplitude constants are implicit convergent limits. Dynamics of coordinate labels at a tie are not classified. Similar general exponential-stability literature is not regarded as a model-specific sharp amplitude theorem; unindexed equivalents remain possible. Independent assessment has not occurred.

## References

[1] O. R. Satur, *From oscillations to symmetry breaking in a two-dimensional piecewise-smooth dynamical system*, arXiv:2611.13318v1 (2026-11-09), Theorem 2 and Section 5.2, https://arxiv.org/abs/2611.13318.

[2] D. J. W. Simpson, *The stability of fixed points on switching manifolds of piecewise-smooth continuous maps*, arXiv:1612.02932v1, https://arxiv.org/abs/1612.02932.

Self-review: passed. Independent audit: not yet performed.
