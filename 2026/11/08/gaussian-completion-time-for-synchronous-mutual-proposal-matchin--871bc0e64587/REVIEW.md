# Scientific review

## Correctness

**PASS.** Exact ordered disjoint-pair counting yields factorial moments. The resulting one-step conditional mean and variance agree with independently enumerated rational proposal distributions for all states tested. The probability of a nonzero matching in any nonterminal state is uniformly at least one eighth, so the total finite-population drift has logarithmic first and second moments. A stopped square-integrable martingale gives the expectation and asymptotic variance; its predictable variance tends to \(2n\) and uniform exponential moment bounds imply Lindeberg, proving the Gaussian limit. An analogous functional martingale argument proves the preterminal Brownian trajectory. The verifier passed 1,838 exact finite tests, which do not replace the asymptotic proof.

## Originality

**PASS, with historical-priority risk.** The October 2026 source studies the same rule on sparse Erdős--Rényi graphs and leaves other densities and the endgame open; its theorems do not imply a complete-graph absorption-time CLT. Métivier--Saheb--Zemmari's 2003 result gives a one-round Poisson approximation on complete graphs, not a many-round stopping-time CLT. The closest mathematical-record findings concern other matching optimizations and random greedy independent sets rather than this repeated uniform rendezvous chain. A related 2017 thesis could not be inspected in its relevant chapter; this uncertainty is explicitly retained and independent priority verification is needed.

## Mathematical value

**PASS.** The full-completion time, its leading variance, and fluctuations are natural invariants for a matching algorithm. The source explicitly asks about its behavior at other graph densities and after a constant fraction has been matched. A complete graph, though maximally dense, requires linearly many rounds here, in striking contrast to the polylogarithmic constant-fraction result on the sparse random graphs of the motivating paper. The result supplies a rigorous Gaussian terminal law and a path-level fluctuation description for this distinct regime.

## Closest literature and limitations

Vishvajeet N and Shrinidhi Teganahally Sridhara, arXiv:2610.25507 (2026); Métivier, Saheb and Zemmari, *Information and Computation* 184 (2003), Section 6.2; Nesrine Ouled Abdallah, related 2017 thesis (relevant full chapter unavailable). The result assumes a complete residual graph and fresh simultaneous independent proposals; it does not establish behavior for intermediate edge densities. Historical originality remains provisional pending independent literature assessment.

Self-review: passed. Independent audit: not yet performed.
