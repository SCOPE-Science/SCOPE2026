# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Short initial Legendre-sum rate at sqrt(p)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1667
- **Disposition:** NO_RESULT
- **Domain:** analytic number theory
- **Method:** Burgess r=2 short-sum bound plus large-value omega construction with exact Legendre census

## Problem

Let (n/p) denote the Legendre symbol. For prime p congruent to 1 mod 4 let H_p=floor(p^{1/2}) and S_p=sum_{1<=n<=H_p}(n/p). Prove or disprove that there exist absolute constants C,c>0 and P0 such that for every prime p>=P0 with p=1 mod 4 one has |S_p|<=C p^{7/16} log p, and there are infinitely many primes p=1 mod 4 with |S_p|>=c p^{1/4}. A complete answer is a rigorous proof of both bounds or a rigorous disproof of at least one (an infinite violating subsequence against the upper bound, or eventual failure of the lower bound).

## Attempted claim

Let (n/p) denote the Legendre symbol. For prime p congruent to 1 mod 4 let H_p=floor(p^{1/2}) and S_p=sum_{1<=n<=H_p}(n/p). Prove or disprove that there exist absolute constants C,c>0 and P0 such that for every prime p>=P0 with p=1 mod 4 one has |S_p|<=C p^{7/16} log p, and there are infinitely many primes p=1 mod 4 with |S_p|>=c p^{1/4}. A complete answer is a rigorous proof of both bounds or a rigorous disproof of at least one (an infinite violating subsequence against the upper bound, or eventual failure of the lower bound).

## Research outcome

Target blocked on the infinitely-often lower half: upper bound follows from Burgess r=2 but CRT forcing and second-moment routes fail on quantified scale barriers; census evidence to 1e6 supports plausibility only. Clean exit with no finding claimed.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The Burgess r=2 upper-bound lemma was verified against the textbook statement but the full two-sided target is unproved: the CRT forcing route fails on the exp(y) modulus barrier, the second-moment route fails on the uniformity-in-d barrier, and the Legendre census to 1e6 is finite-range corroboration that cannot establish any infinitely-often asymptotic.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The Burgess r=2 upper-bound lemma was verified against the textbook statement but the full two-sided target is unproved: the CRT forcing route fails on the exp(y) modulus barrier, the second-moment route fails on the uniformity-in-d barrier, and the Legendre census to 1e6 is finite-range corroboration that cannot establish any infinitely-often asymptotic.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
