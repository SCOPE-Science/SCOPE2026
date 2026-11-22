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

## Reproduction

Run `python3 CHECK.py` using Python 3 and its standard library. The observed output was:

`CHECK_OK exact_integer_pair_sums=145789 decoder_tests=1660 antipodal_tests=132`

The checker tests exact integer pair-sum uniqueness at finite even orders through \(N=120\); its floating-point reconstruction checks cover \(N=4,6,8,10,12,14,16,18\), including singletons, nonantipodal pairs, antipodal pairs, and complex phases. The script is an accompanying diagnostic, not a substitute for the analytical proof for all even orders.

## Exact checks and limits

The proof does not rely on a numerical tolerance. The key identity is the inverse discrete Fourier transform of each measured squared magnitude, yielding the masked cyclic autocorrelation. Distinct unordered products of positive mask amplitudes identify nonantipodal supports; disjoint squared-amplitude intervals identify antipodal supports; complementary real and imaginary correlation components determine relative complex phase. The one-mask lower bound is exact. There is no claim of uniform reconstruction stability under measurement noise or recovery beyond sparsity two.
