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
# Reproducible checks

In the same directory as `verify.py` and `verify.cpp`, run `python3 verify.py`. The script independently enumerates every unital algebra endomorphism of the four-dimensional characteristic-two algebra with two square-zero generators, over both \(\mathbb F_2\) and \(\mathbb F_4\). It composes generator images, tests idempotency, and counts induced cotangent rank. Its exhaustive histograms are `(1,12,1)` and `(1,80,1)` for ranks zero through two. The Python script also evaluates the closed formula at these parameters and checks the deterministic exponent-window bounds at three larger dimensions.

With `g++` installed, the script additionally builds and runs `verify.cpp` under C++17. That code exhaustively enumerates all generator-image choices with up to three variables over \(\mathbb F_2\), independently testing the polynomial substitutions. Its histograms for one, two and three variables are `(1,1)`, `(1,12,1)`, and `(1,448,3584,1)` in ascending cotangent rank. The successful run ends with `VERIFY_OK`. If a C++ compiler is unavailable, that particular exhaustive three-variable test is skipped and explicitly reported.

These tests do not cover every dimension or finite field and are not an infinite proof. The all-parameter theorem follows from the conjugacy, centralizer and exponent-difference arguments in `RESULT.md`. No independent audit or external certification is claimed.
