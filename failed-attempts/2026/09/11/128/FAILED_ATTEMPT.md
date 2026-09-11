# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Single-mode twisted dissipation ledger at unit wavevector
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1018
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Kinetic Theory
- **Method:** Fourier mode-by-mode DMS twisted energy with macroscopic Poincare matrix

## Problem

Decide whether the Dolbeault-Mouhot-Schmeiser twisted energy at the lowest torus Fourier mode satisfies an explicit dissipation inequality with logged twisting and rate constants for cutoff hard spheres, or certify a violating macroscopic direction.

## Attempted claim

For cutoff hard spheres on T^3=(R/2piZ)^3 at Fourier mode k=e1 with |k|=1, the DMS twisted functional H_k[h]=||h||^2+(1/8)Re<A_k h,h> satisfies 0.9||h||^2<=H_k[h]<=1.1||h||^2 and (d/dt)H_k[S_k(t)h]<=-(1/120)H_k[(I-Pi_k)h] for all fiber data, where S_k is the fiber semigroup of L-i k.v and Pi_k the hydrodynamic projection.

## Research outcome

Closed the (epsilon=1/8,kappa=1/120) DMS single-mode ledger at k=e1 for the BGK fiber with certified 28x28 LMI margin 0.00779; hard-sphere target blocked by explicit gap shortfall.

## Why this attempt failed

Failed axes: correctness, value.

correctness: FAIL: the shipped proof chain does not close as a rigorous proof. Verified exactly and independently: F/S matrices from Gaussian moments, P=S-F^2 spectrum {0,1,1,4/3,5/3}, ||A||<=1/2 by AM-GM giving equivalence [0.9375,1.0625], joint Gram J (found rank-8 singular since u_1==w_0 micro, so the stated J^{-1} constraint as written is ill-posed and only the regularized superset argument saves sufficiency), and float PSD of G_28 (min eig 0.007787, residuals ~1e-15). But (i) both shipped verify scripts begin exec(open('scratch/lmi15.py')...) and that file is absent from inputs/artifacts, so the documented reproduction cannot run and the F/S/B/J reconstruction plus K-block derivation (complex skew terms) cannot be checked from the package; (ii) the LMI 'certificate' is plain floating-point eigendecomposition with no interval/rational enclosure, i.e. experimental evidence, while DRAFT Step 3 overstates it as certifying lambda_min>=0.007787. Independent exact-restriction Galerkin checks (degrees<=6, Qmax=-0.02236) support truth but do not repair the shipped proof gap. value: FAIL: new but not independently worth retrieving; judged with no preset-value presumption as required for EMERGENT_FINDING. The conceptual content -- DMS twisted-L2 hypocoercivity of the linearized BGK relaxation operator -- is textbook (it is the headline illustration of DMS 2009, arXiv:0810.3493), and the submission only fills the hard-sphere target's leftover numbers (eps=1/8, kappa=1/120) into that known framework at one mode. The concluded bound dH/dt<=-(1/120)||micro||^2 is micro-only (no macroscopic coercivity, implies no decay by itself) and 120x lossy against the unit BGK micro gap, with constants arbitrary from any BGK perspective. No benchmark, classification boundary, sharpness, or downstream BGK use is demonstrated; the claimed bottleneck-direction and LMI-template significance points to future hard-sphere work, i.e. a new research direction, which cannot carry an emergent finding's value. This is a textbook restatement plus arbitrary parameter fact, explicitly rejected by the shared standard even when correct and new.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: The certificate proves the BGK (relaxation-operator) ledger, not the admitted cutoff hard-sphere target: it does not supply the hard-sphere microscopic gap beyond the Baranger-Mouhot 0.0281 lower bound nor the weighted collision-frequency auxiliary-operator bounds the hard-sphere closure needs. The LMI certificate is a floating-point orthogonality-residual enclosure (margin 0.00779, errors ~1e-15) rather than exact rational arithmetic, and it covers only the single fiber k=e1, not global torus…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
