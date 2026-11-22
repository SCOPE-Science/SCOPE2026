# Scientific review

## Correctness — PASS

The explicit Bernstein expansion of the jump responses follows by composing the polynomial averaging operator at its own grid nodes. Strict monotonicity of the binomial upper tail ensures exactly one positive Bernstein derivative coefficient, so Descartes' rule and endpoint-sign/mean-value arguments rigorously classify every real critical point, for arbitrary degree. The variation norm is exactly the maximum response to a single nodal jump because arbitrary nodal data decompose telescopically into jumps. For the boundary jump, Poisson limits for both the response and its rescaled derivative, combined with its unique critical point, prove the maximizer location and limiting overshoot. Exact arithmetic and root-finding replay supplement rather than substitute for these infinite-degree arguments. A potential risk is silently extending the boundary-jump limit to globally maximizing jumps; the finding explicitly does not do so.

## Originality — PASS (historical priority qualified)

Full lawful texts examined: Raşa (2006) develops semigroup/Boolean-sum convergence rates, while Draganov (2014) develops smooth simultaneous approximation bounds. Neither examined statement gives the all-degree step-response critical-point theorem, the sharp BV operator reduction with algebraic prescription, or the explicit microscopic boundary overshoot. Published mathematical literature and available related result descriptions were searched for Bernstein Boolean combinations, their aliases \(2B_n-B_n^2\), BV norms, step profiles and Gibbs-type boundary effects; nearby results concern different Bernstein smoothing operators or different functionals. Later strong-converse papers by Cheng–Zhou (2019) and Draganov (2022) concern continuous-function approximation in the uniform norm and do not establish the discontinuous-step BV norm (the 2022 main theorems were inspected in the open full text). Most relevant unresolved sources: Agrawal–Kasana (1984) and Gonska–Zhou (1994), for which full texts were not available. Therefore the priority comparison is reasoned but not an exhaustive literature guarantee.

## Mathematical value — PASS

Accelerated Bernstein Boolean sums are used to improve approximation order for smooth data, but the resulting operator is no longer positive. The proved oscillation rigidity and exact step reduction clarify the associated variation-stability cost in a classical method for every degree; the nonzero and explicitly located boundary-layer overshoot shows why smooth-approximation acceleration does not guarantee monotonicity or BV stability. The two-extremum classification and the limiting profile require substantive sign-variation and asymptotic analysis, not merely a low-degree calculation.

## Closest sources and limits

- Raşa (2006), https://doi.org/10.33993/jnaat351-1018: full text, semigroup-related Boolean-sum rate estimates, not BV jump amplification.
- Draganov (2014), https://doi.org/10.1007/s00025-014-0389-z: lawful author manuscript read, weighted simultaneous rates, not the stated sharp variation result; online publication verified 20 May 2014.
- Draganov (2022), https://doi.org/10.24193/subbmath.2022.3.10: open full text inspected, theorem statements concern uniform approximation and K-functionals, not BV step instability.
- Cheng–Zhou (2019), https://doi.org/10.24193/subbmath.2019.3.01: abstract and theorem description concern strong approximation inequalities; full text not inspected.
- Agrawal–Kasana (1984), https://doi.org/10.1515/dema-1984-0320, and Gonska–Zhou (1994), https://doi.org/10.1016/0377-0427(92)00133-T: relevant early references without full-text comparison, retaining historical-priority risk.
- For the global norm, only an exact finite-degree root characterization and a first-jump asymptotic **lower bound** are proved; a global asymptotic is not asserted.

Self-review: passed. Independent audit: not yet performed.
