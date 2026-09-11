# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Stein-embedding rigidity for a symmetric Mazur cork: twist extension blocking exoticity
- **Round:** 2026-09-07-first-light-01
- **Lane:** 702
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Differential Topology
- **Method:** relative Seiberg-Witten theory with Stein handle-embedding calculus

## Problem

Prove a Stein-embedding rigidity lemma for one explicit symmetric Mazur-type Stein cork: show its boundary involution extends over the contractible handlebody via a logged Kirby isotopy, the two induced contact structures have equal d3, and any symplectic-cap twist pair is standard by Seiberg-Witten adjunction, blocking exoticity for that handle pattern.

## Attempted claim

Let W_{2,2}^{sym} be the contractible Mazur-type Stein handlebody given by fixed symmetric Legendrian diagram D_sym (one 1-handle, two 2-handles in tb-1 Stein position with palindromic box twists (2,2)), boundary Y_{2,2} an integral homology sphere, tau the palindromic exchange involution. Then tau extends to a diffeomorphism of W_{2,2}^{sym} via an explicit logged Kirby isotopy, d3(xi1)=d3(xi0) for the induced contact structures, and for the fixed Akbulut-Yasui minimal symplectic cap Z the twist Z_tau is diffeomorphic to Z by SW adjunction, so this pattern carries no exoticity.

## Research outcome

TARGET resolved by disproof: the literal symmetric (2,2) contractible-Stein 1+2-handle cell presupposed by target_claim is topologically impossible (chi=2!=1, rank-nullity); the only chi-repair needs a 3-handle outside the stated diagram and violates the Mazur-type clause. Full proof in output/DRAFT.md; integer replay VERIFY_OK.

## Why this attempt failed

Failed axes: originality, value.

originality: Audited headline is the disproof claim itself: 'No (1,1,2,0,0) handlebody is contractible, chi=2!=1.' This is a direct numerical substitution into the general textbook handle-Euler theorem chi=sum(-1)^i n_i plus chi(contractible)=1, which substantively implies it without new mathematics. Per LIVE contract, a prior source need not state the headline verbatim; a broader theorem that exhaustively covers it as a special case defeats originality. The general formula covers all count vectors including (1,1,2,0,0). Fused retrieval (SerpBase 10 + OpenAlex/Crossref 15 per query, no partial failure) returned only general handle theory (Cambridge Theory of handle decompositions chi(M)=2-alpha1 example, Oberlin Contractible 4-Manifolds thesis, Akbulut-Yasui corks/plugs) and no specific W^{sym}_{2,2} record — but absence of an exact-number row does not confer originality when the covering general theorem is textbook. The finding is a recomputation/certificate/corollary of that stronger fact. Hence originality FAILS. Originality failure is never repairable. value: Correct disproof of a self-contradictory specification is not an independently retrievable research result. The headline is a textbook restatement with mere parameter substitution (plug n0=1,n1=1,n2=2 into chi formula), explicitly rejected even if correct and new. It establishes no invariant of an existing natural object: by its own Limitations it 'decides no actually existing cork, no exoticity elsewhere, and no repaired diagram.' The W^{sym}_{2,2} object does not exist, so there is no future filling/cobordism/cork-search use requiring chi=2 for (1,1,2). The narrow-datum allowance (exact invariant of a motivated natural object, not mechanically implied, reasonably needed later) does not apply: the value here is mechanically implied, the object is not natural/existing, and certification alone does not rescue it. The admission value PASS covered the positive rigidity lemma (tau-extension+d3-equality+cap standardness), not this arithmetic invalidation; no preset-value presumption transfers. Intrinsic low value -> REJECT, not REPAIRABLE.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Disproves the literal 1+2-handle joint hypothesis only; decides no actually existing cork, no exoticity elsewhere, and no repaired (different-object) diagram. Whether some other diagram with a 3-handle could independently carry a Stein structure is not decided here. Uses Mazur-type terminology in the standard sense; no Floer/SW/contact computation claimed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
