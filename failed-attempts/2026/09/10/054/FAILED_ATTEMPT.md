# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Near-critical noise-sensitivity window for planar FK percolation at q=2 via one-scale RSW plus OSSS and four-arm quasi-multiplicativity
- **Round:** 2026-09-07-first-light-01
- **Lane:** 633
- **Disposition:** NO_RESULT
- **Domain:** Statistical Mechanics
- **Method:** RSW box-crossing with OSSS influence bounds and arm-event quasi-multiplicativity comparison

## Problem

Pin a near-critical noise-sensitivity window for planar FK percolation at q=2 on Z^2 using RSW box-crossing plus OSSS influence and four-arm quasi-multiplicativity: prove a new arm-exponent/influence lower bound forcing noise sensitivity of 2:1 rectangle crossings via a one-scale OSSS lemma with logged RSW crossings, or else exhibit a certified stable-crossing witness with explicit pivotal-tail cutoff that isolates the obstruction.

## Attempted claim

For planar FK percolation with q=2 on Z^2 at p_c(2)=sqrt(2)/(1+sqrt(2)), let f_n be left-right crossing of R_n=[0,2n]x[0,n]. Prove {f_n} is noise sensitive by establishing from a logged RSW lower bound inf_n P_{p_c}(cross(R_n))>=c_RSW>0 plus an explicit exploration algorithm with revealment delta_n<=n^{-gamma} (gamma>0 stated) that the BKS/OSSS criterion diverges: sum_e Inf_e(f_n)->infinity via an alternating four-arm lower bound pi_4(r,R)>=(r/R)^{2-eta} with explicit eta>0 over one dyadic window, hence Cov(f_n(omega),f_n(omega^{eps}))->0 for every fixed eps>0.

## Research outcome

Target (FK q=2 noise sensitivity via RSW+OSSS+four-arm window) BLOCKED on dependent-measure/noise-operator obstruction plus missing finite-scale constants, confirmed by a 4-part recovery test. Revealed fallback (I(f_128)>=8 at exactly 256x128) ATTEMPTED_AND_BLOCKED via three bounded replayable routes: FKG-gluing gap table (max 5.70<8), exact small-box enumeration (E<=17 only, target needs E=65920), Russo slope reduction (needs F'(p_c)>=8.242641, no citable floor). No valuable original increment; clean exit with audit artifacts preserved.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['Target Cov->0/BKS-divergence proof not established: product-noise operator misspecified for dependent FK q=2 and finite-scale constants (c_RSW numeric, gamma, eta) uncitable.', "Exact fallback I(f_128)>=8 not established: honest gluing peaks at 5.70<8, exact enumeration reaches only E<=17 vs required E=65920, Russo reduction needs uncitable slope F'(p_c)>=8.242641.", 'Small-box exact values (I=1.53 at 2x1, I=1.97 at 3x2) and the gluing/slope tables are logged as routine byproducts, not claimed as emergent findings.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['Target Cov->0/BKS-divergence proof not established: product-noise operator misspecified for dependent FK q=2 and finite-scale constants (c_RSW numeric, gamma, eta) uncitable.', "Exact fallback I(f_128)>=8 not established: honest gluing peaks at 5.70<8, exact enumeration reaches only E<=17 vs required E=65920, Russo reduction needs uncitable slope F'(p_c)>=8.242641.", 'Small-box exact values (I=1.53 at 2x1, I=1.97 at 3x2) and the gluing/slope tables are logged as routine byproducts, not claime…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
