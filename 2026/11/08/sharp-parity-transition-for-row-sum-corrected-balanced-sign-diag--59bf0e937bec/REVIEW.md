# Scientific review

## Correctness — PASS

For each permutation-invariant sign law, the identity for the squared sign sum gives the attainable correlation range and the exact even/odd minimum. Algebraic variance calculation uses only sign squares and pair correlations; it requires no unsupported independent-coordinate fourth-moment factorization. The explicit derivative is positive for any nonzero off-diagonal matrix, proving optimality within the stated family. Rowwise Cauchy--Schwarz proves the complete zero-risk classification, and an exact comparison with iid signs including the all-ones matvec proves the sharp budget thresholds. The standalone exact-rational finite consistency checker passed 1,423 assertions after extraction; the infinite-dimensional statement rests on the written proof, not testing.

## Originality — PASS, with residual precedent risk

Accessible primary full texts of Baston--Nakatsukasa (2022), Hallman--Ipsen--Saibaba (2022), Dharangutte--Musco (2022) and Epperly--Tropp--Webber (2023) were compared at the level of estimator formulas and assumptions. They contain iid-coordinate probing, concentration guarantees, Diag++ or a low-rank leave-one-out XDiag construction, rather than the exact fixed-sum-sign plus known-row-sum affine design and all-dimensional parity classification. The closest indexed related result concerns AdaHessian's iid diagonal variance; it does not cover exchangeable fixed-sum probes. No exact implication was found from the inspected prior results, although older unindexed sampling-without-replacement and probing sources could contain equivalent reductions. Negative searches are not proof of uniqueness.

## Value — PASS

This solves a natural constrained estimator-design problem with a complete attainable-law classification, sharp even/odd zero-variance boundary, and practical query-budget caveat. It explains how a dense class of constant-coupling matrices can be recovered exactly by two matrix--vector products in even dimensions, and why odd parity forbids the same cancellation. The result neither asserts universal superiority over modern diagonal estimators nor ignores the cost of the deterministic query.

## Closest literature and limits

Baston--Nakatsukasa, arXiv:2201.10684; Hallman--Ipsen--Saibaba, arXiv:2202.02887; Dharangutte--Musco, arXiv:2208.03268; Epperly--Tropp--Webber, arXiv:2301.07825, especially §2.4. The result is restricted to exact matvecs, exchangeable within-vector sign laws, universally unbiased affine correction and squared Euclidean risk; exact precedence in unindexed finite-population sampling literature remains unverified.

Self-review: passed. Independent audit: not yet performed.
