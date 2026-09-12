# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Isomorphism versus bi-embeddability spectra for p-groups
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1307
- **Disposition:** AUDIT_1_REJECT
- **Domain:** computable structure theory
- **Method:** Ulm-invariant embedding analysis and coding

## Problem

Fix a prime p. Does there exist a computable reduced abelian p-group G of Ulm length at most omega+1 with divisible part zero such that its isomorphism spectrum DgSp(G) = {deg(X) : X isomorphic to G} is a proper subset of its bi-embeddability spectrum BiEmb(G) = {deg(X) : X bi-embeds with G via mutually embeddable computable-in-X copies}? A complete answer either constructs such G plus a degree d with a d-computable structure bi-embeddable with G and a proof that no d-computable copy is isomorphic to G, or proves that DgSp(G) = BiEmb(G) for every computable reduced abelian p-group of that Ulm-length scope.

## Attempted claim

Fix a prime p. Does there exist a computable reduced abelian p-group G of Ulm length at most omega+1 with divisible part zero such that its isomorphism spectrum DgSp(G) = {deg(X) : X isomorphic to G} is a proper subset of its bi-embeddability spectrum BiEmb(G) = {deg(X) : X bi-embeds with G via mutually embeddable computable-in-X copies}? A complete answer either constructs such G plus a degree d with a d-computable structure bi-embeddable with G and a proof that no d-computable copy is isomorphic to G, or proves that DgSp(G) = BiEmb(G) for every computable reduced abelian p-group of that Ulm-length scope.

## Research outcome

Proved the target in the negative: every computable reduced abelian p-group of Ulm length at most omega+1 has isomorphism spectrum equal to bi-embeddability spectrum, both being all Turing degrees.

## Why this attempt failed

Failed axes: originality, value.

originality: Headline 'for every computable countable G, DgSp(G)=BiEmb(G)=all degrees' is not new: it is mechanically implied by two textbook facts - (i) degree/isomorphism spectrum of a computable structure contains 0 and is upward closed, hence all degrees, and (ii) isomorphic copies are mutually embeddable so DgSp subset BiEmb. Live fused search (SerpBase/OpenAlex/Crossref/OpenAIRE, partial=false) returned the decisive bi-embeddability-spectra literature, notably Fokina-Rossegger-San Mauro 2019 'Bi-embeddability spectra and bases of spectra' plus degree-spectra surveys (Knight/Fokina/Miller/Solomon theses) defining the same spectra and upward-closure. No synonymous notation, dual/complement encoding, or database evades this implication; the general computable-structure fact strictly dominates the p-group Ulm-length<=omega+1 special case. A timestamp or absence of verbatim equality statement does not establish priority when prior result substantively implies it. Originality FAILS and is never repairable. value: ADMISSION_DEFECT: the TARGET's computable-G hypothesis makes the question vacuous. The submitted proof uses only computability and upward closure and no Ulm invariants, reducedness, divisible-part, prime p, or omega+1 bound, answering a general computable-structure triviality rather than advancing the admitted p-group classification/coding problem. Under STANDARD and TARGET policy a rigorous negative resolution that merely exposes vacuity, type/normalization collapse, or trivial upward-closure-from-0, without any motivated invariant, boundary, benchmark, or downstream use, fails value even though literally correct. This is a textbook restatement and arbitrary-scope corollary with no independent retrieval worth: no future researcher needs to retrieve this p-group record to learn that computable spectra are all degrees. Intrinsic triviality, not a bounded presentation gap, so not repairable.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The result is deliberately general and does not analyse noncomputable groups, degree spectra of relations on p-groups, or the structure-level classification of bi-embeddability types; it uses only computability of G and upward closure, not Ulm invariants or the omega+1 length bound.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
