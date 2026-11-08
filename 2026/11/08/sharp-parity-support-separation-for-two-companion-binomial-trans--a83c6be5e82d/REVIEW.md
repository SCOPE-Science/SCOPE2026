# Scientific review — sharp parity-support separation for two companion binomial transforms

## Correctness — PASS

The two foundational run-length-transform identities are published in Rampersad–Wiebe, Theorems 13 and 14. Starting from their respective base-sequence initial vectors, the parity recurrences are independently reconstructed: in characteristic two the fourth-order recurrence immediately yields period five. The allowed one-run residue classes are therefore exact for every nonnegative argument. The binary-word decomposition is bijective (initial zeros, complete run/positive-zero blocks, optional final run). It produces the rational count generating functions without asymptotic assumptions. For each denominator, coefficient positivity, a degree-one term, and the strict positive derivative condition establish one simple dominant positive pole, yielding the leading constants and exact exponents. The universal bound for arbitrary cutoffs follows from dyadic sandwiches. This proves all quantified conclusions, including zero natural density, without extrapolating finite data.

A standalone executable reconstruction of both integer binomial sums used Lucas's bit test, comparing direct values and word predicates for \(0\le n<1024\). Exhaustive word counts through 14-bit words match the generating function coefficients. The supplied output was produced from the supplied checker. Experiments corroborate but are not used as an infinite proof.

## Originality — PASS within inspected evidence

The explicit binomial-to-run-length correspondences are **not new**; they are the published starting point in Rampersad–Wiebe (2023), Section 5. The exact arithmetic odd-support description of the second transform, its rational count, its algebraic growth exponent and asymptotic constant, and the strict relative exponential thinning in the companion pair are not asserted in that paper. Its Section 6 treats means of selected original transforms, not parity-support counts for this pair. Wu (2016, preprint; later revisions) establishes related but different older transforms, not this pair. OEIS A124312 **does already tabulate the first transform's binary-word count**, so that enumeration is a comparison baseline rather than independently claimed originality. An entry implying the second transform's count or the support-inclusion/relative-growth theorem was not identified by focused formula, coefficient, keyword, equivalence, and thematic searches. Such searches do not prove global novelty; unidentified equivalent counting sequences remain a residual risk.

## Mathematical value — PASS

These are two naturally paired arithmetic sums, introduced together by the primary source precisely because their generating recurrences agree but their initial conditions differ. The exact parity-support theorem shows that this small initial-state change produces a strict support inclusion and an unusually large gap between canonical power-law counting exponents (approximately \(0.975225\) versus \(0.582165\)); furthermore their relative dyadic frequency decays at a specified exponential rate. Parity sparsity and its precise exponent describe a nontrivial natural invariant of the arithmetic transforms, complementing the paper's work on mean values. The second rational enumeration and the relative asymptotics are not merely a recomputation of the previously catalogued first count, and the comparison is useful for questions about distribution and constraints in automatic/regular number-theoretic sequences.

## Closest literature and limitations

* Rampersad and Wiebe, *Sums of products of binomial coefficients mod 2 and 2-regular sequences*, arXiv:2309.04012v1 (2023-09-07), Theorems 13–14 and Section 6: supplies input formulas but no stated parity-support count/exponent comparison.
* Chai Wah Wu, *Sums of products of binomial coefficients mod 2 and run length transforms of sequences*, arXiv:1610.06166v1 (2016-10-19): precursor and general identities, not the two new 2023 transforms.
* OEIS A124312: older exact forbidden-run enumeration for the first companion. The current claim does not present that independent enumeration as new.

The result applies only to these two binomial sums, presupposes the published identities, and concerns parity, not magnitude distributions. No independent scientific audit has been performed; possible undiscovered equivalent counting statements remain a genuine originality risk.

Self-review: passed. Independent audit: not yet performed.
