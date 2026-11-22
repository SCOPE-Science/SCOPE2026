# Review of area-weighted LAB concentration

**Correctness: PASS.** Each area-weighted path is the unique descendant containing an area-uniform point; the angle-bisector theorem and sine rule yield the uniform conditional branch lower bound. The verified minimum-angle lemma and strict two-step projective Lyapunov decrement, combined with compactness, yield a positive decrement for each fixed distance threshold. Disjoint pair indicators stochastically dominate independent Bernoulli variables and imply the stated finite-depth inequality; no finite experiment is substituted for this proof.

**Originality: PASS within inspected evidence.** Michaud's arXiv:2611.06492v1 proves the deterministic switch criterion and equal-count concentration and explicitly lists area-weighted sampling as unproved. Ismailescu et al. (arXiv:1908.02749) give geometric nondegeneracy but not distribution of area-weighted descendant shapes. The published-finding corpus mixed-block contraction work addresses an equal-count family rather than actual geometric areas. Equal-count estimates alone do not bound a tilted area-weighted law, because a small exceptional count may carry significant total area. The new ingredient is a uniform conditional area probability and a stochastic domination bound. Previous unindexed work remains a priority risk.

**Value: PASS.** Physical area, unlike equal node count, measures how much of the refined mesh retains exceptional geometry. The recent motivating article explicitly asks whether the statistical regularization persists under area-weighted sampling. This theorem answers that precisely for complete unconstrained refinement and gives a usable finite-level tail rather than merely asymptotic weak convergence. It does not extend to adaptive pruning or conforming completion.

**Limitations:** Rates are initial-shape dependent, the decrement is defined by a compact minimization, and the bound is not claimed optimal. The critical projective Lyapunov theorem is prior work, not a newly certified result. No independent mathematical audit was performed.

Self-review: passed. Independent audit: not yet performed.
