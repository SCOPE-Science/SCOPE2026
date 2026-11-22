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

- Compile `verify_gl3.cpp` with a standard C++17 compiler. It enumerates all 168 invertible binary rank-three maps and tests every support of sizes one through three: counts 49, 882, 4704, with no mismatches against two-sided vector independence.
- Run `verify_gl3_homology.py` in Python 3. It constructs 49 vertices, 882 edges and 4704 triangles, computes the exact mod-two triangle-boundary rank 834, and obtains first Betti number zero and second Betti number 3870.
- Run `verify_gl2_ternary.py` in Python 3. It enumerates all 48 invertible ternary rank-two maps and all 2016 pairs of 64 possible point-image queries: the full polynomial is \(1+64z+1152z^2\).

These are separate finite checks. The proofs for all \(q\) and \(d\) use the basis-extension principle and the strict union bound. The homology statement is limited to the stated binary dimensions and field coefficients. No independent audit or formal proof-system certification is claimed.
