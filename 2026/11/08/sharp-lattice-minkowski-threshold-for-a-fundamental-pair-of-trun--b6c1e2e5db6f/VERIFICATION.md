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

# Reproducible exact verification
Run `python3 verify.py` from the directory containing the checker. It uses only the standard Python library, no internet access or third-party dependencies.

The verifier (i) checks the exact width-based inequalities of the six-cell witness for the four-column case, (ii) checks all choices of the small antichain for failure of decomposition, (iii) exhaustively checks \(8008\) six-element supports in the \(4\times4\) poset and \(38760\) in the \(5\times4\) poset for the double-star comparability graph, and (iv) checks preservation of the explicit six-cell witness for several larger widths as a non-essential consistency test.

Expected output:

```
CERTIFICATE_OK
four_by_four_double_stars= 0
five_by_four_double_stars= 1
witness= [(0, 3), (1, 2), (2, 0), (2, 3), (3, 1), (4, 0)]
```

The exhaustive steps are finite assertions and can be independently replicated by a different enumeration. The all-parameter claims depend on the proof in `RESULT.md`, not on the finite parameter checks in the code. No independent mathematical audit has been performed.
