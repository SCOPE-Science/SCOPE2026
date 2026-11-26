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

For the closed solid, on each horizontal half-chord of the projected ball the ray meets material iff c|p|+s sqrt(R²−p²−y²) ≥ sqrt(a²−y²) for |y|<a; for |y|≥a every ray through the ball meets material. The left-hand side is concave in |p| with maximum sqrt(R²−y²)>sqrt(a²−y²). The inner crossing, when present, is p=c sqrt(a²−y²)−sh: the projected point lifts along the ray to the rim x=sqrt(a²−y²), z=h at its positive endpoint. The central gap is the open intersection of two filled ellipses, with boundary entirely in the shadow; any other missing point within the ball's projected disk can reach the unbounded exterior along its horizontal section. At criticality the origin hits the rim, so there is no remaining bounded component. The axial and side-on cases follow directly from the ray test. Integrating the inner width proves the area and strict nesting. The lens factor is the integral of 2 sqrt(1−t²) from τ to 1, giving 4 sqrt(2)/3 times (1−τ)^(3/2) with the stated error. Combining τ'(θc)=R²/(ah) and cos θc=h/R gives the stated angular constant; converting by c−h/R~(a/R)(θc−θ) yields B. Uniform viewing cosine then gives the atom, inverse CDF, 2/3 onset and, with the classical volume, unique recovery. Reconstruct from RESULT.md §§1–4; VERIFICATION.md and verify_napkin.py were inspected, not executed. In the checker the tally counts all sampled rays, though only samples in the proposed hole invoke the occupancy assertion. This does not affect the proof. The critical topology uses the stated closed material, not an arbitrary convention that deletes rim points.

## originality

PASS

The supported distinct result is the exact projected bounded component and the induced area law for the spherical drilled solid. The lens integral, classical volume law, and generic contact exponents are not independently new. No equivalent or applicable stronger exact shadow theorem was found in the inspected sources.

## value

PASS

This is an exact directional topology and area classification for a classical nonconvex solid. A ray obstruction does not in general follow from projected rim outlines alone; the proof makes the bounded/exterior distinction and gives an observable visibility statistic independent of the classical volume datum. The explicit dependence and invertible pair make this more than a generic lens asymptotic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
