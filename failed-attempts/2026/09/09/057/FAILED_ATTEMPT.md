# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Nilpotent-cone SL(2)-to-PGL(2) mirror interface across the ribbon spectral curve over a genus-2 curve
- **Round:** 2026-09-07-first-light-01
- **Lane:** 420
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Algebraic Geometry
- **Method:** nonabelian Hodge correspondence with ribbon-BNR spectral data and gerbe-twisted Fourier-Mukai extension analysis

## Problem

Fix the smooth projective genus-2 curve C: y^2 = x^6 - 1 and the SL(2) nilpotent cone h^{-1}(0), whose BNR spectral datum is the non-reduced ribbon R = 2C in T*C. Decide whether the smooth-locus Poincare Fourier-Mukai kernel extends across the ribbon compactified Prym to match the distinguished SL(2) nilpotent component N0 with the Donagi-Pantev predicted PGL(2) dual component M0 under gerbe twist tau, or isolate the ribbon obstruction class xi that blocks the extension.

## Attempted claim

For C: y^2 = x^6 - 1 with ribbon spectral curve R = 2C, BNR identifies the SL(2) nilpotent fiber h^{-1}(0) with fixed-determinant rank-1 torsion-free sheaves on R, and the smooth-locus Poincare kernel extends to a maximal Cohen-Macaulay kernel on the ribbon compactified-Prym pair matching the distinguished SL(2) nilpotent component N0 to the Donagi-Pantev predicted PGL(2) dual component M0 with gerbe twist tau of order 2; any failure is recorded as the explicit nonzero ribbon obstruction class xi in Ext^1 over the non-locally-free ribbon locus.

## Research outcome

Certified nonzero ribbon obstruction: for C: y^2=x^6-1, R=2C, the Poincare kernel does not extend to an MCM kernel on the ribbon compactified-Prym pair; xi!=0 via restriction pairing +1 at sigma=(1,0). Full target extension unproved (open tau-splitting reduction); pre-gate H^0-edge derivation corrected (sheaf-Ext=K^-1, dim 3) with retired files quarantined.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Route is PRESET_FALLBACK. Exact fallback_claim requires: C, R=2C, compactified-ribbon-Prym pair (Pbar,M0), test cycle sigma, proof of <xi,sigma>=+1 HENCE xi!=0 AND no MCM extension of smooth-locus Poincare kernel. Decision: NOT exactly completed — partial completion only. CERTIFIED part (correct): C: y^2=x^6-1 smooth (sympy disc 46656, separable, affine smooth; projective P(1,3,1) model smooth with 2 infinities), g=2 via 6 branch points; R=2C=V(lambda^2) with O_R=O_X/(lambda^2), N=(u)=K^-1, chi(O_R)=-4, p_a=5; sheaf-Ext^1_{O_R}(O_C,K^-1)=K^-1 because Hom differential f|->f o u is 0 (u^2=0); H^0(K^-1)=0, H^1 dim 3 via Serre h^0(K^2)=3, so global Ext^1=H^1(K^-1) dim 3; fiber 0->k->k[u]/(u^2)->k->0 nonsplit (Ann(u)=(u), mult-by-u matrix [[0,0],[1,0]] rank1 kernel span{(0,1)}), so Ext^1_A(k,k)=k generator. Re-ran all 28 artifacts: all print VERIFY_OK. Base-change O_R flat rank2 over O_C preserves exactness, so global ribbon class restricts to fiber generator; hence ribbon structure extension xi=[0->K^-1->O_R->O_C->0] is nonzero. This elementary part is correct. HEADLINE inference (incorrect/missing): Step 5 claims xi!=0 => no MCM kernel on (Pbar,M0) via S2-uniqueness and 'defect along D is exactly xi|_sigma'. No bridge is constructed: xi lives in Ext^1_{O_R}(O_C,K^-1) on the ribbon curve R, not in Ext on Pbar x M0; P_sm, U (dense line-bundle locus), D (boundary divisor), j_*P_sm, and identification of its S2-defect with xi are never defined or computed. S2-uniqueness is cited without hypotheses (normality, codim, S2 of Pbar/M0) and without proof that U is dense with complement codim>=2. The artifact verify_mcm_depth.py itself states the opposite: '[R] product-kernel MCM <=> splitting xi-twisted extension: REDUCTION (open global step)' and 'global extension not yet proved; whether the twisted kernel (with gerbe tau) splits the defect is remaining global step, NOT claimed here.' Hence twisted MCM kernel is explicitly left open, contradicting DRAFT Step 5 'hence no MCM kernel'. Naive-pushforward non-automatic != impossibility. Additional defect: verify_pairing_both.py (non-retired, still relied on for 'both points') claims canonical edge map Ext^1_R(O_C,K^-1)->H^0(C,O_C) with eps(xi0)=1_C. Under corrected sheaf-Ext=K^-1 this map does not exist (H^0(K^-1)=0); direction is reversed (connecting H^0(O_C)->Ext^1). It merely prints, proving nothing. DRAFT Sec.5 retires only two files but leaves this false mechanism in evidence. Therefore headline 'does not extend to MCM kernel' is unproved. Pairing +1 for ribbon structure does not imply FM non-extension. Exact success criterion's parenthetical 'hence ... no MCM' is logically false as stated. This is partial completion, not preset fallback. originality: Two layers distinguished. (1) Claimed novel layer (FM non-extension on ribbon compactified-Prym pair with gerbe twist): if proved it would be outside Franco 2206.12349 (verified abstract: reduced projective planar C, dense reduced singular spectra…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Full TARGET (MCM extension + N0<->M0 match with tau) not proved: tau-splitting of the defect triangle remains an open reduction. Cited-not-proved: Hitchin properness/flatness, nilpotent-cone Lagrangian, Narasimhan-Ramanan N0~=P^3, Donagi-Pantev program, Simpson transfer, Heisenberg rep existence, S2-uniqueness, Franco reduced-planar scope. Global component census and wobbly-divisor class on this C not derived. Pre-gate H^0-edge derivation retired after correction; record keeps it under output/r…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
