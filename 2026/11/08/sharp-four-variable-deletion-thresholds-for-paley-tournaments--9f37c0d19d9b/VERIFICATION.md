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

# Verification of sharp deletion thresholds

Run these commands in the directory containing this file and its embedded artifacts:

```sh
python verify_multiplicity.py > reproduced_multiplicity.txt
python verify_affine.py > reproduced_affine.txt
cmp verification_output.txt reproduced_multiplicity.txt
cmp verification_affine_output.txt reproduced_affine.txt
```

Both programs run using the Python standard library. `verify_multiplicity.py` enumerates every unordered triple in each indicated field and all eight sign patterns; for order 27 it computes arithmetic in the explicit irreducible cubic quotient. `verify_affine.py` normalizes anchors to `(0,1,t)` using affine transformations and constructs order-27 arithmetic through a primitive-generator recurrence, independently from the first implementation. The finite checks establish the exact witness minima at ten admissible orders. The general prime-power proof additionally requires the exact character-sum identities and the classical elliptic-curve Hasse bound. Neither finite checker proves the bound for arbitrary larger orders. The mathematical result is self-reviewed; independent audit and validation have not been performed.
