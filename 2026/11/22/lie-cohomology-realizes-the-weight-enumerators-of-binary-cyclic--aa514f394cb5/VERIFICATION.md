---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible checks

Run `python3 verify.py` with Python 3. The script requires only the standard library. It tests the Chevalley–Eilenberg differential matrices independently of the Frobenius-relation-code formula for every irreducible binary polynomial of degrees two to six. It separately enumerates all binary cyclic ideals and full-degree field scalars in those dimensions to verify the converse realizability assertion. It checks \(H^2=0\), both primitive degree-three examples, and the corresponding Hamming enumerators. The test reports 21 irreducible defining polynomials and 11 distinct eligible cyclic codes across the five lengths.

Expected output includes `BINARY_FROBENIUS_CODE_COHOMOLOGY_VERIFIED`. The finite computations do not prove the unrestricted-degree theorem: the proof requires the separable diagonalization, the normal-basis theorem and the annihilator-of-a-divisor argument in RESULT.md.

Publication-priority comparisons were performed against the cited related papers and mathematical records. This review is not independent validation.
