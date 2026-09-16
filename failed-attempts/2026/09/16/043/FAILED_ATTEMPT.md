# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Sharp subellipticity beyond the rank-one Levi kernel: two-variable dbar-uncertainty principle for dilation-invariant special domains in C^6
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20487
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Several Complex Variables
- **Method:** Hormander L2 d-bar estimate analysis

## Problem

Let n=5, d>=2, F:C^5->C^5 homogeneous of degree d with isolated zero at 0, phi(z)=|F(z)|^2, H its Levi form, and Omega={(z,z_6) in C^5 x C : Im z_6 > phi(z)}. Assume max_{p != 0} dim ker H(p)=2. Prove s(Omega,0) >= 1/(2 max{d,t(tilde F)}) = 1/sup_p(h_p(phi)+2), hence s(Omega,0)=1/tilde T^1(bOmega,0), by establishing the Hormander-type weighted spectral-gap sufficiency bound for this rank-two class via a two-variable dbar-uncertainty principle.

## Attempted claim

Let n=5, d>=2, F:C^5->C^5 homogeneous of degree d with isolated zero at 0, phi(z)=|F(z)|^2, H its Levi form, and Omega={(z,z_6) in C^5 x C : Im z_6 > phi(z)}. Assume max_{p != 0} dim ker H(p)=2. Prove s(Omega,0) >= 1/(2 max{d,t(tilde F)}) = 1/sup_p(h_p(phi)+2), hence s(Omega,0)=1/tilde T^1(bOmega,0), by establishing the Hormander-type weighted spectral-gap sufficiency bound for this rank-two class via a two-variable dbar-uncertainty principle.

## Research outcome

Proved sharp subelliptic gain 1/(2d) for the rank-two dilation-invariant special domain class in C^6 via a two-variable dbar-uncertainty lemma, dilation reduction, and finite weight patching, with a numeric certificate for the hypothesis class.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route: denominator identity T^1=2d for lines through 0 is elementary, but the hard sufficiency s>=1/(2d) is not proved. Fatal gap at origin: for d>=2, J(0)=0 so ker dim is 5, not <=2, yet the rescaled compact K={|F|<=C} contains 0 and is claimed covered by balls at sphere points p with only a 2-variable lemma. No origin analysis, no Levi-form computation for psi_{p,delta}, no preservation of Hessian lower bound under max-convolution/mollifier, no box-stability covering (the hard part in Catlin-Cho). Lemma statement is vague (datum equals 1, tensor-derivative) and its slicing claim t<=d is shown only for lines through 0, not affine restrictions p+K_p. Uniform sup_p(h_p+2)<=2d is asserted without proof. Example certification is sampling (60000 points + local refinement, reproduced: min|F|~0.18, sigma3~0.036) not a global sphere lower bound, so isolated-zero/rank>=3 for the example and nonvacuity are not rigorously established.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: The proof cites two standard black boxes without re-proving them: Catlin-D'Angelo finite-type necessity (s<=1/T) and the Straube-Catlin Hormander weighted sufficient criterion (bounded psh weights with Hessian gap imply subelliptic gain). The numeric script certifies one d=2 example of the hypothesis class rather than all maps; the general genericity claim rests on the analytic codimension count. The uncertainty lemma constants are uniform by compactness but not made explicit.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
