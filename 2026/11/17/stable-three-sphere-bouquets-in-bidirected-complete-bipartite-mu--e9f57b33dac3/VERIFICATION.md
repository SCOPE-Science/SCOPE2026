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

# Reproducibility and verification limits

Run `python3 verify_k2n.py` in the same folder as this document. The program uses only Python 3 standard-library modules and enumerates all four-slot tuples with labels up to each specified finite width. It evaluates the five explicit forbidden conditions, checks the complete face vector, and performs each prescribed lexicographic matching operation. For every width from six through nineteen it asserts exactly the quartic number of critical three-faces and no other critical faces, with the empty face included during matching.

For widths six and seven, it separately evaluates **every** tuple using actual directed edges, degree restrictions and cycle detection (not the five-case predicate), then constructs the complete directed Hasse graph with matching edges reversed and checks acyclicity by topological sorting. The recorded output in `verification_output.txt` reports all checks and terminal success marker `K2N_MULTIPATH_STABLE_MORSE_EXACT_PASS`.

The family statement above width nineteen is not verified by extrapolation; it follows from the proved fresh-tail induction and the universal acyclicity argument in `RESULT.md`. The package does not implement a proof assistant or independent mathematical validation. Future independent examination of the fresh-tail lemma and the novelty comparison remains appropriate.
