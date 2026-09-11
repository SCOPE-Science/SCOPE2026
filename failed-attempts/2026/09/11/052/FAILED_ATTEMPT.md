# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** dP2 smooth-divisor chamber: order-2 scattering identity for the anticanonical class
- **Round:** 2026-09-07-first-light-01
- **Lane:** 833
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Enumerative Geometry
- **Method:** tropical scattering-diagram wall-crossing with mirror cluster theta-function comparison

## Problem

For X=dP2 (blowup of P2 at 7 general points) with smooth anticanonical elliptic divisor E, compute the Gross-Siebert scattering diagram from its toric degeneration to order 2 at one named joint and decide the chamber identity: does log of the unbounded-wall product equal the genus-0 maximal-tangency generating function at class beta=-K_X, i.e. does the theta coefficient equal N_beta?

## Attempted claim

The order-2 consistent scattering diagram for (dP2, smooth E) has unbounded-wall product F_out with log F_out = N_{-K} z^{-2 m_out} + higher terms, i.e. the genus-0 maximal-tangency log invariant N_{-K} equals the mirror theta coefficient at this joint; if consistency fails, the obstructing wall carries an explicit multiple-cover correction term stated with the joint.

## Research outcome

Target blocked (no Graefnitz-form toric degeneration for dP2; w_out-mixing). Emergent finding: primitive-point log BPS m^P_{-K}=10 for (dP2,smooth E) with eta=0 proof, plus the order-2 mixing obstruction showing the literal chamber equation is ill-posed. Verified by replay scripts; full report in DRAFT.md.

## Why this attempt failed

Failed axes: originality, value.

originality: EMERGENT_FINDING route verified as genuinely target-derived (same pair (dP2,E), same class beta=-K, invariant side of audit step 4 + structural reason steps 1-3 blocked), not a convenient replacement; no preset-value presumption applied. Fused live search (3 normalized forms in one scope_literature_search call, no partial failure) + full-text comparison shows headline count is substantively implied by strictly stronger prior theorem. Choi et al. arXiv:1810.02377 Thm 5.2(2) (summarized as Thm 1.11): for any del Pezzo S, smooth anticanonical E, beta line/conic/nef-big with p_a=1 and beta != -K_S8, m^P=e(S)-eta at primitive P. S7 with beta=-K satisfies all hypotheses (ample=>nef-big, p_a=1, not S8), e=10, eta=0 by adjunction above, so m^P=10 follows by substitution. Prior need not state 'S7 -K 10' verbatim; it exhaustively covers it. DRAFT's novelty claim ('not tabulated, Thm 1 covers only line/conic/dh') confuses Thm 1.4 (P-independence/Conj 1.3, proved only for multiples of lines/conics/dh) with Thm 5.2/1.11 (primitive-point calculation, proved for all nef-big p_a<=1). The mixing part (w_out=1, x^2 mixes 2l/conics/-K) is standard wall-sum structure plus trivial line intersection, not a new lemma. See decisive_checks. value: Judged strongest headline separately from blocked target survey. The exact datum m^P=10 is a mere parameter substitution into published general formula e(S)-eta: e=10 textbook, eta=0 one-line adjunction. It is mechanically implied, computable in seconds by any future researcher from the stronger theorem, not a previously unknown invariant requiring new computation. Fails the exact-invariant test (motivated object yes, but value mechanically implied, no new method). Mixing observation w_out=1<2 is a target-failure explanation (why literal single-class chamber equation cannot isolate N_{-K}), not an independently retrievable enumerative benchmark; global wall formula already sums over all classes, and no new scattering object is constructed. No downstream DT/cluster use needs the isolated '10' beyond the general formula; no correction term with coefficient is proved. Hence textbook restatement / corollary repackaging with no independent retrieval value. FAIL.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Primitive-point invariant only (general pair (X,E)); total maximal-tangency invariant N_{-K} and P-independence for -K of S_7 remain open (Conj1); no scattering-diagram computation for (dP2,E) is claimed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
