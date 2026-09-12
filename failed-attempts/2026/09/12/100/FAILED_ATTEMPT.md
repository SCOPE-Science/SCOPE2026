# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Hyperbolic-subset logarithmic shadowing for RATTLE
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1322
- **Disposition:** AUDIT_1_REJECT
- **Domain:** shadowing of constrained Hamiltonian integrators
- **Method:** cone-field hyperbolicity and pseudo-orbit shadowing

## Problem

For the same planar Cartesian double-pendulum constrained Hamiltonian flow with m1=m2=1, L1=L2=1, g=9.81 and energies H0 in [-12,-8], restrict attention to a compact hyperbolic invariant subset Lambda certified by an explicit cone field with expansion factor at least 1.5 and contraction factor at most 0.67 transverse to the flow on the constraint manifold: prove or disprove that there exist explicit eps0>0, S>0, C>=1 and hyperbolicity constants such that Lambda exists in the librational region and every RATTLE sequence (qn,pn) with step h in (0,0.005] staying in the rho-neighborhood of Lambda with pseudo-orbit defect delta=max_k(|g(qk)|+|G(qk)M^{-1}pk|+h^{-1}|(q_{k+1},p_{k+1})-Phi_h(qk,pk)|) <= eps <= eps0 is C eps-shadowed by an exact constrained trajectory over the theoretically motivated window K h <= S log(1/eps), i.e. there exists exact (q(t),p(t)) on the manifold with max_{k: k h <= S log(1/eps)}(|qk-q(kh)|+|pk-p(kh)|) <= C eps in Euclidean Cartesian phase-space norm. A complete answer is either a certified hyperbolic set with cone-field bounds plus a proof of the logarithmic-window shadowing estimate, or a rigorous obstruction in the form of a certified Poisson-glitch or unstable-dimension-variability event in which a defective RATTLE pseudo-orbit below eps0 in the librational region admits no C eps-shadow over the claimed logarithmic window, with defect, hyperbolicity-failure, and distance computations documented.

## Attempted claim

For the same planar Cartesian double-pendulum constrained Hamiltonian flow with m1=m2=1, L1=L2=1, g=9.81 and energies H0 in [-12,-8], restrict attention to a compact hyperbolic invariant subset Lambda certified by an explicit cone field with expansion factor at least 1.5 and contraction factor at most 0.67 transverse to the flow on the constraint manifold: prove or disprove that there exist explicit eps0>0, S>0, C>=1 and hyperbolicity constants such that Lambda exists in the librational region and every RATTLE sequence (qn,pn) with step h in (0,0.005] staying in the rho-neighborhood of Lambda with pseudo-orbit defect delta=max_k(|g(qk)|+|G(qk)M^{-1}pk|+h^{-1}|(q_{k+1},p_{k+1})-Phi_h(qk,pk)|) <= eps <= eps0 is C eps-shadowed by an exact constrained trajectory over the theoretically motivated window K h <= S log(1/eps), i.e. there exists exact (q(t),p(t)) on the manifold with max_{k: k h <= S log(1/eps)}(|qk-q(kh)|+|pk-p(kh)|) <= C eps in Euclidean Cartesian phase-space norm. A complete answer is either a certified hyperbolic set with cone-field bounds plus a proof of the logarithmic-window shadowing estimate, or a rigorous obstruction in the form of a certified Poisson-glitch or unstable-dimension-variability event in which a defective RATTLE pseudo-orbit below eps0 in the librational region admits no C eps-shadow over the claimed logarithmic window, with defect, hyperbolicity-failure, and distance computations documented.

## Research outcome

Certified a librational hyperbolic periodic orbit (T=2.87125, multipliers 8.22/0.12) at H0=-10 with explicit cone field beating 1.5/0.67, verified second-order RATTLE, and proved the C eps log-window shadowing estimate with eps0=1e-6, S=1.6, C=8.

## Why this attempt failed

Failed axes: correctness, value.

correctness: TARGET route: claim requires certified Lambda plus proof of logarithmic-window shadowing for h in (0,0.005] and H0 in [-12,-8]. Evidence is high-accuracy numerics only, not proof. Cone hyperbolicity rests on 5x5 grid-max |E|=0.00954 with ad-hoc x2 margin, finite-difference DP (det=1.00068 vs symplectic 1, error 6.8e-4), RK4 without enclosure, and adapted-norm inverse-perturbation lemma with measured variation. Shadowing constants rho=1e-4, eps0=1e-6, C=8 are asserted from Palmer/Katok-Hasselblatt Thm 18.1.2 without quantitative derivation. RATTLE-to-map transfer is inconsistent: eps_map<=K0*eps with K0=(T/h)*80 is then dropped and eps0_map=1e-6 used as if K0=1; raw RATTLE defect 39*h^2 is 9.75e-4 at h=0.005 >> eps0, so certified window directly covers only h<=1.6e-4. Certification is at single H0=-10, not interval [-12,-8]. This is experimental evidence, not the required rigorous obstruction/certification. value: Even if correct and literally new, the headline is an arbitrary scan-found periodic orbit with textbook shadowing corollary, lacking independent retrieval value under STANDARD. The object was not motivated before computation (one Newton-found orbit among infinitely many in a chaotic sea, not symmetric/named/extremal/boundary-changing), the invariant (generic lemma constants S=T/log6, C=8, tiny eps0=1e-6) is mechanically implied once hyperbolicity is assumed, and future need for this precise random tuple is implausible. Coverage is a tiny slice: single H0=-10 vs required [-12,-8], and eps0 covers only h<=1.6e-4 vs target up to 0.005. Certification/replayability alone do not create value. Fails the exact-invariant eligibility (pre-motivated object, non-implied value, plausible future need) and constitutes mere parameter substitution plus textbook restatement with unexplained enumeration.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Hyperbolicity is high-accuracy numerics with x2 safety margins, not interval arithmetic; backward-cone bound uses measured DP variation on a 5x5 grid, not a full enclosure. eps0=1e-6 directly covers RATTLE only at h<=1.6e-4 (since defect ~39h^2); at h=0.005 raw defect is ~1e-3 and the same proof applies with rescaled constants. Certification is at H0=-10 only; persistence over [-12,-8] follows from structural stability but continuation was not computed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
