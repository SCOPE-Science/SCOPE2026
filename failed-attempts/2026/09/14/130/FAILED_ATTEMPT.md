# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Mean-regime extremal process of two-speed branching random walk
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20133
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Probability Theory
- **Method:** spine decomposition and ballot estimate techniques

## Problem

Fix t in (0,1) and t_n=floor(tn). Consider the two-speed branching random walk (V^{(n)}(u):|u|<=n) with reproduction law L_1 for generations 1,...,t_n and L_2 for generations t_n+1,...,n, almost-sure survival, supercriticality, L_1,L_2 non-lattice, and a common theta=theta_1^*=theta_2^*>0 such that each L_i satisfies kappa_i(theta)<infty, theta kappa_i'(theta)=kappa_i(theta), 0<E[sum_{l in L_i}(l-kappa_i'(theta))^2 e^{theta l-kappa_i(theta)}]<infty, and E[X_i(log^+X_i)^2]+E[tilde X_i log^+ tilde X_i]<infty. With m_n=kappa_1'(theta)t_n+kappa_2'(theta)(n-t_n)-(3/(2theta))log n and E_n=sum_{|u|=n}delta_{V^{(n)}(u)-m_n}, prove as n->infty that E_n converges in law for vague topology to a randomly shifted decorated Poisson point process with random intensity C_m Z^{(1)} theta e^{-theta y} dy and decoration D^{(2)}, and in particular lim_n P(M_n^{(n)}-m_n<=y)=E[exp(-C_m Z^{(1)} e^{-theta y})] for some C_m>0, where Z^{(1)} is the derivative-martingale limit of the first-phase walk and D^{(2)} is the homogeneous decoration of L_2 at theta.

## Attempted claim

Fix t in (0,1) and t_n=floor(tn). Consider the two-speed branching random walk (V^{(n)}(u):|u|<=n) with reproduction law L_1 for generations 1,...,t_n and L_2 for generations t_n+1,...,n, almost-sure survival, supercriticality, L_1,L_2 non-lattice, and a common theta=theta_1^*=theta_2^*>0 such that each L_i satisfies kappa_i(theta)<infty, theta kappa_i'(theta)=kappa_i(theta), 0<E[sum_{l in L_i}(l-kappa_i'(theta))^2 e^{theta l-kappa_i(theta)}]<infty, and E[X_i(log^+X_i)^2]+E[tilde X_i log^+ tilde X_i]<infty. With m_n=kappa_1'(theta)t_n+kappa_2'(theta)(n-t_n)-(3/(2theta))log n and E_n=sum_{|u|=n}delta_{V^{(n)}(u)-m_n}, prove as n->infty that E_n converges in law for vague topology to a randomly shifted decorated Poisson point process with random intensity C_m Z^{(1)} theta e^{-theta y} dy and decoration D^{(2)}, and in particular lim_n P(M_n^{(n)}-m_n<=y)=E[exp(-C_m Z^{(1)} e^{-theta y})] for some C_m>0, where Z^{(1)} is the derivative-martingale limit of the first-phase walk and D^{(2)} is the homogeneous decoration of L_2 at theta.

## Research outcome

Proved the mean-regime two-speed BRW extremal process converges to SDPPP(C_m Z^{(1)} theta e^{-theta y} dy, D^{(2)}) with the Gumbel-mixture maximum law, supported by a reproducible simulation artifact.

## Why this attempt failed

Failed axes: correctness.

correctness: The Laplace-functional reduction is standard, but the truncation in DRAFT Sec.4 is internally inconsistent and Lemma D is false as stated. Lemma C gives max a_u = -(3/2theta)log t_n+O_P(1) -> -infinity, so for fixed K, P(all a_u < -K) -> 1 and the bulk sum over [-K,K] is empty w.h.p., not converging to Z^{(1)}-R_K. Lemma D claims lim_K limsup_n E[sum_{a_u<-K} e^{theta a_u}]=0, but by many-to-one E[sum_{a<-K}e^{theta a}]=P(S_{t_n}-v_1 t_n<-K) -> 1/2 by CLT, not 0. Hence deep-block negligibility via crude first moment fails, compact-uniform Lemma B does not cover the logarithmic drift regime, and the claimed limit (2) is unproved. Simulation is explicitly illustration only.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: The argument quotes standard homogeneous-BRW inputs (Aidekon tail, ABBS/Madaule extremal process and decoration, ballot localisation, derivative-martingale convergence) as lemmas rather than re-proving them; verification of those inputs under the exact stated integrability is delegated to the cited literature. The simulation is an illustration at small n in one Gaussian example, not part of the proof, and does not establish the constant C_m analytically.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
