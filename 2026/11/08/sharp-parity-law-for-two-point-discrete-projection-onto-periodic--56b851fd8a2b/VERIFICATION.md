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

# Verification and reproducibility

The proof uses an explicit second-order cyclic Green kernel. Its recurrence is checked directly at the origin and away from the origin, then periodized for every integer \(N\ge3\); this is the all-parameter argument. The absolute coefficient sum is a finite geometric series. Opposing adjacent-row signs establish strict knot localization. Exact hyperbolic differentiation proves monotonicity for odd \(N\), and a rank argument handles the coincident-midpoint boundary.

Run `python3 checker.py` in the extracted directory. The checker requires only the Python standard library and performs exact rational Gaussian elimination rather than floating-point approximation. The executed diagnostics yielded:

```text
EXACT_RATIONAL_GRAM_AND_LEBESGUE_N_3_TO_13_OK 33 CASES
ODD_MIDPOINT_LIMIT_AND_ATTAINMENT_OK
KNOT_SAMPLING_LIMIT_OK
ALL_DISCRETE_SPLINE_CHECKS_PASSED
```

The checker exercises only the explicitly indicated finite test cases. It does not establish the universal statement by enumeration. The Gauss-node specialization is obtained analytically from \(1-2t=1/\sqrt3\), not numerical approximation. The result applies to the precise sampling measure and spline space defined in `RESULT.md`; ordinary continuous-measure \(L^2\) projection is distinct. Independent audit has not been performed.
