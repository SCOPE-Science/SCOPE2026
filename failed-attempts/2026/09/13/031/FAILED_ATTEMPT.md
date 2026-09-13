# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Finite-state monotone MFG exponential turnpike
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1533
- **Disposition:** NO_RESULT
- **Domain:** finite-state mean-field games
- **Method:** Lasry-Lions duality and forward-backward ODE stability

## Problem

Let d>=3 and S_d be the probability simplex in R^d. Consider the continuous-time finite-state mean-field game forward-backward system on horizon [0,T] with controlled jump rates, separable convex Hamiltonian H^i, Lasry-Lions strictly monotone running coupling F:S_d->R^d with modulus c_F>0 and terminal coupling G with modulus >=0, both Lipschitz, and admissible rates uniformly bounded above and bounded below by a>0. Let (u^T(t),m^T(t)) be any classical solution starting from m_0 in the interior of S_d, and let (ubar,mbar,lambdabar) be the associated stationary ergodic triple. Prove or disprove that there exist finite constants C>=1 and gamma>0 depending only on d,c_F,Lipschitz bounds,a and the interior distance of m_0, but not on T or t, such that for all T>=1 and all t in [0,T], |m^T(t)-mbar|+|u^T(t)-ubar-lambdabar*(T-t)*1|<=C*(exp(-gamma*t)+exp(-gamma*(T-t))). A complete answer is either a rigorous proof of the stated two-sided exponential bound with explicit C,gamma, or an explicit choice of d,F,G,H,m_0,T,t violating it with all assumptions verified.

## Attempted claim

Let d>=3 and S_d be the probability simplex in R^d. Consider the continuous-time finite-state mean-field game forward-backward system on horizon [0,T] with controlled jump rates, separable convex Hamiltonian H^i, Lasry-Lions strictly monotone running coupling F:S_d->R^d with modulus c_F>0 and terminal coupling G with modulus >=0, both Lipschitz, and admissible rates uniformly bounded above and bounded below by a>0. Let (u^T(t),m^T(t)) be any classical solution starting from m_0 in the interior of S_d, and let (ubar,mbar,lambdabar) be the associated stationary ergodic triple. Prove or disprove that there exist finite constants C>=1 and gamma>0 depending only on d,c_F,Lipschitz bounds,a and the interior distance of m_0, but not on T or t, such that for all T>=1 and all t in [0,T], |m^T(t)-mbar|+|u^T(t)-ubar-lambdabar*(T-t)*1|<=C*(exp(-gamma*t)+exp(-gamma*(T-t))). A complete answer is either a rigorous proof of the stated two-sided exponential bound with explicit C,gamma, or an explicit choice of d,F,G,H,m_0,T,t violating it with all assumptions verified.

## Research outcome

Target blocked: candidate center/resonance disproof collapsed under sign correction and closed-form BVP analysis; no proof or verified violation obtained, so clean exit with no result.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The investigation refuted its own candidate disproof routes (sign-corrected linearization is dichotomic, critical BVP decays, energy identity blocks cycles) but did not resolve the target in either direction. The full two-sided exponential turnpike question for d>=3 finite-state monotone MFGs remains open; no proof and no verified violation was produced.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The investigation refuted its own candidate disproof routes (sign-corrected linearization is dichotomic, critical BVP decays, energy identity blocks cycles) but did not resolve the target in either direction. The full two-sided exponential turnpike question for d>=3 finite-state monotone MFGs remains open; no proof and no verified violation was produced.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
