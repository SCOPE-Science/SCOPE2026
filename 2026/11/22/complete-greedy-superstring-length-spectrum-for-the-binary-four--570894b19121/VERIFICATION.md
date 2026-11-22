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

The finite-state recurrence is justified in `RESULT.md` and implemented in `spectrum.cpp`. Its recorded complete output is in `spectrum_output.txt`. `witness_generator.cpp` prints a legal 15-merge sequence for every attainable length. The independent `check_witness.py` uses literal intermediate strings, recomputes every current maximum overlap, and checks all 16 original windows at completion; its recorded output is in `witness_check_output.txt`.

Compile with a C++17 compiler using `-O3`; run `spectrum` and `witness_generator` and compare their outputs with the provided text, then run `python3 check_witness.py witnesses.txt`. A finite census proves only the stated fixed-input theorem.
