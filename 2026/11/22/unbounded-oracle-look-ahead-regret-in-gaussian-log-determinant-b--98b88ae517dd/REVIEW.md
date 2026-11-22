# Self-review

## Correctness — PASS

The claim is an all-parameter theorem for any fixed rational rank fraction and any fixed integer per-probe budget at least two. Integer ranks and costs follow from choosing the rank divisible by the square of the denominator. The Frobenius and logarithmic look-ahead inequalities are strictly positive by exact tail counts and elementary logarithm bounds. Gaussian quadratic-form unbiasedness and the exact second moment give both full-budget risks; minimal polynomial degree two justifies quadrature exactness. The checker independently tests 27,860 finite equalities and inequalities, but the universal quantifiers and diverging limit rest on the written proof.

## Originality — PASS, with residual priority risk

The motivating preprint's variance identities, two-rank heuristic, its conservativeness remark, and empirical incorrect choices are explicitly credited. Its full mathematical Sections 2 and 4 do not present the every-fraction construction, the unbounded full-budget regret, or failure of the *exact logarithmic* short-rank predictor. A separately inspected public ideal-allocation theorem determines the global optimum using the full-budget spectrum but does not assess the shorter-rank predictor. Earlier published adaptive Hutch++ and randomized matrix diagnostic results provide other allocation guarantees rather than this exact implication comparison. Unindexed equivalent counterexamples remain possible; absence from searches is not proof of publication priority.

## Value — PASS

The result distinguishes two different limitations that are easily conflated: distortion caused by a Frobenius surrogate, and structural extrapolation caused by evaluating the choice at reduced rank. Eliminating the first source of uncertainty does not control the second. The effect persists for the paper's recommended rank fraction, for exact two-step quadrature, and for near-identity positive-definite systems. Thus the theorem is a motivated adversarial benchmark for designing more reliable budget-allocation checks, not an arbitrary numerical slice.

## Limits

This is an exact worst-family lower bound for the ideal deterministic choice; the practical random Nyström diagnostic is not analyzed, and neither independence from prior publications nor independent proof verification is asserted.

Self-review: passed. Independent audit: not yet performed.
