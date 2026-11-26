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

Independently enumerated normalized five-coordinate points with both sums zero (85 and 199), and all rational dual forms modulo constants and scalars (400 and 1464). The exact sizes and multiplicities agree at every bin, and the two point/pair incidence moments agree. Enumerating every two-dimensional subspace by unique reduced echelon bases and testing all four binary cubic coefficients gave 15 and 27 rational lines. Section line profiles (none, one, three nonconcurrent, three concurrent) are (310,75,5,10) and (1230,189,35,10); no two-line case. The geometric residual-line argument also uses smoothness: if a plane restriction had a repeated line, on that line the gradient of the surface would be controlled by a single quadratic (the normal derivative), which vanishes somewhere on the geometric line. The ten maximizing equations are exactly X_i+X_j=0; on each, the other coordinates A+B+C=0 have cubic sum 3ABC, yielding three concurrent lines and 3q+1 points. Triangles give 3q. The same census independently recovered all 43 frozen S5 orbit rows (13+30). A nonzero form never vanishes on the whole surface point set, so the four-coordinate evaluation is injective. Each projective dual row contributes q-1 different words of weight N_q-z, giving the full stated weight enumerator and distances 63 and 165. Replay: python3 /workspace/audit-replay/5.py; output /workspace/audit-replay/5.txt. Exhaustion is for the specified model and fields only.

## originality

PASS

Best-of-knowledge pass on the complete section-size distributions and their orbit and line profiles for this fixed Clebsch model. Classical geometry, point–line incidence, and maximal-section or minimum-distance results are credited, not claimed as new. Full code weights are an equivalent presentation of the census, not a second independent novelty claim.

## value

PASS

These fields are singled out by the known empty line complement for the model, not by an arbitrary sample. The complete distribution gives the frequency of each rational section size rather than just the maximum, distinguishes concurrency and triangle contributions to large cuts, and supplies the ordinary weight distribution of the corresponding natural evaluation codes. Exact multiplicities are useful finite invariants even without a general-q theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
