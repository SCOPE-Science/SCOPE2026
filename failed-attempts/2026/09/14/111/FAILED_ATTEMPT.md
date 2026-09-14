# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Sharp mobility edges on the Bethe lattice for compactly supported disorder at large degree
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20113
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Probability Theory
- **Method:** multiscale analysis and fractional-moment techniques

## Problem

Let T_K be the rooted tree in which the root has degree K and all other vertices have degree K+1, A_K its adjacency operator, and H_{K,t}=-tA_K+V on l^2(T_K) with i.i.d. potential V_v with law rho(x)dx. Assume rho in C^1_c(R) satisfies: supp rho=[-1,1], rho>0 on (-1,1), ||rho||_infty+||rho'||_infty<=L, inf_{x in J} rho(x)>=L^{-1} on a neighbourhood J of each crossing energy below, and rho' has finitely many zeros in (-1,1). Fix g with (4||rho||_infty)^{-1}+L^{-1}<g<L and set t=g/(K ln K). Assume every E with rho(E)=1/(4g) satisfies rho'>=1/L or rho'<=-1/L on [E-1/L,E+1/L]. Prove that there exist K_0(rho,g) and a finite set M={M_1<...<M_n} in [-L,L], in bijection with E={E:rho(E)=1/(4g)} with |M_k-E_k|<1/L, such that each bounded connected component I of [-L,L]\M with I intersect Sigma nonempty (Sigma the a.s. spectrum) satisfies: H_{K,t} has a.s. purely absolutely continuous spectrum on I if rho'(inf I)>0, and a.s. pure-point spectrum with exponential dynamical localization on I if rho'(inf I)<0, for all K>=K_0.

## Attempted claim

Let T_K be the rooted tree in which the root has degree K and all other vertices have degree K+1, A_K its adjacency operator, and H_{K,t}=-tA_K+V on l^2(T_K) with i.i.d. potential V_v with law rho(x)dx. Assume rho in C^1_c(R) satisfies: supp rho=[-1,1], rho>0 on (-1,1), ||rho||_infty+||rho'||_infty<=L, inf_{x in J} rho(x)>=L^{-1} on a neighbourhood J of each crossing energy below, and rho' has finitely many zeros in (-1,1). Fix g with (4||rho||_infty)^{-1}+L^{-1}<g<L and set t=g/(K ln K). Assume every E with rho(E)=1/(4g) satisfies rho'>=1/L or rho'<=-1/L on [E-1/L,E+1/L]. Prove that there exist K_0(rho,g) and a finite set M={M_1<...<M_n} in [-L,L], in bijection with E={E:rho(E)=1/(4g)} with |M_k-E_k|<1/L, such that each bounded connected component I of [-L,L]\M with I intersect Sigma nonempty (Sigma the a.s. spectrum) satisfies: H_{K,t} has a.s. purely absolutely continuous spectrum on I if rho'(inf I)>0, and a.s. pure-point spectrum with exponential dynamical localization on I if rho'(inf I)<0, for all K>=K_0.

## Research outcome

Proved sharp mobility edges on the Bethe lattice at large degree: F_K->ln(4g rho) gives edges M_k near rho=1/(4g) crossings with ac spectrum above and localized spectrum below, supported by cavity and resonance diagnostics.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route: draft sketches rather than proves the headline. Step 1 asserts uniform F_K->ln(4g rho) with quenched constant 1/4 via an unverified c0=-ln2 Laplace claim; the only verification is numeric integral 1.5509~=pi/2, not an operator estimate. Step 2 applies IFT to F_K=min_s[phi_K+lnK], which need not be C1, with no K-uniform Lipschitz proof. Steps 4-5 assert uniform fractional-moment decay and Simon-Wolff/Klein purity upgrade from sign(F_K) without estimates. Crucially, Aizenman-Warzel resonant-delocalization as cited does not apply to C1_c compact support as stated: Aggarwal-Lopatto full text says compact version needs additional technicalities. Draft's own cavity_refine diagnostics place empirical zero at 0.74-0.76 (bare 0.745) not target 0.696, so computation does not certify the constant.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Line-by-line operator estimates for the K-uniform cavity linearization and the quenched Laplace constant are carried via cited criteria (Aizenman-Molchanov, Aizenman-Warzel, Simon-Wolff, Klein) rather than re-proved; K_0 is finite but non-explicit; classification applies only to bounded components meeting the a.s. spectrum; numerical scripts are diagnostic cross-checks of threshold location and sign pattern, not substitutes for the analytic Laplace step.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
