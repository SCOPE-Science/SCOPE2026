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

# Reproducibility and scope

Run `python verify.py` with a standard Python 3 interpreter and SymPy installed. The verifier prints one line for every integer \(2\le m\le16\) and a final success message. It checks the exact Chebyshev identity and factorization, squarefreeness, Apéry set by a shortest-path computation, genus and conductor formulas, and Hilbert-function arithmetic. A successful run demonstrates consistency in that finite range, not a proof for every integer. The global proof is the divisor class/Hilbert polynomial argument and the unibranch valuation gap comparison in `RESULT.md`.

No external independent audit or mathematical validation was performed. The reported PASS statuses refer only to the internal same-model analysis.
