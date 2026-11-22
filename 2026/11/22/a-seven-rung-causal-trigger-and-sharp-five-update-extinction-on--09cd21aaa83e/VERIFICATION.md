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

The proof reduces the universal five-update claim to a complete seven-rung radius-three truth table and a six-case incompatibility argument. `verify_all.cpp` checks every labelled initial state and time-three site on open ladders of lengths one through eight; seven rungs are the complete dependency window for a time-three excitation away from the boundary. `verify_transfer.py` separately constructs and evaluates the forbidden-word automaton and checks pairwise trigger conflicts.

Compile and run `verify_all.cpp` using a C++17 compiler, and run `verify_transfer.py` using Python 3. Compare their output against `verification_output.txt`. The complete finite enumeration, rather than an unverified sampling log, supplies the radius-three lemma. Computational and theoretical scope is exactly as in `RESULT.md`; external mathematical validation remains unperformed.
