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

On the stated real 2×2 domain, det A = det(sym A) + ((A21−A12)/2)^2 > 0, so the rotation maximizing the Frobenius pairing is the polar factor. Its two distinct entry functions are u/r and v/r with u=tr A, v=A21−A12 and r=hypot(u,v). Unit max-entry perturbations give the entire box (du,dv) ∈ [−2,2]^2, so the two absolute row sums yield exactly 2(u+|v|)max(u,|v|)/r³. The scalar envelope after u≥2μ has derivative sign 1−3t−2t² for 0≤t<1 and −(t−1)(t²+3t+1) for t>1. Substitution gives the stated radical and the unique nonnegative optimizer t*. The signed skew can have either sign. The domain is convex for the global integration step. At μ(I+t*J), the direction I−J realizes the largest derivative and points into the domain, giving an admissible sequence of distinct pairs and the sharp supremum. A separate finite-difference calculation at μ=1 reproduced convergence to approximately 1.1429850281; neither this check nor the frozen numerical script establishes the global claim.

## originality

PASS

The classical planar rotation formula and general polar-factor perturbation theory are background. The compared prior inequalities do not give the sharp maximum-entry modulus on the accretive half-domain; norm conversion loses the joint trace/skew constraints responsible for the optimizer. The accepted distinction is the exact modulus and its feasible sharp geometry, not a new polar decomposition formula. This is a best-of-knowledge comparison, not an assertion of historical priority.

## value

PASS

Entrywise errors in a planar matrix and errors in the extracted rotation entries are naturally measured in the same maximum norm. The exact result decides that 1/μ is insufficient, identifies the anisotropic trace/skew geometry causing the gap, and provides an admissible boundary witness. These are useful worst-case statements not interchangeable with Frobenius or spectral perturbation estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
