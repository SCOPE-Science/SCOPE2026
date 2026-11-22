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

# Reproduction and proof boundary

With `verify_valley.py`, `verify_valley.cpp` and `checks.txt` in the same directory, execute:

```sh
python3 verify_valley.py
c++ -std=c++17 -O2 verify_valley.cpp -o verify_valley_bin
./verify_valley_bin
```

Both implementations enumerate all \(2^{n-1}\) valley permutations and all shattered query supports for \(1\le n\le8\), with the resulting face coefficients displayed in `RESULT.md`. Python also checks its bit representation against direct pattern filtering for \(n\le7\). C++ independently uses iterative insertion to generate the concepts rather than copying the bit generation. The verified trace output is in `checks.txt`, which was captured by executing these programs.

The finite exhaustive check certifies the claimed finite coefficients only; the uniform statements about arbitrary \(n\) rely on the proofs in `RESULT.md`. This is a self-review, not an independent audit.
