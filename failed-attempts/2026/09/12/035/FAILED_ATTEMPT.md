# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Bounded braid-orbit separation for two J10 distinguished matrices
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1121
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Singularity Theory
- **Method:** bounded braid-word search with Stokes and Seifert invariant

## Problem

Let h be Arnold simple-elliptic type J10 with published Gabrielov diagram. Let S_a and S_b be two explicit 10x10 upper-triangular distinguished matrices built from two documented distinguished path systems, with compatible diagonals and determinants. Let Br_10 act with sign changes per Balnojan-Hertling. With explicit word-length bound L0 fixed in advance, decide whether S_b lies in the bounded orbit of S_a via a word within L0, versus S_a and S_b lying in distinct orbits certified by a mismatch of the Stokes invariant spectrum of S^{-1}S^t plus Seifert data.

## Attempted claim

For J10 with fixed Gabrielov data, the two named distinguished matrices S_a and S_b lie in distinct Br_10 orbits, certified by an explicit mismatch of the Stokes invariant spectrum of S^{-1}S^t together with Seifert data, with exhaustive enumeration excluding transporters up to length L0.

## Research outcome

Disproved the J10 separation target: the named pair lies in the same Br_10 orbit via reduced word sigma_2 sigma_5 sigma_9 with identical Stokes spectra and congruent Seifert data, and any Hurwitz-orbit pair provably shares Stokes similarity invariants.

## Why this attempt failed

Failed axes: originality, value.

originality: Originality FAILS: the headline same-orbit plus identical-spectrum fact is mechanically implied by the researcher's own construction plus textbook general identities, not a new theorem. S_b was defined as sigma_2 sigma_5 sigma_9(S_a), so same-orbit membership within L0=6 holds by definition of a Hurwitz translate; spectrum equality follows from the general similarity identity M'=P^{-1}MP and the Sebastiani-Thom tensor law M_a=M2 tensor M5, both standard Picard-Lefschetz/Seifert-form theory covered by Balnojan-Hertling distinguished-matrix orbit theory and Hertling monodromy work. No prior source states the arbitrary word sigma_2 sigma_5 sigma_9 verbatim, but a literal-title miss does not establish priority: the exact word is an arbitrary researcher-chosen parameter, the charpoly follows mechanically from known A2/A5 factors, and Lemma A restates a known braid invariant. The result is a corollary/repackaging of a known stronger fact. value: Value FAILS under the TARGET negative-resolution rule and the narrow-datum rule. The disproof decides only a self-constructed arbitrary-parameter fact: applying a chosen 3-move word to S_a trivially yields an orbit mate, so finding the same word back with 25 entry differences and equal spectra has no independent retrieval value. S_a=S(A2) tensor S(A5) is natural, but the word sigma_2 sigma_5 sigma_9, the bound L0=6, and the resulting S_b were not motivated before computation by J10 geometry, the Stokes charpoly t^10-t^9+t^7-t^6-t^4+t^3-t+1 is mechanically implied by the tensor product of known A2/A5 spectra, and no concrete downstream wall-crossing or moduli use needs this precise transporter. ADMISSION_DEFECT: Admission certified both transporter-existence and mismatch-separation as live for two independently documented path systems with compatible diagonals, but the research instantiated S_b as an explicit Hurwitz translate of S_a, making mismatch dead on arrival for this pair and reducing the rigorous disproof to vacuity/construction tautology rather than a substantive Stokes-region decision. Certification and exactness do not create value for an arbitrary scope.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Falsification applies to the named constructed pair and the target's mismatch-certification method via Lemma A; it does not classify all J10 distinguished matrices, unbounded orbits, or finer integral/real-chamber invariants for other pairs, and the rank-8 Seifert datum is a computed property of the fixed S_a rather than a general J10 theorem proved here.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
