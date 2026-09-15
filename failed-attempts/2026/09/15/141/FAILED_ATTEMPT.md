# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Stability threshold for join-model Mayer–Vietoris spectral sequences of Vietoris–Rips filtrations of compact metric spaces
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20381
- **Disposition:** AUDIT_2_REJECT
- **Domain:** Algebraic Topology
- **Method:** multiparameter persistence stability and spectral-sequence analysis

## Problem

Let X,Y be compact metric spaces with Gromov–Hausdorff distance d_GH(X,Y)<varepsilon, equipped with finite Borel partitions P,Q of mesh at most mu and nerves Delta_P,Delta_Q of uniformly bounded dimension, and let VR_*(X),VR_*(Y) denote the open Vietoris–Rips filtrations (simplex present at scale r iff strict diameter <2r) with field coefficients. Let E(J^{VR(X)}_P) and E(J^{VR(Y)}_Q) be the persistent join-diagram Mayer–Vietoris spectral sequences with E^1_{p,q}=direct sum over sigma in (Delta_P)_p of PH_q(J^P_*(sigma)) converging to PH_{p+q}(VR_*(X)) of Pennig–Torras Lemma 3.2 and Example 3.4, and analogously for Y. Do there exist explicit constants C>=1 and varepsilon_0=varepsilon_0(mu,covering data)>0 such that whenever varepsilon+mu<varepsilon_0 the two spectral sequences are (C(varepsilon+mu),1)-interleaved via filtration-preserving double-complex morphisms in the sense of Pennig–Torras Proposition 6.4 / Theorem 6.5 applied over a common refinement of Delta_P,Delta_Q, hence (C(varepsilon+mu),2)-interleaved, and does this bound persist when X,Y are infinite compact where H_*(VR(X,r)) need not be pointwise finite-dimensional?

## Attempted claim

Let X,Y be compact metric spaces with Gromov–Hausdorff distance d_GH(X,Y)<varepsilon, equipped with finite Borel partitions P,Q of mesh at most mu and nerves Delta_P,Delta_Q of uniformly bounded dimension, and let VR_*(X),VR_*(Y) denote the open Vietoris–Rips filtrations (simplex present at scale r iff strict diameter <2r) with field coefficients. Let E(J^{VR(X)}_P) and E(J^{VR(Y)}_Q) be the persistent join-diagram Mayer–Vietoris spectral sequences with E^1_{p,q}=direct sum over sigma in (Delta_P)_p of PH_q(J^P_*(sigma)) converging to PH_{p+q}(VR_*(X)) of Pennig–Torras Lemma 3.2 and Example 3.4, and analogously for Y. Do there exist explicit constants C>=1 and varepsilon_0=varepsilon_0(mu,covering data)>0 such that whenever varepsilon+mu<varepsilon_0 the two spectral sequences are (C(varepsilon+mu),1)-interleaved via filtration-preserving double-complex morphisms in the sense of Pennig–Torras Proposition 6.4 / Theorem 6.5 applied over a common refinement of Delta_P,Delta_Q, hence (C(varepsilon+mu),2)-interleaved, and does this bound persist when X,Y are infinite compact where H_*(VR(X,r)) need not be pointwise finite-dimensional?

## Research outcome

Repaired proof: explicit threshold C=5, eps0=min{1,lambda/10} from K0-independent cover data, with refinement lemma, acyclic carriers, and infinite-compact convergence; (delta,1) then (delta,2) interleaving.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route: proof of explicit C=5, eps0=min{1,lambda/10} with (delta,1) hence (delta,2) over common refinement W plus infinite-compacta extension was verified for shift arithmetic (2K0 round trip + 3K0 sweep = 5K0; delta<lambda/2; Lemma 6.1 finite-p-length convergence and 5-lemma need no pfd) and artifact re-execution passes with Part B honestly labeled ILLUSTRATION ONLY (inequality engine, not spectral transfer). Two essential inferences fail. (A) Lemma 2.2/Section 3 existence: for every thickened-overlap vertex w=(i,j) with W_{i,j}=U^0_i cap V^0_j != empty in host Z, a pair (x_w,y_w) in R with block membership is asserted under K0<rho, but thickened overlap (radius rho=0.1 fixed) does not imply an R-pair (proximity eps~0.002): the triangle bound gives dist~eps+2rho>rho, so many W-vertices have no R-pair and the diameter chase has no carrier. Restricting to R-matched vertices breaks the claimed pullback convergence to PH(VR) (surjectivity without fiber-contractibility/goodness, never proved for arbitrary Borel partitions). (B) Page scope: Prop 6.4/Thm 6.5 give (delta,1) for pullback diagrams over the same K=Delta_W, not for the original E(J_P),E(J_Q) over Delta_P,Delta_Q with different nerves; refinement invariance (Pennig-Torras Sec.7) yields at best page 2, so the headline (delta,1) for the originals is not established. The defects change hypotheses/conclusions and need new refinement/fiber machinery, not a bounded presentation fix.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Pennig-Torras numbering taken from target statement, only standard content used; optimality of C=5 not claimed; uniform nerve-dimension bound D and fixed-cover Lebesgue lambda essential; Part B artifact is explicitly illustration of the inequality engine, not the spectral transfer.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
