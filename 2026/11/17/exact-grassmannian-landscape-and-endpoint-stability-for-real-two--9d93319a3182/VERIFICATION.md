---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-20.md",
      "INDEPENDENT_AUDIT_2026-11-20.json"
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

Read frozen RESULT.md and check.py. For a real-linear complex representation xi↦z xi+w conj(xi), determinant |z|²−|w|², singular values |z|±|w|, and Hilbert–Schmidt metric 2(|z|²+|w|²) are exact. A nonsingular real projective line forces a fixed determinant sign and hence a contraction graph over its positive coordinate plane. The monotone singular-value ratio G attains its supremum at norm L=rho. Tangents of the two principal angles are the singular values of L, giving the stated projector difference. Taylor expansion gives (q−p)/2 rho² for finite q, rho for q=∞. Independent 4-D projection test rho=0.6 gave gap 0.5144957554 and checked several p,q boundaries.

## originality

PASS

Best-of-knowledge originality for complete per-plane objective profile, exact projector-distance identity, and endpoint stability; scalar Gelfand minimum and conformal optimizers already appear in related literature.

## value

PASS

Replaces a previously known single Gelfand number with the entire Grassmannian objective and sharp optimizer stability. The finite-q versus operator-norm linear/quadratic transition is a structurally motivated endpoint phenomenon and useful for nearly extremal matrix subspaces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
