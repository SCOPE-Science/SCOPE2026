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

The scalar and Frobenius actions multiply the exponent-19 sum by a nonzero factor and square it, respectively. A normalized space on a scalar orbit is exactly u^(-1)E for nonzero u in E. The frozen certificate checks all 10,795 normalized spaces without omission. In a fresh enumeration using binary reduced row echelon bases rather than normalization (/workspace/audit_replay_3.py), trial division through degree four confirmed the field polynomial, and all 788,035 linear three-spaces gave 1,606 zero spaces, 22 through 1. Direct disjoint scalar images of F_8, E_0, E_0^2, and E_0^4 partitioned the zero set in sizes 73, 511, 511, 511; squaring the last representative returned to the scalar orbit of E_0. Thus both semilinear orbits and the explicit representative are correct. No claim for other degrees or affine spaces was checked.

## originality

FAIL

No explicit matching degree-nine orbit table was found, but the principal classification is a direct orbit-stabilizer and group-order corollary of the published count, not an independent invariant requiring a new census. The displayed coordinate representative was not located in prior sources; it names the single already-forced generic orbit rather than distinguishing any additional classes.

## value

FAIL

The distinction between short and full semilinear orbits is naturally motivated, but the exact split is already forced by the known count and the ambient scalar and Frobenius actions. The independent census is useful corroboration, not a new classification problem being solved. A particular coordinate basis in the forced unique generic orbit is not a separately motivated invariant or distinguished witness here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
