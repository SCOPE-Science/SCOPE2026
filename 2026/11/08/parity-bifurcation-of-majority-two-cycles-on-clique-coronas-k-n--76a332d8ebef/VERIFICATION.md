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

Run `python3 verify_exhaustive.py` and `python3 verify_types.py` with Python 3.10 or newer. No third-party Python dependencies or external data files are required. Their expected outputs are `exhaustive_output.txt` and `types_output.txt`, respectively. The first constructs each graph explicitly and iterates a majority update on every initial bit configuration for orders 2–7; the second separately counts all ordered old/next hub-word types through multinomial multiplicities for orders 2–60. Both assert agreement with the claimed even/odd formulas.

The decisive general identities are proved in RESULT.md: the leaf-copy rule, the exact reduction of two-periodicity to old/next hub-word inequalities, the complete even/odd cases, and the symmetric-threshold energy excluding periods above two. Finite checks do not establish the infinite family by themselves. No independent audit has been performed; no stronger verification status is claimed.
