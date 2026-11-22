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

# Verification and limits

Run `python3 verify_game.py` to enumerate all binary positions through length 17 and compare their recursive mex values with the proposed complete decomposition; this also confirms that the core of every non-Dyck word is nonempty and has no removable Dyck end.

Run `python3 verify_series.py` for independently implemented mex recursion, integer formal-power-series arithmetic, coefficient comparison at lengths 0 through 14, global sum-to-\(2^n\) tests through length 60, and the exact fixed-nimber residue identities for sixteen values. `verification_output.txt` records the outputs of the replayed programs. Both scripts require only Python 3 standard libraries.

The all-length result relies on the written nonoverlap, game-isomorphism, and generating-function proofs, not on extrapolation from the finite checks. The random limit further relies on classical coefficient transfer for algebraic generating functions. No independent audit has been performed.
