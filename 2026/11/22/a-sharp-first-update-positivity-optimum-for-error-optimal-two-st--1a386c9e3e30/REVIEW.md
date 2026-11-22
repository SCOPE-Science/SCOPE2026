# Scientific review: a sharp first-update positivity optimum

## Correctness — PASS
The source coefficients lead directly to a positive-denominator first-output numerator \(F(z,\kappa)\). An analytic upper bound makes \(F\) strictly decreasing in the dimensionless step, while its strict concavity in \(\kappa\) creates one interior optimizer. The envelope decreases and crosses zero only once, proving uniqueness of both sharp constants; the BDF2 crossover is an exact factorization. The standalone arithmetic checker successfully exercised coefficient consistency, the recurrence identity and finite brackets. These computations are diagnostics, not infinite proofs.

## Originality — PASS, qualified
The original Jensen–Lóczi–Ketcheson formulas and the classic starting-procedure positivity framework are prior work. The closest indexed published published-finding corpus results address **all-iterate** positivity for the same method or a different starting procedure. The claim here concerns the **first completed output from exact scalar-decay data** and specifically the unique optimizer and BDF2 crossover for that different objective. Those values and the full local frontier were not found in accessible records. The complete texts of the closely related published-finding corpus records were inaccessible and remain a priority risk; absence of indexed matching values is not proof of global novelty.

## Value — PASS, limited
An exact first-output positivity margin matters as a finite diagnostic for a stiff method, yet can mislead users about enduring nonnegativity. The computed optimum occurs at \(\kappa\approx0.36687\), distinct from the published optimal robust all-iterate value \(1/2\). For the high-damping case \(\kappa=0.8\), a first positive update is possible at dimensionless steps nearly three times the robust all-iterate ceiling. No general accuracy, robustness, or long-time improvement is asserted.

## Relationship to prior literature and limitations
See `RESULT.md` and `AUDIT.json` for exact comparisons and the source-inspection record. The result is restricted to a single scalar linear ODE, a specific error-optimal two-step family, an exact positive start and the first new output. The full-text access restriction on closest published same-family records remains material.

Self-review: passed. Independent audit: not yet performed.
