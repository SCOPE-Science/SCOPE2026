# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Jump-spectrum equality versus degree-spectrum separation
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1306
- **Disposition:** AUDIT_1_REJECT
- **Domain:** computable structure theory
- **Method:** jump inversion and transfer via equivalence structures

## Problem

Fix a prime p. Do there exist computable reduced abelian p-groups G and H, both of Ulm length at most omega with divisible part zero, such that their jump degree spectra {x' : x in DgSp(G)} and {x' : x in DgSp(H)} are equal as sets of Turing degrees, but their unrelativized degree spectra DgSp(G) and DgSp(H) are different as sets (i.e., some degree computes a copy of exactly one of G,H)? A complete answer either exhibits such G,H with full verification of the jump-spectrum equality and a separating degree for the degree spectra, or proves that equality of jump spectra forces equality of degree spectra for all such pairs.

## Attempted claim

Fix a prime p. Do there exist computable reduced abelian p-groups G and H, both of Ulm length at most omega with divisible part zero, such that their jump degree spectra {x' : x in DgSp(G)} and {x' : x in DgSp(H)} are equal as sets of Turing degrees, but their unrelativized degree spectra DgSp(G) and DgSp(H) are different as sets (i.e., some degree computes a copy of exactly one of G,H)? A complete answer either exhibits such G,H with full verification of the jump-spectrum equality and a separating degree for the degree spectra, or proves that equality of jump spectra forces equality of degree spectra for all such pairs.

## Research outcome

TARGET proved: any two computable reduced abelian p-groups as stated have full degree spectra and hence equal jump spectra, so the requested separating pair cannot exist.

## Why this attempt failed

Failed axes: originality, value.

originality: Originality FAILS. The headline -- any two computable reduced abelian p-groups of Ulm length <=omega have full degree spectra and hence equal jump spectra -- is mechanically implied by the strictly broader textbook theorem: every computable structure contains 0 in its degree spectrum and every degree spectrum is upward-closed, hence every computable structure has spectrum = all degrees. Fused retrieval (SerpBase/OpenAlex/Crossref/OpenAIRE, partial=false) confirms the definitions and closure fact in standard sources (Montalban CST draft: 'Degree spectra are closed upward'; Harrison-Trainor arXiv:2505.23613: spectrum = degrees computing a copy, cones as simplest spectra). The p-group/Ulm/divisible-part hypotheses are admitted by the draft itself to play no role. A prior source need not state the p-group headline verbatim; substantive implication by the broader theorem defeats priority. A timestamp or failed literal-title search does not establish originality. value: Value FAILS -- ADMISSION_DEFECT. The resolution is correct but exposes an Admission mistake under STANDARD sky-survey-admission-depth-gate-v12: before research both TARGET outcomes must be plausibly independently original and valuable, ruling out type/normalization errors, vacuity, and arbitrary parameter facts. Here the negative outcome merely exposes definitional vacuity: by the admitted 'computes a copy' definition all computable structures trivially share the full spectrum, so no Ulm theory, jump inversion, or equivalence-structure transfer is tested. The draft itself states the Ulm hypotheses 'play no role beyond delimiting the class'. This is a textbook exercise / mere parameter substitution (prime p, Ulm length <=omega) with no motivated invariant, no downstream use, and nothing a future researcher would independently need to retrieve as a p-group result. Per TARGET route policy, a negative resolution that is only vacuity/cheap mismatch fails value even if literally true, and the Admission error is labeled here as ADMISSION_DEFECT.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The result uses only the hypothesis that G and H are computable, so the Ulm-theoretic hypotheses play no role; it says nothing about noncomputable p-groups, where spectra can be proper cones and jump equality need not imply spectrum equality, and nothing about alternate exact-degree spectrum definitions.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
