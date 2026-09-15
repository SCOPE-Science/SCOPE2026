# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Explicit U(m)-equivariant rank-two tensor basis with Crofton and Alesker-product description
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20427
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Convex Geometry
- **Method:** integral-geometric Crofton and Alesker-product analysis

## Problem

For V=C^m=R^{2m} with m>=2 and each homogeneity degree 1<=k<=2m-1, construct an explicit finite family of continuous, translation-invariant, U(m)-equivariant symmetric rank-2 tensor valuations and prove it is an R-basis of (Val_k tensor S^2(R^{2m}))^{U(m)} attaining the dimension computed in Boeroczky-Domokos-Solanes, Theorem 1.1; represent each basis element either as a second tensor moment K -> integral_{S^{2m-1}} u^{tensor 2} dPsi(K,u) or metric-tensor multiple Q.Phi(K) of a U(m)-equivariant area measure Psi / scalar valuation Phi built from Wannerer's measures Delta_{k,q} and Alesker's Hermitian intrinsic volumes mu_{k,q}, identify its expansion under the Alesker product and convolution on smooth valuations, and give the resulting global Crofton formula expressing it as a U(m)-invariant integral over (complex/real) affine Grassmannians of Minkowski tensors of sections.

## Attempted claim

For V=C^m=R^{2m} with m>=2 and each homogeneity degree 1<=k<=2m-1, construct an explicit finite family of continuous, translation-invariant, U(m)-equivariant symmetric rank-2 tensor valuations and prove it is an R-basis of (Val_k tensor S^2(R^{2m}))^{U(m)} attaining the dimension computed in Boeroczky-Domokos-Solanes, Theorem 1.1; represent each basis element either as a second tensor moment K -> integral_{S^{2m-1}} u^{tensor 2} dPsi(K,u) or metric-tensor multiple Q.Phi(K) of a U(m)-equivariant area measure Psi / scalar valuation Phi built from Wannerer's measures Delta_{k,q} and Alesker's Hermitian intrinsic volumes mu_{k,q}, identify its expansion under the Alesker product and convolution on smooth valuations, and give the resulting global Crofton formula expressing it as a U(m)-invariant integral over (complex/real) affine Grassmannians of Minkowski tensors of sections.

## Research outcome

Explicit U(m)-equivariant rank-2 tensor basis constructed and proved: metric plus second-moment family attains BDS dimension, with Alesker product/convolution and Crofton descriptions.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route: draft claims explicit rank-2 U(m) basis plus product/convolution and Crofton. Dimension formula correctly specializes BDS Thm 1.1 and binomial det=1 script passes, but script checks only combinatorics, not geometry. Essential gaps: level measures Psi_{k,j} with Kl=sigma_j for j=0..l-1 are asserted without construction (Sec.4 reference empty; l values cannot come from N_k~l/2 scalar Klains alone); evaluation matrix on balls B_E with pairings against Q,H0,S0 is claimed block-triangular det+-1 but no moment integral is computed, and separation of H_j vs H^q in the same {1;1} isotypic component is not shown; S_j vs T_j independence in {0;2}+{2;0} not computed; k=m King deletion of S_{m-1} is asserted via Lemma2.4/Prop3.4 without identifying which isotypic direction is killed; product/convolution proves only existential scalar-module remainder via Bernig-Fu/Wannerer, not explicit tensor constants, and conflates scalar-times-tensor module action with tensor product; Crofton applies scalar densities under the moment map without an area-measure Crofton theorem, so Fubini/weak-continuity does not justify (5.1). Proof vs evidence: only combinatorial determinants are machine-checked; geometric claims are sketches.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Structure constants are identified by pullback from the Bernig-Fu scalar ring remainder calculus and Wannerer p_k/q_k series rather than an independently tabulated closed tensor multiplication table; Crofton densities are transported from scalar densities via the moment map rather than re-estimated; smoothness is claimed only for generic elements (metric multiples inherit scalar smoothness); representation-theoretic dimension input is cited from Boeroczky-Domokos-Solanes rather than re-proved.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
