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

# Reproducibility and verification

The claim is a completely finite statement about \(2^{18}=262144\) binary configurations once the global sign has been fixed. Its analytic reduction is Fourier orthogonality, and its exhaustive conclusion is established by the two included source files `verify_hex19.cpp` (integer-only C++17 Gray-code enumeration) and `verify_hex19.py` (direct NumPy pair-product enumeration and a complete 48-transformation symmetry test).

Run from the directory containing the included files:

```sh
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_hex19.cpp -o verify_hex19
./verify_hex19
python3 verify_hex19.py
```

The C++ program exits with status zero and reports `INCREMENTAL_EXHAUSTIVE_PASS` only when all expected exact counts match. The Python program independently computes all autocorrelations without using the incremental C++ recurrence, and emits `DIRECT_EXHAUSTIVE_PASS` only when both the finite optimum and the orbit classification agree. The observed outputs are included in `CHECKS.txt`. No sampling, pseudorandomness, approximate optimization or floating-point comparisons are used in the core moment computation. No third-party source or external file is required, other than NumPy for the Python implementation and a C++17 compiler for the C++ implementation.

The exact domain, three representative signings, full search-space coverage, and sharp next-value gap are stated in `RESULT.md`. The verification does not establish the analogous optimization for complex-phase arrays or larger shells, and does not constitute independent mathematical review or historical priority certification.
