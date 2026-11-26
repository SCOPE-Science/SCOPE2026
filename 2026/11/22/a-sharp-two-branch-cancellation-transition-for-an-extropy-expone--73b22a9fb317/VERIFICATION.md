---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Integrating the cubic of the two linear survival pieces and subtracting thrice that integral from the mean gives the stated P_b. The independently checked discriminant factors as 3b^2(b−1)^6 Q(b); the shifted quartic has one positive root counting multiplicities, so the crossing is simple. Both endpoints in p are strictly negative, while a positive leading coefficient forces a third root above 1; the positive exact witness at b=5 and the impossibility of crossing p=0 or 1 prove the interior counts on the open regions. At the threshold two interior roots collide away from the third root. For an exact onset argument factor out that simple analytic third root s(b), writing the remaining monic quadratic as p^2+d(b)p+e(b). The cubic discriminant is a smooth strictly positive factor times d^2−4e near b_*, so the quadratic discriminant has positive first derivative there and its square root gives the stated split with nonzero coefficient. Bounded support precludes exponentiality; equality of an integrated departure does not imply a constant NDSE profile. The bound |Δ(F)−Δ(G)|≤10W_1 together with three stable sign witnesses gives two interior zeros after sufficiently small smooth strictly positive component perturbations. The U-statistic projection uses the conditional expectation of the minimum, namely ∫_0^x S(t)^2 dt. The resulting x−9∫_0^x S(t)^2 dt has positive variance, the U-statistic strong law and CLT apply to the bounded exact mixtures, and Slutsky at a blind weight uses the positive mean. For mean-one exponential the projection differs by a constant from X+(9/2)e^(−2X), with variance 4/5. Independent quadrature and root solving at b=6 reproduced both blind weights, both normalized variances (about 0.601031 and 1.418417), and the limiting rejection probabilities 0.028869 and 0.108361. The supplied verification/check.py was read, not executed; it is advertised for replay with Python, SymPy and mpmath from the frozen directory. The stochastic use is the one-sided fixed Gaussian-null calibration, not a finite-sample or omnibus-power claim.

## originality

PASS

The original NDSE profile, signed departure, U-statistic and null calibration are already known. The distinct result is the complete exact two-uniform zero diagram, its simple fold, robustness of the pair of zeros to smoothing, and differing blind-weight calibrations. The strongest distinct extropy and parametric blind-alternative records address different statistics.

## value

PASS

This gives a complete and robust mechanism for signed cancellation by mixture, with two negative component discrepancies and a positive interior region separated by exact blind weights. It isolates a concrete distinction between characterizing a full profile and testing a single scalar; the two limiting rejection probabilities illustrate that even exact population cancellation need not give equal calibration. It does not challenge performance within the original INDSE alternative.

The dated certificate retains the supplied scientific assessment, sources and limitations.
