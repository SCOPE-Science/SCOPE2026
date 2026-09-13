# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Polarity and regular nonabelian order-81 action for (81,16,3)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1706
- **Disposition:** AUDIT_1_REJECT
- **Domain:** combinatorial design theory
- **Method:** Kramer-Mesner orbit-matrix and difference sets

## Problem

For symmetric 2-(81,16,3) designs (v=81, k=16, lambda=3, order n=13): determine whether there exists such a design admitting both a polarity (an incidence-preserving involutory bijection from points to blocks) and a regular automorphism group that is a nonabelian group of order 81. A complete answer either exhibits an 81x81 (0,1)-incidence matrix satisfying the symmetric 2-(81,16,3) equations together with an explicit polarity permutation and regular group action verified by incidence preservation and pair-balance counts, or proves by exhaustive Kramer-Mesner orbit-matrix enumeration with a tactical decomposition log that no such polarity-preserving regular-orbit incidence matrix exists.

## Attempted claim

For symmetric 2-(81,16,3) designs (v=81, k=16, lambda=3, order n=13): determine whether there exists such a design admitting both a polarity (an incidence-preserving involutory bijection from points to blocks) and a regular automorphism group that is a nonabelian group of order 81. A complete answer either exhibits an 81x81 (0,1)-incidence matrix satisfying the symmetric 2-(81,16,3) equations together with an explicit polarity permutation and regular group action verified by incidence preservation and pair-balance counts, or proves by exhaustive Kramer-Mesner orbit-matrix enumeration with a tactical decomposition log that no such polarity-preserving regular-orbit incidence matrix exists.

## Research outcome

Proved polarity obstructions and difference-set nonexistence for symmetric 2-(81,16,3): abelian-regular polarity impossible; no DS in five order-81 groups; polarity numerics.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Theorem A fiber-triple classification and reversibility forcing were re-executed and verified (all admissible triples are permutations of (3,6,7), reversibility forces a repeat; sqrt(13)-not-in-Q(zeta9) argument is sound). Proposition C absolute count 16 and normalized-polarity lemma are sound spectral/orbit arguments. But Theorem B, essential to the headline, is not verifiable: the exact C enumerators (enum27.c, liftdirect.c, nonab_liftdirect.c), group tables and associativity checks cited in RUNLOG are absent from inputs/artifacts; qprofiles_c9c3.txt is a single summary line (SURVIVORS=0, no profiles to check); lifting claims (6 x 1594323 exact nonabelian tests, 0 lifts) have no certificate or code. Independent re-check confirmed P1/P2/P3 on samples and reps, but not the lifting nonexistence or the C9xC3 zero-profile enumeration. An essential computation therefore rests on self-reported node counts, so correctness FAILS. originality: Route is EMERGENT_FINDING and it genuinely arose from the target investigation (abelian-polarity reduction plus quotient pipeline), so no route penalty applies; assessment is on ordinary novelty. Arasu (JCTA 1986) proved no (81,16,3) difference set exists in any abelian group of order 81 (abstract: remaining two of five groups closed; Bozikov review and Abdollahi et al. 2007 Theorem 1.1 confirm the full abelian nonexistence). This strictly implies submitted Theorem A (no reversible abelian DS) and the C3^4 limb of Theorem B: if no abelian DS exists, a fortiori no reversible one exists. A new fiber-triple/sqrt(13) proof of a weak corollary does not make the claim new. Polarity count 16 and normalizer lemma are standard spectral/orbit facts via the cited Kantor/Jungnickel correspondence. The headline as framed is substantively covered by a stronger 40-year-old theorem, so originality FAILS; originality failure is never repairable. value: The abelian-polarity and C3^4 nonexistence add no independently retrievable fact beyond Arasu 1986: they are corollaries/repackaging of a known stronger nonexistence theorem, which the STANDARD rejects even if correct and re-proved. The only potentially new content (nonexistence in two to four specific nonabelian groups) is offered as an uncertified narrow slice of the 15 groups of order 81 with maximal-class groups admitted open, without verifiable certificates or the cited programs, and without a demonstrated downstream need for these exact group exclusions. Certification alone does not create value, and an unverified partial enumeration is not a retrievable exact invariant. Hence value FAILS.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The complete target is not closed: nonabelian groups of order 81 with only nonabelian order-27 quotients (maximal-class/class-3 groups) are outside this pipeline and remain open, as does existence of any symmetric 2-(81,16,3) design. Theorem A uses the cited Kantor/Jungnickel polarity-reversibility correspondence for abelian developments without re-proof. The attempted originality literature search failed (service key error), so originality is explicitly not claimed and audit must check overlap…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
