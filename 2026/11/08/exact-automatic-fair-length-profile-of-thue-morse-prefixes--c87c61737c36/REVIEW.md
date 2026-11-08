# Scientific review

## Correctness — PASS

The identity relating the scattered \(01\)/\(10\) difference to the length and letter imbalance of two fair concatenands is derived by direct counting. Its integer divisibility constraints eliminate all purported two-piece factorizations where the profile predicts three, and they force a unique cut where the profile predicts two. The \(4\)-uniform substitution gives the exact difference and imbalance for every prefix. All boundary cases \(n=1,2,3\) are covered. The independent substring-DP verifier checked every prefix through length \(2048\), plus separate ordered-pair tests. No finite search is used to justify the infinite result.

## Originality — PASS, with priority risk

A full-text inspection of Richomme's arXiv:2510.07159v1, particularly §§6.2–6.3 and Proposition 6.2, finds the general factor bound four and its proof, not the exact prefix formula, residue-dependent one/two/three classification, unique two-part cuts, or aperiodic profile. The standard Thue–Morse automatic-sequence results establish substitution recurrences but do not give the fair-length factorization formula. Targeted semantic mathematical-record searches and searches for the exact prefix length pattern found no covering result. An earlier unindexed or unpublished equivalent computation is still possible.

## Value — PASS

The 2025 work introduces fair length and proves a universal factor bound four, with sharp examples. The present theorem obtains a **complete infinite-prefix classification**, a strictly sharper bound three, forced uniqueness of every optimal two-piece cut, and an explicit automatic yet nonperiodic length spectrum with exact densities. These are structural results about the newly studied factorization invariant, not an arbitrary bounded census or a routine finite increment. The theorem also pinpoints why the sharp factor bound four never appears at the distinguished prefix origin.

## Closest literature and remaining limits

G. Richomme, *On some 2-binomial coefficients of binary words*, arXiv:2510.07159v1, §6.3 and Proposition 6.2, is the closest inspected primary source. The cited result covers **every factor** only with a bound, whereas the present result covers **prefixes** with exact minima and split uniqueness. Other shifted factors are not classified. No third-party independent check is claimed; unindexed priority remains a risk.

Self-review: passed. Independent audit: not yet performed.
