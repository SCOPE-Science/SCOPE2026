# Independent audit — 2026-10-01

## Record

A single weakly Stalnakerian frame already has non-arithmetical validity

## Final claim

For the explicit weakly Stalnakerian frame \(\mathfrak F_*\) with \(W=D=\omega\), universal accessibility, constant domain, and the least-point-at-or-above selection function, every closed arithmetic sentence \(\alpha\) satisfies \(\mathbb N\models\alpha\) iff \(\mathfrak F_*\Vdash AX\to\alpha^*\); the same holds for every class \(\mathcal K\) with \(\mathfrak F_*\in\mathcal K\subseteq WS\), so all these validity sets are non-arithmetical.

## Correctness

**PASS** — The selection function satisfies Success, Weak Centering, Uniqueness, and Uniformity; the empty-selection case in Uniformity is harmless. For true arithmetic, the source theorem gives validity of \(AX\to\alpha^*\) on every weakly Stalnakerian frame, hence on \(\mathfrak F_*\) and every subclass of \(WS\). For false arithmetic, the source's explicit model on exactly this underlying frame satisfies \(AX\) at world \(0\) and interprets standard arithmetic, so it falsifies the translated sentence there. The sandwich statement follows immediately. The computable translation then transfers non-arithmeticality of true arithmetic to each validity set.

Risk: The conclusion is only for closed arithmetic sentences and proposition-based set-selection semantics, exactly as stated.

## Originality

**FAIL** — The 2026 Kocurek–Walsh–Weiss primary paper was obtained in full and inspected. Its Theorem 1 states \(\mathbb N\models\alpha\) iff \((AX\to\alpha^*)\in L(WS)\). In the converse proof it then defines exactly \(W=D=\omega\), \(d(w)=D\), \(R=W^2\), and the least point of \(X\) not below \(n\) as the selection function, and uses that model at world \(0\). Therefore the fixed-frame biconditional follows immediately by combining the theorem's forward direction with the very countermodel used in its reverse direction. The intermediate-class sandwich is then an immediate monotonicity corollary. This is direct prior implication, not merely title overlap.

Risk: No priority uncertainty remains on the decisive source comparison; the exact frame and both directions needed for the localization are in the prior primary text.

### Equivalent formulations

Combining the published forward theorem with its own fixed countermodel is exactly the audited fixed-frame biconditional.

### Broader coverage

These two published components dominate the localization and all intermediate-class sandwich cases.

### Exact database or table

No numerical table is relevant.

### Claim versus prior implication

The final claim is an immediate corollary of prior theorem-plus-proof and therefore covered.

## Value

**FAIL** — The underlying arithmetic interpretation is mathematically substantial, but the submitted record's incremental claim is a routine localization of that already published proof: it packages the source theorem together with the source theorem's own explicit countermodel and then applies class monotonicity. Under the value bar, that is a mechanically implied corollary rather than a separate motivated mathematical gap.

Risk: This value judgment concerns the incremental record, not the importance of the source theorem.

## Source inspections

- **Stalnaker's Logical Problem of Conditionals is Unsolvable** (arXiv:2608.07387v1): Complete 14-page primary text; especially Theorem 1 and its converse construction on W=D=omega with universal accessibility and the least-at-or-above selection function Assessment: COVERING. Evidence: Theorem 1 gives the WS arithmetic biconditional; its converse uses exactly the audited fixed frame. The fixed-frame equivalence and intermediate-class sandwich follow immediately from those same proof components.

## Residual risks

- No residual source-access risk affected the disposition.

## Disposition

Failed: the submitted claim does not survive all three axes and is preserved as a failed attempt.
