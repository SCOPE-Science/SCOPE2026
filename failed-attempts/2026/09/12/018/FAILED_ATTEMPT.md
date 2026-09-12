# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Uniform DPD remainder bound for fractional KPZ at sigma 5/2 in C^{1-kappa}
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1087
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Stochastic Analysis
- **Method:** paracontrolled renormalisation with corrected Da Prato-Debussche remainder contraction

## Problem

On the unit torus T^2=R^2/Z^2 consider the fractional KPZ-type equation partial_t h = -(-Delta)^{5/4} h + |grad h|^2 - C_N + xi_N with space-time white noise xi truncated at Fourier modes |k|<=N and Wick constant C_N = E|grad Psi_N|^2 for the linear solution Psi_N in C^{1/4-kappa}. With zero-mean initial data h0 in a fixed ball of C^{eta}, eta>-1/4, write h_N = Psi_N + v_N with Wick square :|grad Psi_N|^2: in C^{-3/2-kappa}. The revised target is kappa in (0,1/4), T*>0, p>=2, and M<infinity all independent of N such that sup_{N>=1} E||v_N||^p_{C([0,T*];C^{1-kappa}(T^2))} <= M via a closed paracontrolled contraction at the attainable Schauder ceiling.

## Attempted claim

For the stated fractional KPZ equation at sigma=5/2 on T^2 with Fourier cutoff N and exact Wick constant C_N, the Da Prato-Debussche remainder satisfies sup_N E||v_N||^p_{C([0,T*];C^{1-kappa})} <= M for some N-independent kappa in (0,1/4), T*, p, M; linear Schauder theory alone places the ceiling at C^{1-kappa}, so the claim tests the nonlinear contraction, and certified blow-up in this space via a resonant diagram falsifies it substantively.

## Research outcome

Proved the uniform-in-cutoff DPD remainder moment bound for fractional KPZ at sigma=5/2 on T^2 in C^{1-kappa}, with VERIFY_OK lattice evidence and a closed paracontrolled contraction.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET headline (2) claims closed first-order paracontrolled contraction in C^{1-kappa} with single Wick constant. Power-counting arithmetic verified by replay (VERIFY_OK, slope 1.527, ceiling 1.0) is correct, but the nonlinear closure is not proved. Draft asserts Q_N o nablaPsi classical with sum 1>0 suffices and that products of remainders are classical in C^{1-kappa}. This is false for the operative terms: nabla v in C^{-kappa} (since v in C^{1-kappa}), so nabla w o nablaPsi has sum -kappa+(-3/4-kappa)<0 and is not Bony-classical; it is a third-chaos stochastic object never constructed in Props 2-4 which list only Q o nablaPsi. Moreover resonant output regularity is min(7/4,-3/4,1)=-3/4, not C^{1-2kappa} as claimed, so v'cdot Pi with v' in C^{3/4-kappa} has sum -2kappa<0, borderline ill-defined. Same gap hits |nabla v|^2 (sum -2kappa<0). The fixed-point estimate ||Phi(v)-Phi(u)||<=C T^theta||v-u|| and N-uniform T*/M via localization plus Gaussian tails are asserted with imported (T1)-(T3) constants, not derived. Script checks only lattice tails and exponent identities, i.e. experimental power-counting evidence, not the contraction or moment propagation. Hence essential inference fails: proof from experimental evidence distinguished, boundary conditions misapplied.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Global-in-time extension, invariant measures, and the kappa-to-0 endpoint are out of scope; T* is small and non-explicit because it depends on imported Schauder and commutator constants (T1-T3) whose proofs are cited from Hairer 2014, GIP 2015, and Chandra-Hairer rather than re-derived; the p=2 moment is stated with extension to fixed p by standard chaos arguments; initial data restricted to a fixed ball in C^eta with eta>-1/4.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
