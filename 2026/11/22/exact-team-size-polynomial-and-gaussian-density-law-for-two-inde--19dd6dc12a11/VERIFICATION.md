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

Run `python3 VERIFY.py` using the standard library. The checker builds a full cardinality polynomial two independent ways: exact inclusion–exclusion over labelled row patterns, and direct set-union enumeration of every pair of Cartesian rectangles, for \(1\le m,n\le5\). It compares an independent multinomial intersection grouping, and checks symmetry under transposing the matrix. Complete exact factor-encoding enumeration for square orders one through four, and generic representation multiplicities at order four, confirm the claimed mean \(7/16\) and variance \((38N+25)/(256N^2)\).

Successful output begins `VERIFY_OK 25_rectangular_cases` and concludes `GENERIC_FACTOR_UNIQUENESS_OK` after the multinomial and moment tests.

The complete proof is in `RESULT.md`, steps 1–5. In particular finite enumeration is not evidence for the infinite normal limit; that limit uses a proved generic unique-representation reduction and an explicit degenerate-kernel variance bound. Historic priority and any independent mathematical audit are outside these checks.
