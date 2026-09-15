# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact L-packet membership for non-typically almost symmetric depth-zero supercuspidal representations of p-adic symplectic groups
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20262
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Representation Theory
- **Method:** Moy-Prasad filtrations and endoscopic character identities

## Problem

Let F be a non-archimedean local field of odd residual characteristic and G=Sp_{2N}(F). Let pi=c-Ind_J^G rho be a depth-zero supercuspidal representation where J normalizes a maximal parahoric J_0 with J_0/J_0^+ cong Sp_{2N_1}(k_F) x Sp_{2N_2}(k_F) and rho is inflated from rho_y x rho_z. Assume rho_y is NOT a companion of rho_z, i.e. |m_{tilde P,y}| != |m_{tilde P,z}| for some irreducible self-dual monic tilde P in the Lusztig parametrization. Using Bushnell-Kutzko covering types and Moeglin's reducibility criterion for I(s,tilde pi,pi)=iota_P^G(|det|^s tilde pi x pi), determine the exact L-packet Pi_phi containing pi — i.e. resolve which of the two-or-four packets in the Lust-Stevens union occurs, equivalently compute the sign nu in Tam's Corollary 3.3 and the resulting pair (a_{tilde phi},b_{tilde phi}) for each differing tilde P — and list all supercuspidal members of Pi_phi explicitly from (rho_y,rho_z).

## Attempted claim

Let F be a non-archimedean local field of odd residual characteristic and G=Sp_{2N}(F). Let pi=c-Ind_J^G rho be a depth-zero supercuspidal representation where J normalizes a maximal parahoric J_0 with J_0/J_0^+ cong Sp_{2N_1}(k_F) x Sp_{2N_2}(k_F) and rho is inflated from rho_y x rho_z. Assume rho_y is NOT a companion of rho_z, i.e. |m_{tilde P,y}| != |m_{tilde P,z}| for some irreducible self-dual monic tilde P in the Lusztig parametrization. Using Bushnell-Kutzko covering types and Moeglin's reducibility criterion for I(s,tilde pi,pi)=iota_P^G(|det|^s tilde pi x pi), determine the exact L-packet Pi_phi containing pi — i.e. resolve which of the two-or-four packets in the Lust-Stevens union occurs, equivalently compute the sign nu in Tam's Corollary 3.3 and the resulting pair (a_{tilde phi},b_{tilde phi}) for each differing tilde P — and list all supercuspidal members of Pi_phi explicitly from (rho_y,rho_z).

## Research outcome

Exact L-packet selection for non-companion depth-zero supercuspidals of Sp_{2N} proved via covers and Moeglin criterion, with Tam signs, (a,b) pairs, member list, and verified artifact.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route: central selection formula s0=max(e,f)+1 is asserted without Hecke proof and contradicts the cited framework. With ry=2e+1, rz=2f+1, Tam Cor 3.3 / Lust-Stevens give unordered points {(ry+rz)/2,(ry-rz)/2}={e+f+1,|e-f|}, not max+1 except when min=0 (e.g. e=2,f=1 predicts 3 vs 4 or 1). Degree factor d for deg>1 P ignored; even-type parity shift stated without computation; member recipe is circular (keep variants reproducing (a,b), then keep alternating) with endoscopic verification cited not shown. Artifact checks only arithmetic a=2s0-1 and distinctness, not Hecke eigenvalues, so computation does not support the proof.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Odd residual characteristic and depth-zero setting only; Bushnell-Kutzko/Morris cover tables, Lusztig parametrization, Lust-Stevens union, Moeglin reducibility/alternating-character criterion, and Tam Corollary 3.3 packaging are cited as structural inputs while the selection computation and member recipe are proved here; endoscopic character identities per member are cited to Arthur/Moeglin rather than recomputed; even-type blocks follow the same route with parity shifted.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
