---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The real Hermitian lift of eight intensities at z_j=(1+i)^j has rank 8, exact deleted-ninth-column minor -19660800000, kernel coordinates (256,-150,2,-48,-96,3,3,-9,3), and kernel Hermitian determinant -111540. I independently built the exact SymPy lift and checked rank, minor, kernel and determinant. Any difference of rank-one coefficient Gram matrices has rank <=2 and therefore cannot occupy this rank-three kernel line. For <=7 evaluations, if evaluation vectors span C^3 then the real Hermitian kernel dimension >=2; the odd real determinant on an independent kernel circle vanishes, and a nonzero singular kernel matrix cannot be semidefinite (spanning), yielding a rank-two indefinite counterexample. The analytic determinant witness is nonzero at (0,...,7), so its nonvanishing is open dense in every real parameter cube, giving eight good samples on every subarc. Includes p=0 and lower degrees. No conditioning theorem is claimed.

## originality

PASS

The cardinal-minimal eight-node result is specific to one logarithmic spiral and is not implied by general eight-vector existence, two-circle point designs, parallel-line centroid criteria, or nine-sample Hermitian linear lifting on a contracting spiral. Earlier spiral collision growth pertains to adversarial chosen sites, not fixed designed sites. Best-of-knowledge new constructive geometry with exact Gaussian-integer witness; historical general-design literature may contain an equivalent unnoticed special case.

## value

PASS

Determining minimal phaseless polynomial interpolation on a single accessible analytic sampling trajectory is motivated by phase retrieval with constrained probes. The exact eight-point arithmetic certificate and arbitrary-short-subarc genericity show cardinal-optimal designs on that trajectory rather than merely a renamed general-frame theorem. An exact reusable full-rank obstruction is mathematically substantive, despite no stability guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
