# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Full-ensemble 1D discrepancy rate for Dedekind sums
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1662
- **Disposition:** AUDIT_1_REJECT
- **Domain:** analytic number theory
- **Method:** Rademacher-Kloosterman identity with Weil bound and Erdos-Turan plus large-Kloosterman lower bound

## Problem

Let s(h,k)=sum_{r=1}^{k}((r/k))((h r/k)) be the classical Dedekind sum with ((x))=x-floor(x)-1/2 for non-integer x and 0 otherwise, and {y} the fractional part. For prime p congruent to 3 mod 4 let D_p be the 1D star-discrepancy in [0,1] of the multiset {{12 s(h,p)}: 1<=h<p, gcd(h,p)=1}, i.e. D_p=sup_{0<=t<=1}|(1/(p-1))#{h:{12 s(h,p)}<=t}-t|. Prove or disprove that there exist absolute constants C,c>0 and P0 such that for every prime p>=P0 with p=3 mod 4 one has D_p<=C p^{-1/2}(log p)^2, and there are infinitely many primes p=3 mod 4 with D_p>=c p^{-1/2}/log p. A complete answer is a rigorous proof of both bounds or a rigorous disproof of at least one (an infinite violating subsequence against the upper bound, or eventual failure of the lower bound).

## Attempted claim

Let s(h,k)=sum_{r=1}^{k}((r/k))((h r/k)) be the classical Dedekind sum with ((x))=x-floor(x)-1/2 for non-integer x and 0 otherwise, and {y} the fractional part. For prime p congruent to 3 mod 4 let D_p be the 1D star-discrepancy in [0,1] of the multiset {{12 s(h,p)}: 1<=h<p, gcd(h,p)=1}, i.e. D_p=sup_{0<=t<=1}|(1/(p-1))#{h:{12 s(h,p)}<=t}-t|. Prove or disprove that there exist absolute constants C,c>0 and P0 such that for every prime p>=P0 with p=3 mod 4 one has D_p<=C p^{-1/2}(log p)^2, and there are infinitely many primes p=3 mod 4 with D_p>=c p^{-1/2}/log p. A complete answer is a rigorous proof of both bounds or a rigorous disproof of at least one (an infinite violating subsequence against the upper bound, or eventual failure of the lower bound).

## Research outcome

Both halves of the target proved true: D_p << (log p)/sqrt(p) for all large primes p=3 mod 4 and D_p >> 1/sqrt(p) for infinitely many such p, via the Dedekind-Kloosterman congruence, Weil plus Erdos-Turan, and Koksma plus Katz Sato-Tate.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route: upper bound and Koksma lemma verify, but headline lower bound is unproved. Lemma 1 congruence proof, Weil+Erdos-Turan upper D_p<<log p/sqrt(p), Remark on p=3 mod 4 avoiding atom at 0, and Lemma 2 D_p>=|K(1,1;p)|/2pi(p-1) were checked line-by-line and reproduced numerically (1105 pairs pass; Koksma holds for p=3 mod 4 <=200). Lemma 3 claims Katz vertical Sato-Tate over p=3 mod 4 gives equidistribution of theta_p for diagonal K(1,1;p) and hence infinitely many |K|>=sqrt(p). Cited Katz Ch.9 and Fouvry-Kowalski-Michel Duke 2014 do not prove diagonal equidistribution as modulus varies in a progression; they give horizontal equidistribution (vary a, fixed p) and power-saving for sums over primes of fixed-modulus trace functions. Diagonal vertical Sato-Tate as p varies is not an established black box. Hence infinitely-often lower bound and two-sided headline remain unproved.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: The proof cites four standard deep theorems as black boxes rather than reproving them: Dedekind reciprocity, the Weil bound for Kloosterman sums, the Erdos-Turan inequality, and the Katz vertical Sato-Tate law for Kloosterman angles over primes in arithmetic progressions (with the Fouvry-Kowalski-Michel form for the progression aspect). Constants C and c are absolute but not optimized. The numerical scripts are illustrative checks of the lemmas on small moduli and are not part of the logical ch…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
