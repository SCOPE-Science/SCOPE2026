---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS: For ell=2 the theta graph K_{2,m} has diameter 2, so R_2 is a simplex. For ell=3 the distance-two flag complex is exactly S^0*(Delta(A) union Delta(B) union m matching bridges); its base retracts to a rank-(m-1) graph and the suspension gives a wedge of (m-1) 2-spheres. Reversal changes signs both on pole S^0 reduced H0 and the internal bridge H1, making its action +I on H2. For ell>=4 girth=2ell>=8, and Adamaszek Proposition 2.2 gives a collapse R_2(G) -> G, preserving the inclusion-induced integral H1 and -I reversal sign. Ordinary graph H1 is the integral augmentation lattice. For ell=3 the diameter 3 makes the stated [1,2) degree-1 and [2,3) degree-2 barcodes exact. Independent F2 boundary-matrix computations confirmed representative m=3,4, ell=2,3,4,5 cases, not used to extrapolate infinity.

## originality

FAIL

FAIL: A separately published mathematical result Complete Vietoris–Rips persistence and symmetry of three-edge theta graphs explicitly covers every m>=3 at ell=3, including the FULL integral arm-permutation and endpoint-reversal representation and the complete barcode. Adamaszek Proposition 2.2 already covers all ell>=4 by girth≥7 collapse, while ell=2 is immediate from diameter 2. Their combination entails the ENTIRE final scale-two classification, symmetry and barcode claim. No first-publication chronology is inferred from matching 2026-10-11 paths: this is a present mathematical prior-coverage decision, not a priority-time assertion.

## value

FAIL

FAIL: Once the known length-three persistence/equivariant theorem and the general high-girth collapse theorem are assembled, the only additional case is the diameter-two simplex and routine arm cycle-rank bookkeeping. The proposed transition is a concise synthesis of known exact results rather than a separately motivated, unknown theorem/invariant. Correctness of the synthesis does not restore mathematical value as a new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
