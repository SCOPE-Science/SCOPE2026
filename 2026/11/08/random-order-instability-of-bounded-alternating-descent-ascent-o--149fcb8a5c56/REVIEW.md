# Scientific review

## Correctness (PASS)

The two update matrices follow from the stated sequential gradient semantics. Their positive quadratic invariants prove power boundedness for the two nonrandom orders when \(0<t<2\). Exact multiplication proves balanced conditional Euclidean energy growth. The symmetric second-moment transfer has \(\det(I-L_p)=-8p(1-p)t^6\), so its spectral radius exceeds one for every interior bias. A positive-definite Perron matrix of the adjoint transfer, obtained via the resolvent and the absence of a common real invariant line, produces the quantitative lower bound for **every** nonzero deterministic initial vector. The symbolic and rational checker verifies the critical algebra. This is a mean-square, not almost-sure, statement.

## Originality (PASS, with residual risk)

Fixed-order alternating Gauss--Seidel descent--ascent results in Zhang and Yu (2019/2020) and Zhang et al. (2021) do not state any mean-square analysis of randomized full-sweep order. Sebbouh et al. (2021) randomize whether to execute **one** of the two player updates, not the orientation of a full two-player sweep. Nan et al. (2025/2026) investigate deterministic alternating schedules and ergodic guarantees. The finite-dimensional exact all-bias classification and exact fair quadratic growth law are not implied by those statements. General matrix-product instability is classical, and an unknown specialist result on random symplectic Euler compositions remains possible; this review does not certify absolute novelty.

## Value (PASS)

The concrete methodological gap is whether randomly rotating the order of two individually stable gradient substeps preserves long-time boundedness. The answer is sharply negative for **every nontrivial mixing bias** at **every elliptically stable normalized step**, with an exact fair-mixing growth rate. This identifies a practically interpretable order-randomization risk for saddle-point algorithms and a self-contained test case for proposed randomized symplectic/alternating integrators. The result is not merely the known statement that simultaneous descent--ascent diverges: every realized sweep here is one of two individually power-bounded alternations.

## Scientific limitations

The result is confined to the two-dimensional bilinear game and fixed independent full-sweep ordering, and does not imply almost-sure divergence or divergence in regularized games. Specialist overlap is still possible. External validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
