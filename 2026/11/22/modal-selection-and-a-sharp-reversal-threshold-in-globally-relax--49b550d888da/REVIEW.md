# Scientific review

## Correctness — PASS

The increment-relaxation quadratic has a unique nonzero positive root because each active \(0<x_j^2<12\) gives \(q_j>0\), \(g_j>0\). Direct expansion of the RK4 polynomial proves the exact energy map, global norm invariance, and the strict weighted-energy Lyapunov identity. The bounded monotone energy of minimum-\(g\) modes forces \(\gamma_n\to g_*\), which in turn forces all other energies to zero. The two-mode threshold follows from an explicit quadratic whose endpoint signs are opposite and whose leading coefficient is positive. A separate direct RK4-stage implementation and rational tests corroborate the algebra; finite tests do not replace the analytic argument. Risks: none identified within exact-arithmetic hypotheses; nonlinear, adaptive-step and inexact-solve cases are outside scope.

## Originality — PASS (qualified)

Compared against the accessible full text of Doehring–Ranocha–Torrilhon (arXiv:2507.04991), Ranocha et al. (2020), prior relaxation methods, and the full claim and proof of the closely related 2026 published projected-RK4 modal-reversal result. Ketcheson (2019), §4.1, already specifically studies this RK4 relaxation on Fourier modes and explicitly reports finite-time modal amplification and attenuation; those are **not** new. His analysis does not give the complete infinite-time selection, strict frequency Lyapunov law, or the sharp two-frequency reversal. The projected-RK4 work instead establishes a **different** radial-endpoint modal ratio; neither published statement implies the new increment-relaxation winner law or its sharp root. The exact opposite-winner benchmark exhibits non-equivalence. Semantic searches checked aliases such as global energy correction, relaxation RK4 modal transfer, frequency selection and quadratic entropy, including published published-finding corpus findings and this topic's accessible historical records. Residual risk: older equivalent special-case formulas or global-conservation modal analysis may exist under other terminology, and this is not a claim of independently verified historical priority.

## Value — PASS

Conserving a global invariant can conceal severe false internal dynamics: independently conserved physical modal actions can be driven asymptotically to zero except for selected frequencies. The precise frequency selection, sharp step boundary, and opposing outcomes between two energy-conserving methods offer a diagnostic for reliable conservative time integration. The result holds for any finite collection of independent linear modes, not just an isolated scalar counterexample. It does not establish a runtime improvement, a general error bound, or a theorem about optimized multirate tableaux.

Self-review: passed. Independent audit: not yet performed.
