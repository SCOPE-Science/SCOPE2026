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

# Verification

From the directory containing `verify.py`, run `python3 verify.py`. The program uses only the Python standard library and checks the sixteen explicit exceptional divisor classes, their integral intersection graph, the forty anticanonical four-cycles, all 1920 binary-affine transformations, all eighteen conjugacy classes and their exact Frobenius signatures through the third extension.

The accompanying `frobenius_spectra.csv` is reproducibly generated and supplies one row for every conjugacy class, including the precise line and square cycle types and the six requested point counts. The execution's success marker is `DEGREE_FOUR_DEL_PEZZO_16_LINES_40_SQUARES_18_CLASSES_SHARP_3_EXTENSIONS_VERIFIED`.

The group enumeration is exhaustive and proves the arithmetic reconstruction because every geometric Frobenius action belongs to this group. The program does not construct finite-field surfaces of all eighteen arithmetic classes, prove field-by-field realization, or independently verify the literature priority claim. Independent mathematical audit has not been performed.
