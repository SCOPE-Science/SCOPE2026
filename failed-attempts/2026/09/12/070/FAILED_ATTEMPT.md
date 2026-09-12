# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** PlainSelfTargetMSIS to SelfTargetMSIS linear reduction or separation
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1235
- **Disposition:** AUDIT_1_REJECT
- **Domain:** lattice-based signatures
- **Method:** PlainSelfTargetMSIS to SelfTargetMSIS black-box reduction

## Problem

Prove or disprove the assumption-separation claim for module-lattice Fiat-Shamir with aborts: let R_q=Z_q[X]/(X^256+1) with q=8380417, (k,l)=(4,4), challenge set B_39 of tau=39-sparse ternary polynomials, and the PlainSelfTargetMSIS game (adversary outputs (w,c,z) with Az-cw'=z-like relation under independently uniform matrix) versus the SelfTargetMSIS game (matrix A fixed uniform, hash-derived challenge). Claim: every PPT PlainSelfTargetMSIS solver with advantage eps implies a PPT SelfTargetMSIS solver with advantage at least eps/poly(lambda) via a black-box reduction that resamples the public matrix and reprograms at most one hash input, with at most linear loss in the number of hash queries and no change to the MSIS norm zeta. A complete resolution is either such an explicit reduction with stated loss and norm preservation, or an explicit separating adversary or distribution that wins the Plain game with non-negligible advantage while no corresponding SelfTargetMSIS winner exists under the same (q,k,l,tau,zeta) scope.

## Attempted claim

Prove or disprove the assumption-separation claim for module-lattice Fiat-Shamir with aborts: let R_q=Z_q[X]/(X^256+1) with q=8380417, (k,l)=(4,4), challenge set B_39 of tau=39-sparse ternary polynomials, and the PlainSelfTargetMSIS game (adversary outputs (w,c,z) with Az-cw'=z-like relation under independently uniform matrix) versus the SelfTargetMSIS game (matrix A fixed uniform, hash-derived challenge). Claim: every PPT PlainSelfTargetMSIS solver with advantage eps implies a PPT SelfTargetMSIS solver with advantage at least eps/poly(lambda) via a black-box reduction that resamples the public matrix and reprograms at most one hash input, with at most linear loss in the number of hash queries and no change to the MSIS norm zeta. A complete resolution is either such an explicit reduction with stated loss and norm preservation, or an explicit separating adversary or distribution that wins the Plain game with non-negligible advantage while no corresponding SelfTargetMSIS winner exists under the same (q,k,l,tau,zeta) scope.

## Research outcome

Proved the TARGET reduction: PlainSelfTargetMSIS solver implies SelfTargetMSIS solver with equal advantage via one hash programming, same MSIS norm zeta.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL: the headline one-program straight-line reduction is mechanically implied by the standard programmable-ROM planting lemma and is a textbook exercise specialized to fixed ML-DSA-44 parameters without using any property of q=8380417, n=256, (k,l)=(4,4), B_39 or zeta beyond nonemptiness. Any PPT finder for a relation R without hash binding yields a hash-bound finder by private simulation plus post-hoc programming of a fresh point with loss 1; DRAFT instantiates this with R=Phi_zeta. No new boundary, classification, or parameter-specific argument is given. The fused retrieval (SerpBase/OpenAlex/Crossref/OpenAIRE, no partial failure) plus direct primary sources (Lattice Zoo SelfTargetMSIS definition, Barbosa et al. 2023/246 Fiat-Shamir with aborts ROM/QROM proofs, StackExchange 117390/JMW24 quoting real Plain vs Self definitions) show the general lemma and the real matrix-distribution question predate and subsume the claim. Timestamp or literal-title absence does not establish priority; substantive implication defeats novelty. value: FAIL (ADMISSION_DEFECT): as formalized, the admitted target is vacuous/textbook. Plain as defined has no hash-binding win condition (RO unconstrained and irrelevant), Self adds only H(w,M)=c satisfiable by one post-hoc program on a fresh point, so the positive side is a one-line ROM programming observation with loss 1 independent of Q and identical zeta, using none of the ML-DSA-44 specifics. This is a mere parameter substitution of a textbook exercise and an arbitrary finite slice (q,k,l,tau fixed but unused), with no demonstrated downstream need for this exact datum, no new structural insight, and no separation analysis of the substantive literature question (uniform A vs systematic [I|A'] with hash in both games, cf. JMW24/StackExchange opposite-direction row-reduction). Certification (toy replay with planted solver at n=8,q=257) strengthens replayability but does not create value per STANDARD. The result exposes that Admission failed to rule out vacuity/textbook triviality before research: ADMISSION_DEFECT.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Games formalized from the topic description around predicate Phi_zeta; ML-DSA abort/rejection-sampling distributions abstracted since claim clauses concern only advantage, program count, and zeta. Reduction lives in the one-programmable random-oracle model; concrete SHAKE hash is not programmable. Toy parameters (n=8,q=257,k=l=2,tau=3) validate reduction mechanics only and carry no hardness claim for full ML-DSA-44 parameters.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
