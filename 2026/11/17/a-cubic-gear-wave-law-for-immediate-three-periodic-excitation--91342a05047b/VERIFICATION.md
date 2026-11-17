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

# Reproduction

Use only the bundled source files. Run `python3 verify_transfer.py` with Python 3 standard library. Compile `verify_direct.cpp` with a C++17 compiler (for example `g++ -O2 -std=c++17 verify_direct.cpp -o verify_direct`) and then run `./verify_direct`. `verification_output.txt` records the successful complete outputs.

The Python code explicitly constructs the two nine-state integer matrices from the local successor rules; uses integer Newton identities, not floating-point characteristic eigenvalues, to reconstruct their characteristic polynomials; and independently compares the recurrence with power traces for all lengths up to 50. The C++ source directly simulates all three-state labelled configurations, independent of matrix or recurrence code, for original rim sizes three through six. Its aggregate of 1,793,340 starting states produces initial primitive-three counts 36, 84, 300 and 954, and in each case the all-zero state is the only fixed state.

The general result is established by the local cycling equivalence and characteristic-polynomial identity in `RESULT.md`; exhaustive finite tests cannot prove unbounded graph sizes. The package excludes a complete attraction-basin census, historical-priority certification and independent mathematical audit.
