# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Explicit long-time RATTLE energy bound for librational double pendulum
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1316
- **Disposition:** AUDIT_1_REJECT
- **Domain:** constrained geometric integration
- **Method:** RATTLE backward-error and symplectic conservation

## Problem

For the planar Cartesian double pendulum DAE family with masses m1=m2=1, rod lengths L1=L2=1, gravity g=9.81, holonomic constraints g1(q)=|q1|^2-1=0 and g2(q)=|q2-q1|^2-1=0, separable Hamiltonian H(q,p)=|p1|^2/2+|p2|^2/2+U(q), and consistent librational initial data with energy H0 in [-12,-8] and angular velocities bounded by 2, let (qn,pn) be the RATTLE (2-stage Lobatto IIIA-IIIB, order 2) sequence with fixed step h in (0,0.01]: prove or disprove that there exist explicit constants C,c,h0>0 independent of h and of the initial point in the stated set such that sup_{n: n h <= c h^{-2}} |H(qn,pn)-H0| <= C h^2 and the constraint-defect ledger inequality |H(qn,pn)-H0| <= C1 h^2 + C2 max_{k<=n}(|g(qk)|+|G(qk)M^{-1}pk|) holds with explicit C1,C2, where G is the constraint Jacobian. A complete answer is either a rigorous proof of both bounds with stated constants and horizon, or an explicit consistent initial datum plus step-size sequence violating the O(h^2) uniform bound with certified defect accounting.

## Attempted claim

For the planar Cartesian double pendulum DAE family with masses m1=m2=1, rod lengths L1=L2=1, gravity g=9.81, holonomic constraints g1(q)=|q1|^2-1=0 and g2(q)=|q2-q1|^2-1=0, separable Hamiltonian H(q,p)=|p1|^2/2+|p2|^2/2+U(q), and consistent librational initial data with energy H0 in [-12,-8] and angular velocities bounded by 2, let (qn,pn) be the RATTLE (2-stage Lobatto IIIA-IIIB, order 2) sequence with fixed step h in (0,0.01]: prove or disprove that there exist explicit constants C,c,h0>0 independent of h and of the initial point in the stated set such that sup_{n: n h <= c h^{-2}} |H(qn,pn)-H0| <= C h^2 and the constraint-defect ledger inequality |H(qn,pn)-H0| <= C1 h^2 + C2 max_{k<=n}(|g(qk)|+|G(qk)M^{-1}pk|) holds with explicit C1,C2, where G is the constraint Jacobian. A complete answer is either a rigorous proof of both bounds with stated constants and horizon, or an explicit consistent initial datum plus step-size sequence violating the O(h^2) uniform bound with certified defect accounting.

## Research outcome

Proved the uniform O(h^2) RATTLE long-time energy bound to horizon c/h^2 plus the constraint-defect ledger with explicit certified constants (h0=1e-9, c=1e-23, C=C1=1e16, C2=200).

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: TARGET route (report declares claim_route TARGET; topic has no fallback_claim, so audit normally against the admitted target). Lemma 1-2 arithmetic rechecks pass (lambda_min=6-2sqrt(5)>1.52, tube perturbation <0.69<lambda_min/2, trapping numbers reproduce: C*h0^2=0.01, Pworst~6.55<8). But Lemma 3, the load-bearing backward-error step, is not proved: L1=30000>=sup||f'|| is assumed, not derived (Cauchy from the claimed complex majorant M=3000/R=0.02 gives M/R=150000>L1, so L1 needs a separate real-tube proof that is absent); the envelopes B2=12*10*L1*M*(1+L1), B4=12*10*L1^4*M^2 and Ka=1e38 from 2000*M^7/R^6 are asserted B-series/Cauchy majorants with no explicit constrained-RATTLE H2/H4 formulas, no verified analytic-continuation bound for GGT^{-1} on the complex R-polydisc (real Frobenius perturbation argument does not transfer), and no justification that unconstrained Thm IX.8.1 applies to the DAE multiplier flow. Symmetry promotion of the residual from O(h^5) to O(h^6) for the constrained map is asserted. Lemma 4 invokes Newton-Kantorovich with no Kantorovich constants or contraction verification, and the off-manifold ledger constant C2=200 cites 'Lemma 5.3 of the supplement', which is not in the inputs, so part (B) for inexact sequences is unproved (on the exact sequence defects are zero, making (B) a vacuous corollary of (A)). final_certificate.py verifies only conditional arithmetic (ALL CHECKS PASSED subject to the assumed L1/D/factor-10 inputs; it errored on output path in this workspace, arithmetic reproduced manually) and rattle_check.py is explicitly non-load-bearing and runs at h=0.005-0.01, outside the theorem scope h<=1e-9. Hence the proof as submitted does not establish the headline. originality: Fused retrieval (SerpBase/OpenAlex/Crossref/OpenAIRE, all providers ok, no partial failure) finds the qualitative headline — order-2 RATTLE/SHAKE (Lobatto IIIA-IIIB) long-time O(h^2) energy conservation over polynomial (indeed exponentially long) horizons for holonomic constrained Hamiltonians — is the standard constrained backward-error theorem: Hairer 2003 'Global modified Hamiltonian for constrained symplectic integrators', Leimkuhler-Reich Thm 7.2, Hairer-Lubich-Wanner Chap. VII, plus Li-Wang 2023 alpha-PRK extensions. Those prove a strictly stronger fact (near-conservation over exponentially long times) for the same method class under the same compactness/regularity hypotheses, so the submitted c/h^2-horizon bound is a weak corollary/repackaging with system-specific loose majorants (C=1e16, c=1e-23) for a textbook double-pendulum example. No source states these exact degenerate numbers, but a prior source need not repeat the headline verbatim: substantive implication by a stronger known theorem defeats originality. The exact-parameter/table search found no database entry, which does not establish priority given the covering general theory. value: Even taken as correct and new-as-numbers, the headline is not independently w…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Constants are valid but very conservative (Cauchy/B-series majorants inflate C to 1e16 while numerics show ~79); the horizon c/h^2 at h0=1e-9 is only 1e-5 time units (1e4 steps), growing as c/h^2 for smaller h; the analyzed sequence is exact-arithmetic RATTLE (floating-point roundoff would enter additively through the C2 ledger term); librational set only (rotational/chaotic regimes excluded); no claim of sharpness or of exponential-horizon optimality.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
