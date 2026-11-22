# Scientific review: Pell polynomial-weight exponentials

## Correctness — PASS

The mathematical proof applies the integer-weight Dold–Euler criterion to the exact Pell recurrence. An integral companion-matrix trace and the identity \(8U_n^2=V_{2n}-2(-1)^n\) handle all odd primes. The identity \(U_{2n}=U_nV_n\) and \(V_n\equiv2\pmod4\) give exact dyadic valuations; quadratic-inert Frobenius primes force even polynomial weights. An explicit Binet factorization gives rational powers, and odd valuation at a noncolliding spectral pole proves the algebraic-degree lower bound. Non-even weights have an irrational logarithmic residue, contradicting algebraicity. The packaged exact checker passed 2,917 tests and seven coefficient expansions through degree 36; these are auxiliary tests and not the basis of the proof.

## Originality — PASS, qualified

The November 12, 2026 Fibonacci article proves an analogous *different recurrence* and does not state these Pell conclusions (full HTML §§1–4 read). OEIS A208034 records the Pell square case and three all-power conjectures, not a proof of them; the directly retrievable page was indexed search text and direct page access was denied. The general Minton trace-sequence classification, as summarized in the full open-access Byszewski–Graff–Ward survey, is a general criterion, not the exact all-polynomial Pell classification or its algebraic-degree formula. Existing closely indexed Pell local Dold studies use prime parts or index-substituted sequences, not these polynomial weight powers. Relevant earlier work on Fibonacci polynomial weights and algebraic degrees concerns a different recurrence. A possible implicit specialization of earlier general trace theory, or an unindexed proof of the OEIS conjectures, is a remaining risk.

## Mathematical value — PASS

The statement settles three explicitly recorded infinite families of Pell power-series conjectures, upgrades them to an if-and-only-if classification of *all* integer polynomial weights, and determines a genuinely varying exact algebraic-degree spectrum. The dyadic congruence condition permits nontrivial cancellations, for example \(T^4-T^2\), so it is not only a separate-monomial multiplier statement. The result makes no claim about arbitrary Lucas recurrences, coefficient asymptotics, or externally certified correctness.

Self-review: passed. Independent audit: not yet performed.
