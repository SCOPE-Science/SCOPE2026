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

The accompanying `verify.py` is standalone and uses Python standard library only. Run `python3 verify.py`; a successful run ends with `PASS_CUBOCTAHEDRAL_MATCHING_QUOTIENT_H2_Z2_PLUS_Z6_H3_Z_PI1_TRIVIAL`.

It reconstructs the 24 edges of the cuboctahedral graph, all 2648 nonempty matchings, all 48 graph symmetries, 11152 quotient orbit cells, their integral incidence, 5117 elementary collapses and the resulting four-dimensional chain complex. Modular ranks 37,192,229, exact integral unit elimination of the third boundary (227 pivots), and remaining determinantal divisors 2 and 12 give Smith factors 2,6 and a free H3 class. The verifier also eliminates 181 generators in a fundamental-group presentation of the unquotiented complex, and verifies fixed barycenters for a generating set of the symmetry group. The homotopy conclusion uses Armstrong, Hurewicz and Whitehead as described in RESULT.md. No claim of independent audit is made.
