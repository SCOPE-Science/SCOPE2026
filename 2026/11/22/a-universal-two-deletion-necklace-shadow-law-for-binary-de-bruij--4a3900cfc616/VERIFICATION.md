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

# Reproducibility

Compile the accompanying standalone `verify.cpp` with a C++17 compiler using `g++ -O2 -std=c++17 verify.cpp -o verify`, and run `./verify`. The program enumerates successor wiring tables and admits a sequence only if it visits every binary length-\(n\) edge once and returns to its start. For each admitted sequence it tries all unordered pairs of deletion indices, extracts the remaining word, canonically minimizes over its rotations, and partitions by the number of ones removed. The expected result is:

- Order 3: 2 cycles, spectrum `(2,2,2)`.
- Order 4: 16 cycles, spectrum `(8,12,8)`.
- Order 5: 2048 cycles, spectrum `(32,56,32)`.
- Order 6: 29 valid cycles among 2000 deterministic sampled wiring tables, spectrum `(128,240,128)`.

The script outputs `VERIFY_OK` on success. The sample at order six is not exhaustive. Infinite-order correctness depends on the analytic run-choice and untouched-factor arguments in `RESULT.md`, not on extrapolation from the finite census. No independent scientific audit has been conducted.
