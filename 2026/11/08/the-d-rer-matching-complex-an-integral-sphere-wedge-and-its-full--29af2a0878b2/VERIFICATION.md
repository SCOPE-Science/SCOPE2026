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
# Reproducibility and limits

Run `python3 verify.py` with standard Python 3.10 or newer. The exact graph definition is internal to the verifier and repeated in RESULT.md. The verifier independently enumerates all simplices by two distinct recursions; it verifies the 506 greedy Morse pairs and directed-Hasse acyclicity on all 1037 simplices; it performs signed integral unit cancellations to obtain the primitive four-cell boundary. It separately enumerates all 12 graph automorphisms and computes orientation-sensitive Lefschetz traces, including all six reflections. See `verification_output.txt` for the recorded stdout. A separate `rank_independent.py` script performs direct modular sparse boundary elimination, without invoking the Morse-matching implementation; `rank_output.txt` records ranks over primes 2, 3 and 5.

The integer Morse differential certifies the homotopy conclusion in conjunction with the topological argument in RESULT.md; numerical agreement alone would not imply an infinite-family theorem. Rational character data do not determine integral representation lattices or equivariant attaching maps. Independent external review has not been conducted.
