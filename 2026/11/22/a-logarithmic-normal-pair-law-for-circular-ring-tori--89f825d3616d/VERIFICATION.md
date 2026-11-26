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

The area factor is r(R+r cos u). At each interior z=sin u the two cosines have opposite signs and the same absolute Jacobian; adding their weights cancels the aspect ratio and leaves the arcsine density, independent of uniform azimuth. Conditioning on the two heights gives the positive integral. It has a continuous interior representative: on a compact range of t away from +/-1, choose small enough polar caps that the two normals cannot both be in those caps with scalar product t. Split the spherical density into its integrable polar part and a smooth remainder. The polar-polar term vanishes, and the mixed term is continuous by integrating the smooth factor on a latitude circle, using symmetry of the two factors. The addition theorem kills all nonzonal modes, and great-circle averaging gives the one-point Legendre moment P_l(0)^2, hence the pair moment P_l(0)^4. The l=2 moment 1/16 gives variance 3/8. The density series is locally uniformly and globally L^1 convergent by the standard Legendre bound; orthogonality and compact moment uniqueness identify the law. Stirling gives coefficient 2/(pi^2 k)+O(k^-2) at degree 2k. At t=cos(theta), frequencies k<=1/theta contribute the harmonic sum with bounded error (the derivative bound gives O(k^2 theta^2)); the high frequencies contribute O(1) by the same Legendre estimate. Thus the leading coefficient in log(1/theta) is 2/pi^2, or 1/pi^2 in log(1/(1-t)), and evenness gives the opposite endpoint. Integrating over length 1-cos(epsilon)~epsilon^2/2 yields the claimed angle-tail coefficient.

## originality

PASS

Horn already determines the one-normal distribution, including aspect-ratio invariance, and the abstract harmonic coefficients follow from the classical Funk multiplier after identifying the torus pushforward with two right-angle steps. The additional evaluated result is the torus normal-pair law and its sharp pointwise endpoint and angular-tail asymptotics. No matching prior asymptotic was located in the material examined; novelty is not assigned to the known one-point law or the multiplier.

## value

PASS

Independent normal-pair angles are a natural surface descriptor, not an arbitrary polynomial statistic. The result evaluates a complete benchmark law for a canonical surface family and, beyond the known pushforward and inherited moments, quantifies the enhanced frequency of almost parallel and antiparallel observations by a sharp integrable logarithm. This is useful when interpreting normal-angle histograms or calibrating rare-angle thresholds; a marginal invariance statement by itself does not provide those probabilities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
