# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Second-order window law for standard 2-neighbour bootstrap in 4D
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1454
- **Disposition:** NO_RESULT
- **Domain:** bootstrap percolation
- **Method:** critical droplet first-passage and quantile window

## Problem

Fix the 4-dimensional torus T_n^4=(Z/nZ)^4 with the standard 2-neighbour rule (a healthy vertex becomes infected iff at least 2 of its 8 nearest neighbours are infected; infected stay infected; initial set i.i.d. Bernoulli(p)). Let lam4>0 be the Balogh-Bollobas-Duminil-Copin-Morris leading constant for (d,r)=(4,2), so p_c=(lam4+o(1))/(log n)^3. Prove or disprove the following second-order window law W2: with explicit tau0=3 (the (d-1) edge-isoperimetric log-log correction from the critical-droplet first-passage heuristic), the alpha-quantiles p_alpha(n)=inf{p:P_p(full percolation)>=alpha} satisfy (p_{0.9}(n)/p_{0.1}(n)-1)*(log n)/(log log n)->tau0/3=1 as n->infinity, and moreover the minimal side-length m_c(n) of an internally spanned cubical droplet at p=p_{1/2}(n) satisfies m_c(n)/(log n)->A4 for an explicit A4>0 determined by the same droplet cost, expanding to the whole torus with conditional probability >=1-n^{-2} while no such droplet of side floor((A4/2)log n) exists w.h.p. at p_{0.1}(n). Scope: fixed d=4, n->infinity, p=p(n)->0. A complete answer is a rigorous proof of the stated second-order ratio limit plus both droplet calibration bounds, or a rigorous disproof via an explicit infinite sequence n_k with the ratio limit violating [0.5,1.5] or either droplet bound failing.

## Attempted claim

Fix the 4-dimensional torus T_n^4=(Z/nZ)^4 with the standard 2-neighbour rule (a healthy vertex becomes infected iff at least 2 of its 8 nearest neighbours are infected; infected stay infected; initial set i.i.d. Bernoulli(p)). Let lam4>0 be the Balogh-Bollobas-Duminil-Copin-Morris leading constant for (d,r)=(4,2), so p_c=(lam4+o(1))/(log n)^3. Prove or disprove the following second-order window law W2: with explicit tau0=3 (the (d-1) edge-isoperimetric log-log correction from the critical-droplet first-passage heuristic), the alpha-quantiles p_alpha(n)=inf{p:P_p(full percolation)>=alpha} satisfy (p_{0.9}(n)/p_{0.1}(n)-1)*(log n)/(log log n)->tau0/3=1 as n->infinity, and moreover the minimal side-length m_c(n) of an internally spanned cubical droplet at p=p_{1/2}(n) satisfies m_c(n)/(log n)->A4 for an explicit A4>0 determined by the same droplet cost, expanding to the whole torus with conditional probability >=1-n^{-2} while no such droplet of side floor((A4/2)log n) exists w.h.p. at p_{0.1}(n). Scope: fixed d=4, n->infinity, p=p(n)->0. A complete answer is a rigorous proof of the stated second-order ratio limit plus both droplet calibration bounds, or a rigorous disproof via an explicit infinite sequence n_k with the ratio limit violating [0.5,1.5] or either droplet bound failing.

## Research outcome

Target blocked after three concrete routes (first-passage, variational hierarchy, bounded computation); no credible continuation and no independently valuable emergent finding, so clean exit with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The second-order quantile-ratio constant and sharp droplet calibration for 4D 2-neighbour bootstrap remain open: BBDM theory gives only the leading constant with polylog window gaps, the droplet quantity m_c needs disambiguation, and asymptotics at n~e^20 are unreachable by finite computation.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The second-order quantile-ratio constant and sharp droplet calibration for 4D 2-neighbour bootstrap remain open: BBDM theory gives only the leading constant with polylog window gaps, the droplet quantity m_c needs disambiguation, and asymptotics at n~e^20 are unreachable by finite computation.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
