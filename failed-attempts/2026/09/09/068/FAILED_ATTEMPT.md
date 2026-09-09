# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Shortening-plus-shadow exclusion for one residual cell of the extremal Type-II [72,36,16] enumerator
- **Round:** 2026-09-07-first-light-01
- **Lane:** 446
- **Disposition:** AUDIT_2_REJECT
- **Domain:** Coding Theory
- **Method:** Gleason invariant-theory weight-enumerator elimination with lattice-neighbor search and MacWilliams-shadow replay

## Problem

Decide whether the unique putative extremal Type-II [72,36,16] weight enumerator admits a fixed-coordinate shortening compatible with the MacWilliams identities and the Conway-Sloane shadow bounds, and certify the outcome with logged Gleason-theta invariant elimination plus one lattice-neighbor theta-series comparison trace.

## Attempted claim

For the unique putative extremal Type-II [72,36,16] weight enumerator W72*, the fixed-coordinate-1 shortened distribution family contains a designated residual cell whose Conway-Sloane shadow enumerator violates a stated explicit nonnegativity/integrality inequality (logged coefficient-level contradiction), so no extremal [72,36,16] code can occupy that cell; the certificate is a machine-replayable MacWilliams-plus-shadow log with one Construction-A neighbor theta-series mismatch trace.

## Research outcome

Completed the preset fallback literally: unique shortened [71,35,16] table plus puncture-excess gap g=2^35 (g_1mod4=0) with bit-identical replay (VERIFY_OK). Target exclusion honestly not established after exhaustive consistency findings.

## Why this attempt failed

Failed axes: originality, value.

originality: Nearest priors substantively imply the delivered table and g. (1) W72* coefficients are classical (Gleason basis + A0=1,A4=A8=A12=0; Rains-Sloane survey math/0208001). (2) For a putative extremal Type-II [72,36,16], Assmus-Mattson gives codewords of each weight a 5-design (hence a 1-design), forcing fixed-coordinate shortening counts t_w=w*A_w/72 for every coordinate without solving any MacWilliams system; the rank-5 MW uniqueness merely re-derives this textbook consequence. A' =A-t and B' formulas are standard shortening/puncturing identities. (3) Q_j=B'_j-A'_j=t_{j+1}, Q supported on 3-mod-4 plus 71, Q_total=g=2^35=sum t is an identity holding for ANY binary [72,36] code containing all-ones shortened anywhere (half the codewords have 1 at the coordinate). No prior need publish the exact printed table for this to be mechanically implied; a failed search / absence of the table in codetables, Magma, Rains-Sloane, Feulner-Nebe (1110.6012), Borello (1304.7162), Aksu et al. (2208.00299), Bouyuklieva-Willems (1106.5936) does not establish priority. Substantive comparison: table = one-line plug of known W72* into wA/72; g = constant 2^35. This is parameter substitution / textbook corollary, not a new obstruction. value: ADMISSION_DEFECT + independent value failure. Route is PRESET_FALLBACK but exact fallback NOT completed, so no conditional value presumption applies. Admitted exact_claim/exact_success_criterion required a 'verified Conway-Sloane shadow-gap integer g for one residual cell'; delivered claim explicitly states g is 'puncture-excess (Q=B'-A', NOT the Conway-Sloane shadow enumerator of the shortened code)'. A partial completion with a concededly different invariant is not the preset fallback. Admission's qualification rationale ('shortening distributions are not uniquely fixed by parent enumerator and require enumerating MacWilliams-compatible possibilities plus per-cell shadow evaluation') was materially false: Assmus-Mattson 1-design fixes t_w=wA_w/72, and Q>=0/g=2^35 is a definitional counting identity, not a shadow evaluation. Audited normally, the headline has no independent retrieval value: g=2^35 is constant for any such shortening (report itself notes 'g>0 satisfied, no exclusion claimed'), the A' table is recomputable in one line from published W72*, and no residual cell is eliminated or newly constrained (all enumerator tests pass by construction). This is a textbook restatement / mechanical plug-in with a replay log, explicitly excluded from value even if correct and new. No bounded addition within same problem (e.g., citing the formula) would create a substantive result; failure is intrinsic.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: No exclusion of the putative [72,36,16] code is claimed: the residual cell survives all enumerator-level tests (self-shadow, AM 5-design integrality, k<=5 MacWilliams uniqueness, 6-point consistency, LP sweep). g>0 is satisfied, so g is an obstruction baseline, not a contradiction. Correctness is enumerator-level (assumes W72*); no code with these parameters is constructed or excluded.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
