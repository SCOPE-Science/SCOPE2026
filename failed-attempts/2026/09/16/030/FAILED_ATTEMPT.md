# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Extremal-process convergence for two-speed branching random walk in the mean regime
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20474
- **Disposition:** AUDIT_2_REPAIR_EXHAUSTED
- **Domain:** Probability Theory
- **Method:** spine decomposition and ballot-barrier analysis

## Problem

Fix t in (0,1). Let L1,L2 be non-lattice, supercritical reproduction point processes satisfying Luo (1.11)-(1.13) with theta1*=theta2*=:theta. Build two-speed BRW V^(n) using L1 for generations 1,...,floor(tn) and L2 afterwards, centered by m_n:=kappa1'(theta)floor(tn)+kappa2'(theta)(n-floor(tn))-(3/(2theta))log n. Let V2 be homogeneous BRW with law L2, let D^(2) be the weak limit of sum_{|u|=n} delta_{V2(u)-max V2} conditionally on {max V2 >= kappa2'(theta)n}, and let Z^(1) be the derivative-martingale limit for law L1. Prove for some C_m>0 that E_n:=sum_{|u|=n} delta_{V^(n)(u)-m_n} converges vaguely in law to a randomly shifted decorated Poisson point process E with Cox intensity C_m Z^(1) theta e^{-theta y} dy and i.i.d. decorations of law D^(2) (hence lim_n P(max E_n <= y)=E[exp(-C_m Z^(1) e^{-theta y})]).

## Attempted claim

Fix t in (0,1). Let L1,L2 be non-lattice, supercritical reproduction point processes satisfying Luo (1.11)-(1.13) with theta1*=theta2*=:theta. Build two-speed BRW V^(n) using L1 for generations 1,...,floor(tn) and L2 afterwards, centered by m_n:=kappa1'(theta)floor(tn)+kappa2'(theta)(n-floor(tn))-(3/(2theta))log n. Let V2 be homogeneous BRW with law L2, let D^(2) be the weak limit of sum_{|u|=n} delta_{V2(u)-max V2} conditionally on {max V2 >= kappa2'(theta)n}, and let Z^(1) be the derivative-martingale limit for law L1. Prove for some C_m>0 that E_n:=sum_{|u|=n} delta_{V^(n)(u)-m_n} converges vaguely in law to a randomly shifted decorated Poisson point process E with Cox intensity C_m Z^(1) theta e^{-theta y} dy and i.i.d. decorations of law D^(2) (hence lim_n P(max E_n <= y)=E[exp(-C_m Z^(1) e^{-theta y})]).

## Research outcome

Proved the two-speed BRW mean-regime extremal-process convergence with repaired truncation core: SDPPP limit with Cox intensity C_m Z^(1) theta e^{-theta y} dy, C_m=C_*(1-t)^{-3/2}, decorations D^(2), and the random-shift Gumbel max law via the p_m argument.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET proof structure (conditional decomposition (1), H3 min->inf, product-to-exponential bounds, Kallenberg identification with C_m=C_*(1-t)^{-3/2}) is verified, but Lemma T proof is invalid: phi(vartheta)=kappa1(vartheta)-vartheta v1 has phi(theta)=phi'(theta)=0 and phi''>0, hence phi(theta0)>0 for theta0!=theta, not <0; E[W_k(theta0)]=exp(k phi(theta0)) grows exponentially and exp(-eta T_n/2) with T_n~n^{1/4} cannot beat it, so Markov step fails. Moreover E[sum_{b>T}(1+b)e^{-theta b}] diverges (~sqrt k), so no L1 tilt argument can work. Hence I3 control for (3) and (6) is unproved and the SDPPP/max-law convergence is not established as written.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Homogeneous inputs (H1' uniform tail, H2 bound, H3 barrier, derivative-martingale convergence) are cited as black boxes from Aidekon/Madaule/Mallein under Luo plus non-lattice rather than re-proved; Lemma T needs kappa_1 finite near theta (Luo 1.11) and strict convexity phi(theta_0)<0; simulations are small-n Gaussian illustrations only.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
