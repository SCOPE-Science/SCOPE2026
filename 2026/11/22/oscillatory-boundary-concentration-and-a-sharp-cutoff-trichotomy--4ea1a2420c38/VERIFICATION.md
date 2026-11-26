---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Radial orthogonality gives the beta quotient; the substitution t/(1-t) gives the Tricomi integral, taking its Abel limit after the ordinary oscillatory integral is justified. With v=1/(1-t) the tail tends to zero by integration by parts exactly when beta=lambda−gamma>−2; for beta≤−2 the integrals over [R,R+pi] have magnitude asymptotic to 2R^(−beta−2), violating Cauchy convergence. Independently checked the saddle: on the small radius r connector the angular integral of the damping is O(r), giving O(r^(beta+2)); the outer connector and real remainder at m^(−1/3) are O(poly(m) exp(−c m^(2/3))). On u=w x/sqrt(m), w=exp(−i pi/4), the leading exponent is −sqrt(m) w(x+1/x); the correction i x²/2 is imaginary and the remaining real correction is uniformly bounded up to the contour cutoff. Localization at x=1 gives the complex Gaussian sqrt(pi/w), the stated power and the exp(i/2) factor. The counting constant follows by squeezing around k=(log(1/s))²/2 using log(1/|mu_k|)~sqrt(2k); an arbitrary relative o(1) does not alone imply monotonicity, but monotonicity is unnecessary and also follows from I_(m+1)(beta)=I_m(beta)−I_m(beta+1) and I_m(beta+1)/I_m(beta)~w/sqrt(m), with the beta-normalizer ratio only 1+O(1/m). For the tail use one integration by parts: before dividing by B(m,lambda+1) it is O(eps^(beta+2)) when m eps≤1 and O(m^(−beta−2)) when m eps≥1, using exponential bounds on (1−u)^(m−1). This proves the uniform upper rate for gamma≤1. At m eps→lambda+1, a second integration by parts after scaling u=eps x makes the remainder O(eps^(beta+3)), giving the stated positive lower constant. Diagonal convergence on the dense finite-mode space plus uniform bounds proves strong convergence at gamma=1; the diverging norms preclude strong convergence above it. Compactness and all Schatten inclusions follow from spectral decay and harmonic dimensions.

## originality

PASS

Pass for the sharp comparison of canonical truncations with the compact diagonal extension across the entire ordinary-moment range, in particular the matching lower endpoint bound and the distinction between strong-only and divergence with modewise convergence. Do not credit the complex saddle coefficient, all-Schatten cancellation, or the underlying logarithmic count as independent novelty: they have both exact special-function implication and substantial named prior overlap. The existing sufficient average criteria yield part of the cutoff result, but not the matching lower bound or the supercritical divergence while a compact mode-extension persists.

## value

PASS

The lower estimate detects modes whose degree moves out to boundary scale as the cutoff is removed, and separates existence of a compact extension from existence of a bounded strong approximation. This is a useful concrete boundary for interpreting unbounded oscillatory symbols, beyond recovering a standard special-function decay law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
