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

# Exact integer verification

Compile `check_spectrum.cpp` using `g++ -std=c++17 -O3 check_spectrum.cpp -o check_spectrum`; run `./check_spectrum`. It enumerates all order-five ASMs exactly via row and column prefix sums, extracts the 200 one-negative masks, performs the full 2^25 integral Walsh transform, tests all signed coefficient histogram levels, and inverse-transforms the nonzero-frequency support to compute the optimal endpoint norm. The observed output starts with `ONE_MINUS_ASM5_WALSH_PASS` and includes `zero_modes=4194816; rank=29359616; negative_modes=14679808; least_nonzero=4; zero_weights_1_2_3=0,12,200` and `range_projection_abs_sum=2222212096; norm=2170129/32768`.

Run `python3 verify_small.py` for a separate row generator and direct signed character sums at degrees 1–3. Observed `INDEPENDENT_LOW_DEGREE_PASS 429 200 [0, 12, 200]`.

All 25-dimensional Fourier modes are evaluated exactly in the C++ run, not sampled. Python does not independently reproduce the complete 25-dimensional transform; it checks the sensitive low-degree layer. The translation-averaging argument in the proof establishes minimality among all projections. Independent external audit has not occurred.
