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

From the directory containing these delivered files, run:

```sh
python3 check.py
```

Observed execution output begins `PASS: 67598 exact structural/order checks` and reports the empirical exact pairing distributions for sample sizes one through six; this was replayed against the current enclosed source. The checker exhaustively enumerates perfect matchings of up to twelve ranked endpoints (all 10,395 matchings at the largest size). It checks equivalence of the graph-theoretic simplicial condition with the endpoint-order condition for each vertex, compares a rational polynomial-integral formula with exact endpoint-order integration in nine cases, and verifies harmonic/adjacent-matching identities in all six sizes.

The checker uses only Python's standard library and does not rely on other datasets or generated intermediate files. Its enumerated finite cases do **not** imply the infinite marked Poisson theorem. The proof of Poisson endpoint convergence, factorial-moment limits and uniform long-mark exclusion is supplied in `RESULT.md`. Source comparisons and remaining access uncertainties are in `REVIEW.md` and `AUDIT.json`.
