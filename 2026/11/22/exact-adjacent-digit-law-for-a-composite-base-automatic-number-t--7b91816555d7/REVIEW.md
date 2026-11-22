# Scientific review

## Correctness
PASS. The proof independently derives the exact two-prime valuation and residue classification, uses Chinese-remainder equidistribution and a convergent geometric series to compute the conditional nine-digit law, and splits adjacent indices into five disjoint cases. Boundary cases (positive indices, equality of valuations, zero/nonzero residues, and the shared transition) are handled. The logarithmic-squared discrepancy follows from bounded numbers of congruence classes in each valuation stratum. The standalone verifier directly compares the first 300 huge-integer values and 200,000 adjacent pairs, including all 20 support edges; these are corroboration, not an infinite proof.

## Originality
PASS on inspected evidence, with residual bibliographic risk. Example 5.3 of Sobolewski (2022 preprint, 2023 article) supplies the exact object, its strictly automatic nature and a pointwise formula, but it does not state an adjacent-pair histogram, the complete twenty-edge language or a quantitative finite-prefix law. Related published characterizations of factorial digits and arithmetic automatic-word bigrams concern different objects. The new statement is a nontrivial complete statistical classification derived from, not an invention of, the established pointwise representation. Search coverage cannot guarantee global novelty.

## Value
PASS. Symbol frequencies alone do not describe successor constraints of automatic arithmetic sequences. The exact sharp transition support, nonuniform rational weights and uniform logarithmic-squared discrepancy provide a natural full two-point invariant of a deliberately constructed two-prime p-adic example. They make the resulting recurrence's permitted and forbidden local patterns explicit, and give a baseline for longer-block analyses. This is a modest self-contained exact distribution theorem, not a claim to a broad new framework.

## Closest literature and limitations
B. Sobolewski, *On k-regularity of sequences of valuations and last non-zero digits*, Example 5.3, https://doi.org/10.1007/s11139-023-00710-8 (full relevant example inspected); B. Sobolewski, *On the last nonzero digits of n! in a given base*, https://arxiv.org/abs/1809.06947 (different sequence). The paired-word distribution is derived from the earlier pointwise digit classification; other unindexed literature may contain equivalent results. Results are for pairs only; no all-block classification is asserted.

Self-review: passed. Independent audit: not yet performed.
