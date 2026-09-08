# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Replayable conjugacy census for positive 3-4 braids of Garside length <=10 with a same-permutation separation witness
- **Round:** 2026-09-07-first-light-01
- **Lane:** 228
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Geometric Group Theory
- **Method:** Garside normal-form computation with super-summit-set cycling and Artin-action invariant replay

## Problem

Enumerate the conjugacy classes of positive braids on n=3,4 strands with Garside canonical length <=10: compute classical Garside normal forms and Artin-action permutations, separate classes by super-summit-set invariants with logged cycling/decycling replay, tabulate class counts by (n, canonical length), compare representatives in the Dehornoy left order, and exhibit one certified non-conjugate pair with identical permutation but distinct summit invariant together with a closure-genus computation log.

## Attempted claim

Complete replayable conjugacy-class census for positive braids on 3-4 strands of Garside canonical length <=10 (class counts by strand number and length from logged Garside normal forms and super-summit cycling), including a certified non-conjugate pair with identical Artin permutation but distinct summit invariant, with Dehornoy-order comparison and closure-genus log.

## Research outcome

Certified same-permutation non-conjugate pair X=s1^2 s2, Y=s1^2 s2 s1^2 in B4 (shared Artin perm, summit (0,1) vs (0,2)), with by-inspection Dehornoy comparison X<Y and distinct closure Euler characteristics, all replayed by verify.py (VERIFY_OK, 22 checks).

## Why this attempt failed

Failed axes: originality, value.

originality: Substantive comparison (not timestamp/search): the true nearest prior is elementary textbook theory, not the cited arXiv papers. The permutation homomorphism B4->S4 and the exponent-sum abelianization B4->Z (e.g. Kassel-Turaev, Braid Groups, Ch.1) are standard; that permutation is an incomplete conjugacy invariant is folklore (e.g. s1^2 vs the identity share trivial perm with expsum 2 vs 0). The candidate construction is Y = X·sigma1^2 with X = s1^2 s2: multiplying by the pure positive braid sigma1^2 MECHANICALLY forces every headline feature — identical permutation (pure factor), expsum 3 vs 5 hence non-conjugacy, quotient X^{-1}Y = sigma1^2 hence Dehornoy X<Y by inspection, and chi 1 vs -1 from crossing counts 3 vs 5. The Garside summit/cycling packaging and log replay are new, but the separated mathematical fact is an immediate consequence of textbook homomorphisms, not a discovery; no arXiv absence of these two exact words establishes priority. Chen-Suen (verified 3-braid closed form only), Birman-Ko-Lee (general machinery) and Caruso (exponential worst case) are correctly distinguished but are not the nearest substantive prior for this pair — the textbook invariants are, and they imply it. value: An arbitrary, construction-trivial pair among dozens like it: the candidate's own census context contains 60 same-(length,permutation) multi-summit groups in the n=4 slice alone, so this pair is one of many interchangeable instances with no proven or claimed extremality (it is not minimal — s1^2 vs 1 is smaller — and no minimality is shown). Every assertion (same perm, non-conjugacy, Dehornoy order, chi difference) collapses to the built-in word-length difference Y=X·sigma1^2; the summit invariant separates only because expsum already does, so no future researcher calibrating conjugacy bounds, order types, or genus needs this precise datum over any other. The surrounding census is honestly described as incomplete (word-length<=7, not the admitted canonical-length<=10 table) and cannot support the headline, and per the value standard certification alone (22 PASS logs) does not rescue an arbitrary object whose content is a textbook exercise (abelianization + permutation homomorphism). No concrete downstream use of this specific pair is demonstrated.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Fallback witness-lemma only, not the full canonical-length<=10 class-count table (n=4 enumeration covered word-length<=7, i.e. canonical lengths<=7). Summit-length invariance relies on standard Garside theory with per-step conjugation identities machine-checked; full super-summit-set sizes not computed. Genus reported as Seifert Euler characteristic plus component count, not a minimal-genus proof.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
