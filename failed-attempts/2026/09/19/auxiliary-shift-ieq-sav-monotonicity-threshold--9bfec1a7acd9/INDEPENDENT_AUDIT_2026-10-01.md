# Independent mathematical audit — SCOPE-20260919-9bfec1a7acd9

Final disposition: **FAILED**.

## Correctness
**PASS** — The homogeneous recurrences were reconstructed from the displayed IEQ and SAV equations. With C0=V c/epsilon^2 and r=(sqrt(V)/epsilon)q the two updates coincide. Independent symbolic algebra verifies the rational first iterate, its positive derivative in c, the displayed overshoot threshold, its negative derivative, and the critical-shift formula. The sign of the second increment follows from the positive source scaling factor and u1>0. The stored numerical script is therefore corroborative rather than load-bearing.

## Originality
**FAIL** — The audited package itself identifies the rational first-step expression and the two IEQ/SAV large-step threshold formulas as formulas from Li-Wang, and its remaining claims are obtained by a direct rescaling, differentiation, and solving u1=1. The primary abstract confirms that Li-Wang already establish wrong-signed IEQ and SAV increments for the same Allen-Cahn model. Under an implication-based originality standard, the normalized phase diagram is a routine algebraic corollary of the published scheme formulas rather than an independent theorem. Verified full text of the very recent source was unavailable after arXiv/OA and authorized retrieval attempts, but this rejection does not rely on a negative full-document search.

### Equivalent formulations
The claimed conjugacy and phase boundary are equivalent to elementary normalization and root finding in the source recurrences.

### Broader coverage
The inspected/source-attributed formulas already contain the information from which the final phase diagram follows mechanically.

### Exact database or table
Database absence cannot establish originality when the source-formula implication is decisive.

### Claim versus prior implication
The final claim is a direct corollary of prior formulas, even if the source did not package those consequences as a separate theorem.

## Value
**FAIL** — The calculation is a useful numerical-analysis diagnostic, but the scientific payload is a change of variables plus elementary differentiation of an already published first-step/threshold formula. It does not add a nonstandard lemma, new stability mechanism, or independently motivated exact invariant beyond that immediate parameter sensitivity, so it does not clear the value bar.

## Source inspections
- **Pointwise Monotonicity of the Allen--Cahn Flow and Dynamical Limitations of Energy-Stable Schemes** (https://arxiv.org/abs/2609.19023): primary abstract; arXiv HTML failed and authorized full-text retrieval returned no verified PDF Assessment: PRIMARY_SOURCE_SCOPE_CONFIRMED_FULL_TEXT_UNAVAILABLE. Evidence: The abstract explicitly states that IEQ and SAV schemes admit monotone data with large-step wrong-signed increments.
- **Assigned source package** (https://github.com/SCOPE-Science/SCOPE2026/tree/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/19/auxiliary-shift-ieq-sav-monotonicity-threshold--9bfec1a7acd9): complete RESULT.md and verification script/output Assessment: FORMULAS_EXPLICITLY_ATTRIBUTED_TO_SOURCE_AND_ALGEBRAICALLY_REPRODUCED. Evidence: RESULT.md calls the rational u1 expression the source paper's first-step expression and says the source reports the IEQ/SAV threshold formulas separately.

## Residual risks
- The full Li-Wang text was not available through the lawful routes tried; a later source revision could alter formula provenance.
- No correctness defect is asserted; rejection is for originality/value.
