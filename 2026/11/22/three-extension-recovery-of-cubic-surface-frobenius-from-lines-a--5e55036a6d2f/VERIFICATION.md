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

# Verification record

The class enumeration and induced incidence action are reconstructed directly from the divisor-class presentation of a smooth cubic surface. The standalone `verify_e6.py` enumerates all \(51\,840\) group elements, determines \(25\) conjugacy classes by generator conjugation, and reproduces the full table of \(25\) class profiles. The \(45\) tritangent triples are verified both by sum to the anticanonical divisor and by pairwise intersection. All relevant computations use exact integers and finite permutations.

To reproduce from the extracted files in the same directory:

```bash
python3 verify_e6.py e6_profiles.csv
```

The verified output is `E6_27_LINES_45_TRITANGENTS_25_CLASSES_SHARP_THREE_EXTENSIONS_VERIFIED`. The proof of actual large-field sharpness also invokes published equidistribution; the computation alone does not realize individual surfaces. No claim of external or independent audit is made.
