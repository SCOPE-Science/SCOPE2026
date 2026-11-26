---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In the developed sector let delta be the shorter separation on the angular circle. Its range is [0,alpha], with alpha<pi; the chord in the corresponding wedge stays inside the radial disk. Any path through the apex has length at least r+s; an apex-avoiding path whose lifted angular sweep reaches pi also has length at least r+s, by cutting at its first such angle and using radial distance on the remainder. For smaller lifted separations the planar chord bound and monotonicity in separation give the claimed cosine law. Independent area sampling gives radial moments E[r]=2ell/3, E[r²]=ell²/2, with delta independent and uniform, yielding ell²(1−8 sin(alpha)/(9alpha)). At fixed area the derivative of the normalized function has numerator g=8(2 sin(alpha)−alpha cos(alpha))−9alpha with g''=8alpha cos(alpha); g' rises and then falls with one zero in each half, and g(0)=0, g(pi/2)>0, g(pi)<0 force exactly two interior zeros with the stated signs. The endpoint limits and f(pi/3)<1/pi ensure the smaller zero is the unique global minimizer. Independent numerical bisection agrees with the displayed precision up to last-digit roundoff. Fixed-slant coupling delta=alpha U gives almost sure strict increase for positive radii and U>0. Alpha is half the developed angle, not half the physical apex angle. The supplied simulation was inspected, not executed; it is supplementary, not a proof.

## originality

FAIL

Distinct indexed records materially cover the frozen mathematics. The same-date inverse-ambiguity finding already gives the identical normalized second-moment function for the same geometry and sampling. The same-date tail record explicitly treats the second moment and angle ordering as existing results, without establishing who first obtained them. The Nov. 8 record states the exact sharp inequality, unique minimizing angle and the second stationary point, on a domain including the entire frozen one. Thus exact coverage of the central theorem is demonstrable in the inspected corpus; this is not a finding that the Nov. 8 record preceded the frozen result, nor a determination of within-day or historical priority.

## value

PASS

As a mathematical result, the sharp fixed-area classification answers a natural scale-invariant shape question and distinguishes it from the strict ordering at fixed slant. In particular, classifying the two stationary points and eliminating the near-disk competitor supplies information not given by the cosine law or the moment integral alone. This scientific utility does not restore distinctness in the corpus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
