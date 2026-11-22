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

Run `python verify_rank.py` and `python verify_states.py` with Python 3.10 or later. Both scripts use only the Python standard library, reconstruct all adjacency data directly, and do not load outside datasets. The supplied `verification_output.txt` is the actual terminal output of these checks.

The first checker calculates exact matrix ranks and iterate identities over the binary field for every integer graph parameter from 4 through 16. The second checker evolves every binary configuration for the three smallest tested graph orders, independently classifies primitive cycles, first entry times, and individual basin sizes, then verifies all 4,096 states for a four-element characteristic-two field at graph parameter 4. These checks do not establish the theorem for unbounded graph order or all field sizes; those conclusions rely on the algebraic proof in `RESULT.md`.

The graph is specified without external files. Its vertices are the two-subsets of an integer ground set, with adjacency by intersection of size one, except for one added edge connecting two disjoint two-subsets. The field of four elements is represented as two coefficient bits for the polynomial basis of a characteristic-two degree-two extension, and neighbor summation uses coefficientwise XOR. Machine outputs may be regenerated from the complete embedded scripts.

No external or independent audit is claimed.
