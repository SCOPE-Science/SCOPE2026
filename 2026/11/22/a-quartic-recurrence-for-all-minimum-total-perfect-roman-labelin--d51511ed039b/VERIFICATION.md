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

Run `python3 verify.py` under Python 3 with the standard library only. It exhausts the 27 local triples, checks all reduced costs, constructs the nine-state critical matrix, checks its characteristic determinant by exact Newton identities, and independently brute-enumerates every ternary cyclic labeling for each cycle length three through twelve. It then checks the recurrence and trace terms through sixty. The expected terminal output is `VERIFY_OK`.

All-order correctness depends on the explicit nonnegative potential and the formal trace–determinant proof in `RESULT.md`, not on finite experiments. No independent audit has been performed.
