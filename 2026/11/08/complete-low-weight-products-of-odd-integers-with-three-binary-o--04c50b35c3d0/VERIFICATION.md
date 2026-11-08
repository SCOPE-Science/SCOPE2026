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

# Exact checks and limits

The source paper's two product bounds are verified against the primary arXiv manuscript: Kaneko and Stoll, arXiv:2112.03077v1, Theorems 2.1 and 2.2. With equal factor weights \(3\), products of weight \(2\) have size strictly below \(2^{14}\); products of weight \(3\) have size strictly below \(2^{23}\).

`verify.py` generates all \(231\) odd three-bit factors with two higher exponents from \(1\) through \(22\), and checks all \(3672\) unordered pairs with product below \(2^{23}\). Its observed weight-two and weight-three classes match the claimed seven exact products. It prints `VERIFY_OK` and its output agrees with `verify_output.txt`.

`independent_check.py` generates all \(13\) two-bit odd candidate products below \(2^{14}\), and \(231\) three-bit odd candidate products below \(2^{23}\). It tests every odd weight-three potential divisor from \(7\) through the integer square root of the candidate, then tests the complementary factor. It performs exactly \(5523\) integer trial divisions and prints `INDEPENDENT_CHECK_OK`; the output agrees with `independent_output.txt`.

These are exhaustive finite checks under published bounds. They do **not** independently prove the general carry-propagation bounds, nor do they establish anything for weights greater than \(3\). All code uses built-in arbitrary-precision integers and standard Python 3 only. No external verification or independent audit has been performed.
