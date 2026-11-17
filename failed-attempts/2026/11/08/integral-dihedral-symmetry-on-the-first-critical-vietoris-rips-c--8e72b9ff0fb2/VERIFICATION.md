---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

For C_{3k}^k, k≥2, the clique dichotomy gives all consecutive-arc simplices plus exactly k exceptional triangles t_j={j,j+k,j+2k}. The arc subcomplex is a good circular-arc nerve ≃S¹; its canonical radial projection has degree 1 on the 3k-cycle. Every exceptional boundary winds once, so integral relative C_2=Z^k maps to H_1(S¹)=Z by summation. Thus H_2=ker(∑), H_1=0, and the usual CW argument gives a wedge of k−1 spheres. Rotation shifts t_j; reflection reverses their orientation and sends j→−j, giving exactly the signed permutation kernel and parity-sensitive traces. The attached enumerator checks k=2..8 as corroboration only.

## originality

FAIL

The earlier 2026-11-01 published finding is for the identical clique complex Cl(C_{3k}^k), all k≥2, and explicitly determines the SAME integral D_{3k} kernel module, r:e_j→e_{j+1}, s:e_j→−e_{−j}, the exact k−1 wedge, all rotation/reflection traces and even an additional gcd-fixed rank. The submitted claim is literally an equivalent formulation, not a new Rips model.

## value

FAIL

The interesting integral equivariant lattice is already determined by an earlier all-k theorem on the same natural object. Repackaging the same signed augmentation kernel and attached-face proof adds no new mathematically needed invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
