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

# Reproduction and limits

Run `python3 check_matrix.py` and `python3 check_orbits.py` with Python 3.9 or later; no third-party modules are required. `check_matrix.out` and `check_orbits.out` are the captured exact output from the included scripts. The first script uses bit-level rank and matrix-power operations over \(\mathbb F_2\) on all connected 2- and 3-dimensional connection sets and deterministically sampled higher-dimensional sets; the second independently constructs neighborhood transitions and enumerates all small configurations for extinction depths and periodic state counts. The scripts also check the folded-cube excluded case.

The computer results cover only finite small examples; the full quantified theorem is established by the algebraic proof in `RESULT.md`. No independent validation is claimed.
