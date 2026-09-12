# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Split-p finite cuspidal criterion at (K,p)=(Q(i),5)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1397
- **Disposition:** AUDIT_1_REJECT
- **Domain:** anabelian geometry over imaginary quadratic fields
- **Method:** local Heisenberg inertia commutators plus cyclotomic descent on finite ledger

## Problem

Fix K=Q(i) and p=5, which splits as (2+i)(2-i). Let X_K=P^1_K\{0,1,infinity}, Pi its geometric pro-5 group, H=Pi/[gamma_3,Pi^25] the finite Heisenberg exponent-25 quotient with center Z=Z/25(2), pushed out to 1->H->E_H->G_{K,T}->1 with T the places above {2,5}. For a section s:G_{K,T}->E_H let s_v be its restriction at each v|5 with explicit inertia generator, and let the cyclotomic-descent condition be that its Kummer pair (b,a) in the finite ledger O_{K,T}^\times/(O_{K,T}^\times)^25 descends from the mod-25 cyclotomic Z_5-extension of K via the explicit unit ledger. Decide the split-p finite cuspidal criterion: is it true that s is H-conjugate into a cuspidal decomposition image if and only if each s_v satisfies the local Heisenberg inertia commutator relation [s_v(I_v),x_v]=[s_v(I_v),y_v]=1 and (b,a) satisfies cyclotomic descent? A complete answer is either a proof of this equivalence with explicit local-plus-global ledgers, or an explicit section satisfying both local conditions that is provably non-cuspidal, or a cuspidal section violating one of them.

## Attempted claim

Fix K=Q(i) and p=5, which splits as (2+i)(2-i). Let X_K=P^1_K\{0,1,infinity}, Pi its geometric pro-5 group, H=Pi/[gamma_3,Pi^25] the finite Heisenberg exponent-25 quotient with center Z=Z/25(2), pushed out to 1->H->E_H->G_{K,T}->1 with T the places above {2,5}. For a section s:G_{K,T}->E_H let s_v be its restriction at each v|5 with explicit inertia generator, and let the cyclotomic-descent condition be that its Kummer pair (b,a) in the finite ledger O_{K,T}^\times/(O_{K,T}^\times)^25 descends from the mod-25 cyclotomic Z_5-extension of K via the explicit unit ledger. Decide the split-p finite cuspidal criterion: is it true that s is H-conjugate into a cuspidal decomposition image if and only if each s_v satisfies the local Heisenberg inertia commutator relation [s_v(I_v),x_v]=[s_v(I_v),y_v]=1 and (b,a) satisfies cyclotomic descent? A complete answer is either a proof of this equivalence with explicit local-plus-global ledgers, or an explicit section satisfying both local conditions that is provably non-cuspidal, or a cuspidal section violating one of them.

## Research outcome

Disproved the split-p finite cuspidal iff at (Q(i),5): the local Heisenberg inertia test is unsatisfiable on full and tame inertia, and an existing cuspidal section violates it.

## Why this attempt failed

Failed axes: value.

value: ADMISSION_DEFECT: negative resolution exposes exactly the cheap vacuity/type-normalization error Admission was required to rule out. Under the only non-vacuous reading, the local test [s_v(I_v),x_v]=[s_v(I_v),y_v]=1 demands inertia centralize Tate-weight-1 generators on which it acts by surjective chi, impossible for every section already on tame inertia (u=7). Antecedent never holds; DRAFT admits converse vacuously true and descent moot. Topic.json never defines x_v,y_v, and central reading would make test trivially pass, confirming ill-posed normalization (centralizer vs twisted centralizer). Refutation is elementary weight observation plus standard tangential existence, no new boundary, benchmark, classification, or transferable structure beyond textbook semidirect lemma; 15625-element certification strengthens evidence but does not create value per STANDARD. Therefore independently not worth retrieving despite literal falsity.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: No claim is made about any Kummer pair's cyclotomic-descent status since the refutation does not need it; the converse (local+descent implies cuspidal) holds only vacuously because the antecedent never occurs, which is not claimed as a positive result; the argument uses the standard non-central reading of x_v,y_v as lifts of a V-basis, the only reading under which the commutator test is non-vacuous, as documented in DRAFT section 5.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
