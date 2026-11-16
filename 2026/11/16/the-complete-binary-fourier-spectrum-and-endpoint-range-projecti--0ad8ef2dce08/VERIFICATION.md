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

# Exact finite verification

The complete standalone artifact is `artifacts/verify.py`, executable with `python3 artifacts/verify.py` and requiring only the Python standard library. The expected success prefix is:

`LATIN3_WALSH_RANGE_PASS latin=12 dimension=8 quotient=256 rank=77594624 zero=56623104 norm=31/4`

The checker enumerates all 216 row-permutation triples and independently produces the same twelve Latin squares using affine arithmetic over three symbols. It constructs the eight-dimensional affine difference span by binary elimination and evaluates all 256 quotient Fourier characters by direct summation, by an independent fast Walsh transform, and by ambient character representatives. It verifies the signed distribution `{-8:2,-4:45,0:108,4:90,8:10,12:1}` and the Parseval identity. It computes the canonical range projector through all 256 kernel values using two independent methods, checks the absolute histogram `{0:12,4:81,8:108,12:54,148:1}`, and checks the second Parseval identity and the exact rational norm `31/4`.

**Mathematical limits.** These finite calculations are exhaustive for the order-three instance but do not prove a theorem about arbitrary larger Latin squares. The unrestricted-projection optimality step follows from translation averaging, proved in RESULT.md and not from enumeration. No external or independent mathematical audit is claimed.
