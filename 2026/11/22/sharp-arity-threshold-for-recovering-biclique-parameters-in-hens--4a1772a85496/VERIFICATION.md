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

# Reproducible verification
Run `python3 verification/check_henson_threshold.py` in a standard Python 3 environment, with no third-party packages. The checker enumerates all labelled incidence and tuple edge bits and tests every candidate forbidden clique as an actual vertex set. It compares these counts with the theorem's formulas for 92 small instances, then checks distinct reconstruction values for 39600 choices of ambient clique size and positive biclique parameters. The exact recorded output is in `verification/output.txt`.

This is finite diagnostic evidence. The general proof is the clique-size reduction and strict algebraic monotonicity in `RESULT.md`; no inference from a timeout, untested large case, or statistical pattern is used. The literature comparison is provisional and not an independent audit.
