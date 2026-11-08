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

# Verification evidence

The supporting `verify.py` program is self-contained and uses only Python's standard library. It checks the 2048 vertex masks against two independently defined descriptions of the face set. It constructs all 242 nonempty simplices, uses both increasing and decreasing vertex orders for an explicit greedy matching, enumerates all 715 Hasse cover incidences and verifies that every modified orientation is acyclic. Both matchings leave exactly one critical vertex and 21 critical triangles; Forman's theorem then yields the stated integral wedge. Mod-two chain ranks are an independent consistency check, not the integral homotopy proof.

The same program tests that every affine permutation with multiplier in the five quadratic residues preserves all eleven facets. It computes the signed fixed-simplex trace in every dimension for all 55 maps and obtains character values 21, -1 and 1 in the claimed classes. A direct fixed-orbit argument in `RESULT.md` independently explains these values. The recorded output is `verification_output.txt`.

No external independent audit has been performed. No claim is made for other tournaments, an integral equivariant wedge decomposition, or a full integral module classification.
