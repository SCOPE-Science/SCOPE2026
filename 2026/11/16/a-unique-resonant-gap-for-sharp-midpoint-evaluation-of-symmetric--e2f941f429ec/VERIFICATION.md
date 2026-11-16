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

Use `python3 CHECK.py` with the Python standard library. The checker evaluates analytic and independently integrated energy expressions on deterministic random complex coefficient triples, confirms the exact midpoint reproducing-kernel identities, compares the derived derivative with numerical differences, and brackets the unique root. Its observed result is 1,000 passed finite assertions, with optimal gap near \(4.904924457138071\) and squared constant near \(4.267303561395562\).

The theorem for all positive gaps follows instead from the explicitly stated sign inequalities for \(N(w)\), proved analytically in `RESULT.md`; numerical tests do not establish existence, uniqueness, or publication priority. Only the symmetric three-frequency setting is claimed. No independent mathematical audit has been performed.
