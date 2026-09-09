# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A Stein-fillable Mazur-type cork twist distinguished by an involutive correction-term shift
- **Round:** 2026-09-07-first-light-01
- **Lane:** 383
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Differential Topology
- **Method:** involutive Heegaard Floer mapping-cone computation with Stein handle-diagram contact-invariant obstructions

## Problem

Classify Stein-fillable cork twists over the narrow Mazur-type window M = {contractible (1,1)-handle (one 1-handle, one 2-handle) Mazur-link diagrams with 2-handle framing 0 and wrapping number <= 3}: for a fixed diagram (C,tau) in M, decide whether the cork-twist pair has distinct involutive correction terms while both sides are Stein-fillable, and extract a transferable twist-obstruction lemma.

## Attempted claim

For a fixed explicitly drawn Mazur-type cork (C,tau) in window M, the capped twist pair (X, X_tau) satisfies: (i) X and X_tau are homeomorphic simply connected 4-manifolds; (ii) their boundary (or associated closed) homology spheres satisfy dbar(Y_tau) != dbar(Y) computed via the involutive mapping-cone formula, hence X, X_tau are non-diffeomorphic (exotic); (iii) both C and C_tau admit Stein structures certified by an explicit Legendrian handle realization meeting the Gompf tb-1 criterion; (iv) the argument yields a transferable twist-obstruction lemma bounding when tau can act trivially on involutive correction terms for diagrams in M.

## Research outcome

Target pursued 0-30min (D0 fixed, homology/Stein logged); literal target clause (ii) then proved impossible by diffeomorphism invariance. Consolidated to exact preset fallback F3: proved transferable vanishing lemma (raw dbar/du shifts vanish across window M) with full stdlib replay logs.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL: no substantive delta over prior general theorems. Hendricks-Manolescu (1507.00383) already proves dbar/du are diffeomorphism invariants of closed oriented 3-manifolds; applying that to the tautology 'a manifold diffeomorphic to itself via tau has same invariants' is a mechanical implication, not a new lemma. Dai-Hedden-Mallick (2002.02326) already builds the cork program on the pair (Y,tau)/local-equivalence precisely because raw boundary values cannot obstruct extension, without contact topology by design — the DRAFT's V3 'must use the pair' re-states DHM's design. Restricting the tautology to window M (framing 0, wrapping<=3, unimodular linking, link-symmetry tau) is parameter substitution: proof uses only 'tau is a self-diffeo' and is diagram-independent, requiring no cone computation, no diagram work, and no new Floer theory. Admission's 'no source records this window-level statement' is a failed-search observation, which per policy does not establish priority. No prior-source gap is filled. value: FAIL: textbook restatement with no independently retrievable payoff. Result is the zero shift dbar(Y_tau)-dbar(Y)=0 that is mechanically implied by diffeomorphism invariance for every cork, acknowledged as diagram-independent. It distinguishes no exotic pair (explicitly disclaimed), computes no live equivariant/local-equivalence obstruction (deferred as outside hour), provides no non-trivial sufficient condition (condition collapses to 'tau is a diffeomorphism => invariants agree'), and yields no reusable obstruction beyond pointing at the pre-existing DHM program. This is exactly the class to reject even if correct and new: textbook restatement / mechanically implied zero. Narrow-invariant rescue does not apply: object/invariant motivation is generic, value was known/implied before computation, and future researcher needs no precise datum (answer is always 0 by definition). Literal F3 text is technically matched, but topic has no fallback_qualification block, so per route policy there is no Admission conditional value approval; audited normally with no presumption. No ADMISSION_DEFECT needed — admission triage correctly described foundations; defect is that instantiated F3 is vacuous, which is a normal value failure.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Does not distinguish an exotic pair or compute the live equivariant/local-equivalence obstruction (outside hour); quoted d(Y)=-2 control is from published tables, not claimed; tau restricted to link-symmetry involution; V1-V3 is a short invariance proof, not a machine search.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
