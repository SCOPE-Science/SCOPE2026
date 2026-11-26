---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

I rebuilt all filtration faces using oriented endpoint pairs, rather than the frozen numerical incidence labels, and computed signed boundary ranks exactly over Q: (11,37,30). The 163 augmented faces give reduced homology only in H2, dimension five. Orbit counting on invariant faces gave reduced Lefschetz traces (5,-1,-1,5,-1,-1) on rotations and 1 on every reflection; an invariant simplex with k vertex orbits contributes (-1)^(k-1), also valid for the augmented empty simplex. Both different reflection-chain counts sum to 1. The complex agrees with the pure one at this length (KOW Theorem 8.4). The central involution has trace equal to dimension, so is the identity; the quotient S3 character (5,-1,1) is exactly 1+2 Std, and the rotation image has order three. Replay the independent exact check with python3 -B /workspace/audit_math.py 4. Read the bundled verifier; did not run it.

## originality

FAIL

Resultary 4819a9d67705 (2026-10-11) gives the full virtual dihedral character on the same strong complex before taking the pure restriction. At n=6 the restriction is equality and reduced homology is concentrated in even degree. Its formula therefore specializes to precisely the claimed actual character. The kernel and S3 decomposition are immediate from that character.

## value

FAIL

The action is a natural invariant, but this narrow representation is already recoverable by direct specialization and the standard S3 character table. The frozen work checks the same invariant and makes no distinct integral, equivariant homotopy or broader structural claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
