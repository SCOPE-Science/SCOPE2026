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

The proof checks all integer dimensions and vanishing orders under the stated strict contraction hypotheses. The complete singular multiset follows from the injective index shift; the Weyl coefficient follows by multiplicity counting and dominated convergence, not by extrapolating numeric data. The exact-rational checker is `check.py`; it checks both forms of the squared monomial weight and output index distinctness for dimensions 2 through 5, all admissible undamped dimensions, powers 1 through 4, and multi-indices with coordinates 0 through 3. Running it prints `MONOMIAL_COMPANION_EXACT_OK 40065`. Additional finite numerical output compares rescaled counts to the derived limiting series; the convergence can be slow, and no finite cutoff is claimed exhaustive.

The endpoint criterion and logarithmic coefficient follow analytically from the proved infinite counting law. An independent audit or external certification has not been performed.
