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

# Verification

Run `python verify.py` with Python 3 and its standard library in the same directory as `RESULT.md`. The checker verifies the rational inclusion–exclusion tie expression against all permutations of edge-clock rankings on eight rectangular matrices, including all 362,880 orderings for the 3-by-3 case. It also independently enumerates three-state two-time edge histories for every rectangle with one to three vertices per side and three pairs of rational survival probabilities. Finally it tests the special closed family identity for two rows.

Observed output ends with `PASS 51 exact finite checks (exhaustive edge orders, two-time edge histories, special formula)`. The general mixed factorial-moment identity, rare-event scaling, dominated-convergence step and conditional gamma limit are mathematical arguments in `RESULT.md`; the finite checker does not constitute an infinite certificate.

The original full text of an older related random bipartite graph study could not be inspected, so historical priority remains qualified. No independent audit or third-party verification was performed.
