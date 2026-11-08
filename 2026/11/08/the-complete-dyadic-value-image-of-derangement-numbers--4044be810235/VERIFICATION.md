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

The accompanying standard-library program `verify_derangement_image.py` reconstructs the derangement recurrence modulo all powers of two through \(2^{12}\), checks the complete image against the claimed two residue branches, and verifies local distance laws for 10,144 distinct index pairs modulo \(2^{16}\).

Observed output:

```text
VERIFY_OK levels=12 image_sizes=2,3,5,10,20,40,80,160,320,640,1280,2560 odd_pairs=8128 mod4_pairs=2016
```

The proof does not depend on the finite enumeration: the uniform factorial divisibility of divided differences and the two branchwise valuation identities are infinite statements established in `RESULT.md`. The only historical unresolved issue is the possibility of a broader earlier formulation that implies the image classification.
