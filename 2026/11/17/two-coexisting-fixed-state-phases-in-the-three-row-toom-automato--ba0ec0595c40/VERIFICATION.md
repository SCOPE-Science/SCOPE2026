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

Run `python3 verify_structure.py` to reconstruct all 64 possible ordered three-bit column pairs under the original synchronous NEC majority update. The program checks that every allowed transition has exactly the classified form and verifies the exact closed-walk count against the binomial expression for circumferences one through twenty (the scientific theorem covers three and above). Its recorded output is `structure_output.txt`.

Compile `verify_direct.cpp` with `g++ -std=c++17 -O2 -Wall -Wextra verify_direct.cpp -o verify_direct` and run `./verify_direct`. This completely enumerates all binary torus states for each circumference three through seven using the direct local majority rule, classifies the fixed configurations by column type, and checks the exact formula; `direct_output.txt` records the run.

Both programs were run with passing exit codes after creation of the included sources. The universal proof relies on the local transition dichotomy and cyclic-walk count, not on the finite tests. The programs do not test noisy Toom dynamics, arbitrary temporal periods, or previously published results.
