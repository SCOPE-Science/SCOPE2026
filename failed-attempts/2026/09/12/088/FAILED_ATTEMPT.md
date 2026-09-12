# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** 3-subharmonic stability of bright soliton on m=3/4 cnoidal background
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1289
- **Disposition:** AUDIT_2_REJECT
- **Domain:** KdV soliton on cnoidal background / linearized spectral stability
- **Method:** squared Baker-Akhiezer Floquet-Hill computation / Darboux dressing

## Problem

Let u_cn be the real KdV cnoidal wave of elliptic modulus m=3/4 reconstructed from the genus-1 Baker-Akhiezer function, and let u_b(x,t) be the even bright one-soliton on this cnoidal background from the Bertola-Jenkins-Tovbis nodal degeneration formula (genus-2 hyperelliptic curve pinched at the midpoint of the finite gap, Kay-Moses determinant with zero phase shift) via Baker-Akhiezer Darboux dressing. For perturbations periodic with 3 times the cnoidal minimal period, decide whether the linearized KdV Floquet-Bloch spectrum about u_b at t=0 is confined to the imaginary axis or contains a certified off-axis unstable eigenvalue at one Floquet exponent. A complete answer is a rigorous squared-Baker-Akhiezer Floquet-Hill computation giving either 3-subharmonic spectral stability or an explicit off-axis eigenvalue with certified enclosure.

## Attempted claim

Let u_cn be the real KdV cnoidal wave of elliptic modulus m=3/4 reconstructed from the genus-1 Baker-Akhiezer function, and let u_b(x,t) be the even bright one-soliton on this cnoidal background from the Bertola-Jenkins-Tovbis nodal degeneration formula (genus-2 hyperelliptic curve pinched at the midpoint of the finite gap, Kay-Moses determinant with zero phase shift) via Baker-Akhiezer Darboux dressing. For perturbations periodic with 3 times the cnoidal minimal period, decide whether the linearized KdV Floquet-Bloch spectrum about u_b at t=0 is confined to the imaginary axis or contains a certified off-axis unstable eigenvalue at one Floquet exponent. A complete answer is a rigorous squared-Baker-Akhiezer Floquet-Hill computation giving either 3-subharmonic spectral stability or an explicit off-axis eigenvalue with certified enclosure.

## Research outcome

3-subharmonic Floquet spectrum about the even bright BJT soliton on the m=3/4 cnoidal background numerically shows a real unstable pair +-0.402037 (empirical spread +-3e-6, non-rigorous), not confined to the imaginary axis.

## Why this attempt failed

Failed axes: correctness, value.

correctness: TARGET required a rigorous squared-Baker-Akhiezer Floquet-Hill computation with certified enclosure (stability or explicit off-axis eigenvalue). The submission explicitly disclaims rigor: +-3e-6 is an empirical Cauchy-ladder heuristic, NOT an interval certificate, with eigenvalue condition number ~3e13 making a posteriori bounds vacuous (O(1) tail bounds). The 3L profile is only C0 with derivative jump ~2 from the BJT background phase shift, so the Hill discretization has only algebraic convergence and the operator itself is an artificial periodization of a non-3L-periodic infinite-line BJT wave. The linearization is a lab-frame t=0 snapshot of a non-stationary moving hump with no established convective-vs-absolute interpretation. Hence the headline 'spectrum NOT confined' is a plausible numerical indication, not a proved spectral fact; the target success criterion is unmet. value: TARGET value depended on a rigorous decision (confinement vs certified off-axis eigenvalue). What is delivered is an explicitly non-rigorous convergence estimate on an artificially periodized C0 ring with O(1) seam kink and without dynamical stability meaning for the moving BJT snapshot. Under STANDARD an unresolved target remains NO_RESULT, and an exact invariant of a natural object is retrievable only when rigorously established, motivated, unknown, and precisely needed; certification strengthens but non-certified heuristics do not create value. With condition ~3e13 the +-3e-6 spread cannot be trusted as a bound, and heavy mollification moves the pair by ~3%. This uncertified indication, however suggestive, is not independently worth finding later as a public record.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: NON-RIGOROUS: +-3e-6 is an empirical Cauchy-ladder spread, NOT an interval certificate; eigenvalue highly non-normal (condition ~3e13) so Bauer-Fike bounds are vacuous. 3L profile value-continuous but only C0 at the seam (derivative jump ~2, algebraic Hill convergence). Lab-frame t=0 snapshot operator: no established convective/absolute dynamical interpretation. Earlier transcription-error no-go found and corrected per WORKLOG.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
