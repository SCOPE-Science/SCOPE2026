# Scientific review of the squared-cobalancing GCD formula

## Correctness

**PASS.** The formula is asserted for all integers \(k\ge1\). The proof first represents the cobalancing sequence as \(b_n=(P_{2n-1}-1)/2\) and turns sliding-window GCDs into an initial sum and a periodic-difference GCD. The latter is computed exactly using two integral fourth-order recurrences with invertible constant term and explicit first-four-term Bézout reductions. A telescoping Pell identity calculates the initial sum. Odd primes reduce to the congruence \(64S_k(0)\equiv5k\pmod{D_k}\). The difficult power of two is determined by a proved dyadic shift lemma, not by numerical inference. The stand-alone checker independently tests \(500\) window lengths, \(6{,}000\) shifted windows, \(6{,}000\) shifted differences, and the dyadic lemma. Finite testing is corroborative; the full proof is symbolic and unconditional.

## Originality

**PASS, subject to bibliographic uncertainty.** Mbirika--Schrader--Spilker (2023), Section 6.1, Question 30, explicitly ask for closed forms for sums of consecutive **squares** of cobalancing numbers and record only the factor-of-four divisibility. The published paper was materially inspected, including Definitions 6--7, Convention 1, Section 5, and Section 6.1. Its exact results for first powers and the partial Pell-square formulas do not imply the new formula for all cobalancing-square windows. Mbirika--Spilker (2022), materially inspected at its introduction and principal generalized-Fibonacci statement, treats recurrence \(G_{n+2}=G_{n+1}+G_n\), not the affine cobalancing sequence; it does not subsume this result. Actual focused searches of academic sources and published mathematical research records did not identify an equivalent or stronger theorem. The authors mention a possible future proof for Pell-square results, but no accessible later theorem resolving the **cobalancing-square** case was found. A matching result in unindexed literature remains possible. Lack of retrieval is not treated as novelty proof.

## Value

**PASS.** The result gives an exact all-parameter answer to one branch of a named, still-open-in-the-inspected-paper problem. The formula is genuinely arithmetic: the factors \(2\) and \(7\) in the difference GCD, the final exceptional factors of \(5\), and exact valuation at \(2\) cannot be inferred from the original \(4\mid \mathcal B_2(k)\) observation. Its finite GCD of two explicit natural Pell quantities is computationally usable and replaces the original infinite-shift definition. The theorem does not solve the other branches of Question 30, and does not assert a general formula for arbitrary affine recurrences.

## Closest literature and verification risks

1. aBa Mbirika, Janee Schrader, Jürgen Spilker, *Pell and Associated Pell Braid Sequences as GCDs of Sums of k Consecutive Pell, Balancing, and Related Numbers*, Journal of Integer Sequences 26 (2023), Article 23.6.4, arXiv:2301.05758, particularly Section 6.1, Question 30.
2. aBa Mbirika and Jürgen Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, Fibonacci Quarterly 60 (2022), 255--269, arXiv:2204.12626.

A direct arXiv-version PDF retrieval attempt was unsuccessful; the complete journal PDF of the same work was available and inspected. The remaining risk is undiscovered equivalent literature, not a gap in the argument. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
