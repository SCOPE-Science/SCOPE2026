# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Aut(O2) conjugation versus density-zero equality
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1620
- **Disposition:** AUDIT_1_REJECT
- **Domain:** descriptive set theory / C*-algebras
- **Method:** generic turbulence and pinned-ness

## Problem

Let O2 be the Cuntz algebra and Aut(O2) with point-norm Polish topology act on itself by conjugation, with orbit equivalence E_C*: alpha E_C* beta iff exists gamma in Aut(O2) with beta=gamma alpha gamma^{-1}. Let E_d on 2^N be asymptotic-density-zero equality: for a,b subset N identified with 2^N, a E_d b iff lim_{n->infinity} |(a triangle b) cap n|/n=0. Decide: is E_C* Borel reducible to E_d, i.e. does there exist a Borel map f:Aut(O2)->2^N with alpha E_C* beta iff f(alpha) E_d f(beta)? A complete answer is either such an explicit Borel reduction with proof of the iff property, or a rigorous proof that no Borel reduction exists, e.g. via generic turbulence of the Aut(O2)-action, pinned-ness, or Baire-ergodicity obstruction.

## Attempted claim

Let O2 be the Cuntz algebra and Aut(O2) with point-norm Polish topology act on itself by conjugation, with orbit equivalence E_C*: alpha E_C* beta iff exists gamma in Aut(O2) with beta=gamma alpha gamma^{-1}. Let E_d on 2^N be asymptotic-density-zero equality: for a,b subset N identified with 2^N, a E_d b iff lim_{n->infinity} |(a triangle b) cap n|/n=0. Decide: is E_C* Borel reducible to E_d, i.e. does there exist a Borel map f:Aut(O2)->2^N with alpha E_C* beta iff f(alpha) E_d f(beta)? A complete answer is either such an explicit Borel reduction with proof of the iff property, or a rigorous proof that no Borel reduction exists, e.g. via generic turbulence of the Aut(O2)-action, pinned-ness, or Baire-ergodicity obstruction.

## Research outcome

Decided the target negatively: E_C* is not Borel reducible to E_d, via generic turbulence of Aut(O2)-conjugation versus pinned-ness of E_d, with self-contained P-ideal and Borel-complexity lemmas plus a machine-checked diagonal construction.

## Why this attempt failed

Failed axes: originality, value.

originality: Headline E_C* not<=_B E_d is substantively implied by a prior stronger fact: Gardella-Lupini arXiv:1404.3617 proves O2 conjugacy E_C* is complete analytic hence non-Borel, while E_d is Borel Pi03 (standard, also Lemma 1). Textbook lemma: if E<=_B F via Borel f then E=(f x f)^-1(F), so non-Borel E can never reduce to Borel F. Thus the exact comparison is mechanically implied by prior work plus one textbook step. Fused retrieval found no exact prior statement of the pair, but literal-title absence does not establish priority when a broader theorem covers it as a special case. value: ADMISSION_DEFECT: the admitted target asked for turbulence/pinned obstruction, but the negative answer follows from a Borel-level type mismatch alone (known non-Borel source versus known Borel target). Pairing one fixed non-Borel relation with one arbitrary Borel relation among continuum-many Borel equivalences is an arbitrary parameter fact / direct complexity-level lookup, not an advance of a recognized question. The elaborate turbulence-vs-pinned assembly is redundant given complete-analyticity. Under TARGET policy a negative resolution by type/normalization error, direct lookup, or arbitrary parameter fact fails value even if literally true.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Lemmas 1-2 and the logical assembly are proved self-contained in DRAFT.md, but Theorems T, Z, O are cited in precise stated form without reproducing their published proofs, so the result is conditional on those standard statements. One controlled literature-retrieval call was attempted to re-verify citations but the backend was unavailable (missing API key), so exact bibliographic details are deferred. The machine check covers only the finite combinatorial core of the P-ideal diagonal argument,…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
