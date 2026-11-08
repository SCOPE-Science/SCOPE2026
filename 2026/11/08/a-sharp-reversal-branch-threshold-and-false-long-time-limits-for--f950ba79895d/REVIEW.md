# Mathematical review

## Correctness

PASS. Direct substitution into the source's exact positive-root SAV-BE equations yields \(r_{n+1}=r_n/\sqrt{1+\tau a^2\phi_n^2/S_n^2}\). The unshifted recurrence has an exact geometric auxiliary sequence and an exact negative-branch sum, with the sharp branch threshold following from a quadratic inequality in \(q\). The strictly positive-shift example follows from the exact first step, \(r_{j+1}<r_j/10\) and the convergent upper bound \(150\sum_{j\ge2}10^{-j}=5/3\), closing a global induction. The supplied checker passed, but finite computations are supporting evidence only.

## Originality

PASS, with historical-priority uncertainty. The 2026 source proves auxiliary positivity and modified-energy stability, not convergence to the physical equilibrium; it also does not classify the scalar first-reversal branch. The 2024 weighted-SAV paper recognizes large-step energy mismatch, but its discrete equation differs and does not imply the two quantified assertions. The June 2026 pullback-corrected SAV work concerns a modified operator. Related published-result searches found no source implying this particular exact threshold and robust nonstationary limit; an inaccessible relevant full text remains a residual risk.

## Value

PASS. The issue is a direct long-time fidelity question for an explicitly proposed unconditionally stable positive-auxiliary method, not an artificial statistic. The example demonstrates a substantive distinction between positivity, modified-energy dissipation, and convergence to the unique minimizer even under strong convexity. The exact threshold explains the failure mechanism, while the positive-shift interval removes a singular-case artifact. It helps delimit what guarantees can be inferred from unconditional energy stability.

## Scope and closest literature

The main comparison is the complete original SAV-BE formulation of Huang–Liu–Wang–Yan (2026), equations (3.2)–(3.8). Huang–Jiang–Yang–Yuan (2024) recognizes the general modified-versus-physical energy issue under a different auxiliary update. Zhang–Shen (2026) proposes pullback corrections and was available only through the abstract. The result does not contradict theorems asserting only positivity, modified-energy stability, or fixed-horizon small-step convergence. The unshifted branch classification applies to nonzero iterates; the fully nonsingular theorem uses positive \(C\).

Self-review: passed. Independent audit: not yet performed.
