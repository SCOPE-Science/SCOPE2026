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

The finite checker uses ordinary Python 3 and its standard library. Run `python CHECK.py` in the directory containing this file. The output includes one line per tested finite field and ends with `CHECK_OK fields=11`.

The checker verifies the exact kernel norm and nonzero count in all eleven fields, compares the direct defining character sum to its root-fiber expression (all coefficient locations through field order 13 and fixed randomized samples for larger fields), and independently compares the trace-reduced and full-field three-phase averages. Explicit quadratic-extension arithmetic is used for fields of orders 4, 9, 25, and 49. Floating-point tolerances cover only evaluations of complex roots of unity; the combinatorial root and nonzero counts are integer assertions.

The infinite theorem, the trace-rank dichotomy, and the prime-characteristic asymptotics are proved mathematically in RESULT.md. Finite tests do not certify an infinite family. The normalized Fourier transform and projection are explicitly defined there, avoiding alternative Fourier-normalization conventions.
