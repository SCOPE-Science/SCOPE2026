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

# Verification notes

The standalone `VERIFY.py` requires only Python 3 standard-library modules. Run it beside the research files with `python3 VERIFY.py`.

It builds every reachable labeled 1-skeleton from two through seven vertices under the exact vertex-or-edge uniform choice rule. For each state it enumerates every possible attachment and checks the expected changes of all degree classes (and the total degree) using `fractions.Fraction`; the cumulative exact transition-term count is **280391**. It also checks the gamma recurrence, normalization, the known edge/mean-degree relation and a 90,000-vertex seeded simulation.

The elementary martingale stability lemma and proof of convergence for infinitely many system sizes are written in `RESULT.md` and do **not** follow from the script's finite enumeration. The script does not certify priority over unknown literature or anything outside the stated graph-degree domain. Independent validation has not been performed.
