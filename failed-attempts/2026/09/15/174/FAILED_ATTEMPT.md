# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Small-cap decoupling for the paraboloid in Q_p^3 in the Guth-Maldague-Oh range and the implied p-adic restriction exponent 10/3
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20424
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Harmonic Analysis
- **Method:** decoupling and p-adic exponential-sum analysis

## Problem

Let K be a non-Archimedean local field of characteristic != 2 with residue characteristic != 2 (in particular K = Q_p, p odd). Let P^2 = {(xi1,xi2,xi1^2+xi2^2) in K^3 : |xii|_K <= 1} and N_{R^{-1}}(P^2) its R^{-1}-neighbourhood. For vec alpha = (alpha1,alpha2) in [1/2,1]^2 with 1 <= |vec alpha| <= 3/2, let Gamma_{vec alpha}(R^{-1}) partition N_{R^{-1}}(P^2) into small caps gamma of size R^{-alpha1} x R^{-alpha2} x R^{-1}. For Schwartz-Bruhat F:K^3 -> C Fourier-supported in N_{R^{-1}}(P^2), does ||F||_{L^p(K^3)} <= C(K,p,eps) R^{|vec alpha|(1/2-1/p)+eps} (sum_gamma ||P_gamma F||_{L^p}^p)^{1/p} hold for 2 <= p <= 2+2/|vec alpha| with C at most polylogarithmic in R and polynomial in residue-field size, and does it imply the extension estimate ||Ef||_{L^p(K^3)} <= C||f||_{L^p(K^2)} for p > 10/3? Decide validity and sharpness over K, including dependence on the quadratic form (elliptic vs hyperbolic/isotropic) and residue characteristic 2.

## Attempted claim

Let K be a non-Archimedean local field of characteristic != 2 with residue characteristic != 2 (in particular K = Q_p, p odd). Let P^2 = {(xi1,xi2,xi1^2+xi2^2) in K^3 : |xii|_K <= 1} and N_{R^{-1}}(P^2) its R^{-1}-neighbourhood. For vec alpha = (alpha1,alpha2) in [1/2,1]^2 with 1 <= |vec alpha| <= 3/2, let Gamma_{vec alpha}(R^{-1}) partition N_{R^{-1}}(P^2) into small caps gamma of size R^{-alpha1} x R^{-alpha2} x R^{-1}. For Schwartz-Bruhat F:K^3 -> C Fourier-supported in N_{R^{-1}}(P^2), does ||F||_{L^p(K^3)} <= C(K,p,eps) R^{|vec alpha|(1/2-1/p)+eps} (sum_gamma ||P_gamma F||_{L^p}^p)^{1/p} hold for 2 <= p <= 2+2/|vec alpha| with C at most polylogarithmic in R and polynomial in residue-field size, and does it imply the extension estimate ||Ef||_{L^p(K^3)} <= C||f||_{L^p(K^2)} for p > 10/3? Decide validity and sharpness over K, including dependence on the quadratic form (elliptic vs hyperbolic/isotropic) and residue characteristic 2.

## Research outcome

Small-cap decoupling in the Guth-Maldague-Oh range holds over Q_p (p odd) with exactly sharp range and endpoint exponent, implying L^p restriction for p>10/3; isotropic forms agree in-range and diverge only above p=4; characteristic 2 exclusion is necessary.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route: headline (A)+(B) sufficiency over K is not proved. Verified by re-running sharp_exponents.py: coherent-endpoint, strip-comparison and fiber-saturation arithmetic all pass, so range necessity/endpoint equality as inequalities are correct. But analytic sufficiency rests on two flagged deep inputs: Step 2 p-adic canonical l^p decoupling for P^2 in K^3 and broad-narrow upgrade to p>10/3. Cited support arXiv:2503.20015 does not contain a P^2 canonical transfer (it treats moment-curve/sparse means and in Sec.4 proves isotropic l^2 decoupling FAILS with Dec>=delta^{-1/2+1/r}), so the Step 2 justification via real Bourgain-Demeter transfer is invalid, especially isotropic. Sec.5 t-shell asymptotics for H are asserted; artifact checks only exponent comparisons assuming them. Hence proof vs computation not separated and essential inferences unverified: FAIL.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: The p-adic canonical l^p decoupling input (Step 2) and the broad-narrow upgrade to p>10/3 are cited as deep inputs rather than proved self-containedly in this pass; the constant's polylog(R)/poly(q) dependence is established for the elementary steps and asserted for the cited input; endpoint p=10/3 carries an R^eps loss so the extension estimate is claimed only for strict p>10/3; sharpness of 10/3 is qualified to L^p-data/small-cap and elliptic Q since isotropic Q has a worse L^2-data threshold.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
