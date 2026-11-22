# Scientific review

## Correctness — PASS
The target, two orderings, metric, parameters and equality cases are specified exactly in `RESULT.md`. The proof reduces the problem to the common two-dimensional invariant span, proves equal squared Frobenius norms through equal trace/determinant, derives the exact signed difference through a direct projector polynomial calculation, and proves the rate sign with strict monotonicity of the hyperbolic cotangent expression. Symbolic, rational and numerical checks in `verify.py` independently exercise the critical identity and do not substitute for the analytic argument.

## Originality — PASS, with residual historical uncertainty
The defining claim is an exact for-all-positive-steps signed Frobenius-error comparison of **two reversed symmetric Strang compositions** of arbitrary noncommuting rank-one orthogonal dissipators. The inspected full text of Blanes–Iserles–Macnamara studies positivity-preserving splittings without presenting this projector-specific ordering formula. Classical Strang consistency does not determine the sign of two leading error constants or the exact global sign. The closest located published finite-state comparison instead concerns a directed-cycle Lie-versus-Strang **stationary total-variation** error; another concerns exact two-state three-factor splittings, whose one-dimensional dissipator geometry does not imply a strict two-projector result. Searches by aliases, order reversal, rank-one projectors and Frobenius norm found no exact broader claim in reviewed sources. A historical-priority risk survives because exhaustive older projector-product literature was not inspected.

## Value — PASS
Ordering otherwise identical symmetric three-factor schemes changes finite-step accuracy for noncommuting dissipators. The exact sign law gives an actionable choice at **every** step length for an important minimal reversible heat-transfer problem, rather than a small-step heuristic. The equality and strictness cases show when order choice does and does not matter. The result does not claim universality beyond the Frobenius metric, rank-one projectors or one-step comparison.

## Independent assessment and limitations
No independent proof audit or exhaustive historical-priority certification was performed. The supplementary numerical tests sample finitely many parameters; the proof supplies the continuum statement.

Self-review: passed. Independent audit: not yet performed.
