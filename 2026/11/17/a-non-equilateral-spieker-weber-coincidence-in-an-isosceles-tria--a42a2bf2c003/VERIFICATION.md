---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For every 0.7<=h<=0.8, the boundary arclength centroid is S=(0,hs/(2(1+s))) and the continuous perimeter Weber functional is coercive and strictly convex, hence has a unique reflection-invariant minimizer. Differentiating the three edge-integrals at S yields exactly the RESULT.md transcendental G(h). An independently reconstructed SymPy derivative and 100 contiguous mpmath.iv outward interval enclosures gave a conservative strict lower derivative bound 0.09508>0.09; independent 55-digit evaluation gave G(0.7)=-0.0066459334627944..., G(0.8)=+0.0067152187453978... and root h=0.7465542709140345326.... Direct quadrature at h=0.7,0.75,0.8,sqrt(3) agrees to >50 decimal places. This is continuum certification on 100 covering intervals, not 100 point samples. Since the vertical derivative is increasing with site height, its sign reverses the Weber-versus-Spieker order across the unique root. Does not assert global uniqueness among all triangle shapes or outside [0.7,0.8].

## originality

PASS

PASS best-of-knowledge: the exactly isolated non-equilateral equality of the perimeter geometric median and perimeter centroid, plus strict ordering reversal, is distinct from an earlier theorem where the same median equals the AREA centroid at h around 0.109 and at equilateral height. The 2014 general polygon distance-integral method supplies stationarity formulas but does not itself settle the unique transcendental crossing. Only abstract/full-source metadata for the 2014 article was accessible in this execution; direct full-text exclusion is not claimed.

## value

PASS

The Spieker X(10) point is a classical, independently motivated triangle center, and coincidence with a convex boundary 1-median asks whether mean- and median-type centers can agree without full symmetry. The certified exceptional non-equilateral shape and strict order reversal answer a natural geometric question, not an arbitrary sampled parameter or routine rewrite. Local uniqueness is valuable without all-shape classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
