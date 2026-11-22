# Scientific assessment

## Correctness — PASS

The claim is fully quantified for every real \(\alpha>2\) and every off-diagonal interior initial condition. The proof derives the exact reciprocal-odds branch formulas from the original piecewise-max update; proves order preservation with \(R_xR_y>1\); shows finite branch entry by a concrete \(3/2\)-growth estimate; proves permanent switching by an explicit strict inequality; and gives a two-step contraction via divided differences of the log-odds map. The intermediate-value coefficient bounds apply simultaneously to the orbit and to the fixed point. Supporting exact rational and numerical tests are reproducible in `CHECK.py`. They do not purport to prove the infinite statement.

## Originality — PASS within inspected evidence

The original map and the location/local stability of its off-diagonal fixed points belong to Satur, arXiv:2611.13318v1, Theorem 3. The same source expressly records the rigorous supercritical global-attraction problem as open; its large numerical experiments are not a proof. The nearest published-finding corpus finding concerns nonlinear decay at the disjoint critical parameter \(\alpha=2\), and searches for supercritical global attraction and odds-coordinate contraction returned no implication of the theorem. Accessible claim records for this research topic showed no matching result. Equivalence under odds/log-odds coordinates and the possibility of a stronger general theorem elsewhere remain residual historical-priority risks. This status does not represent independent literature certification.

## Mathematical value — PASS

The result closes an explicitly stated dynamical gap for a natural and recently introduced border-collision model. It converts a numerical basin conjecture into a deterministic all-orbit theorem, supplies finite switching-time control, and establishes a uniform parameter-dependent post-entry contraction rate. The scope is structural, not a selected finite computation, a textbook restatement, or a trivial improvement to existing local stability.

## Boundaries

The invariant diagonal and the critical/subcritical parameter ranges are excluded; the contraction bound is not claimed optimal. The checker is supporting evidence only. Independent verification and historical-priority assessment remain outstanding.

Self-review: passed. Independent audit: not yet performed.
