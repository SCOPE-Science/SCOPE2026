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

# Computational and mathematical verification
The proof establishes recurrence and the generating polynomial for every integer \(n\ge2\). Independently, run `python3 verify_book.py` with Python 3 using only the standard library. The replay checks all stable configurations and source vertices for \(1\le n\le9\) (where \(n=1\) is the known triangle boundary), with independent burning and queue stabilization and exact coefficientwise comparisons. The recorded output was `PASS 56453 exact checks`.

The exact formulas in `RESULT.md` are supported by the recurrence criterion, the exhaustive source cases, elementary binomial identities and standard binomial limit laws. Finite checks are corroborative only; no formal or independent certification is claimed. The toppling metric counts individual vertex firings, not absorbed grains or parallel relaxation rounds. The root is fixed at one high-degree spine vertex; changing the root is outside the claim.
