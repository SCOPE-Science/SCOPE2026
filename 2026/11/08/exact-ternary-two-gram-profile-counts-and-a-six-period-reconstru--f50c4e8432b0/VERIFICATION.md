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

# Verification procedure

Execute `python3 verify.py` with a Python 3 standard-library interpreter. Expected terminal marker: `VERIFY_OK: symbolic identity, rational expansion, 9 exhaustive word/matrix checks`.

The checker reconstructs all rational expressions with its own integer polynomial arithmetic and cross-multiplication, verifies the compact numerator and denominator, and compares twelve exact coefficients. For each transition count \(m=1,\ldots,9\), it enumerates every ternary input word (all \(3^{m+1}\) choices) and every nonnegative nine-component integer vector totaling \(m\), then checks membership equivalence with the directed Euler-trail criterion and the claimed coefficients. The graph check is an independent implementation and does not infer feasibility from the generating function.

The infinite theorem additionally requires the source-to-trail bijection, the complete classification of disconnected balanced and endpoint-imbalanced graphs, and the analysis of rational-function poles. These steps are argued in RESULT.md. The finite checker by itself cannot prove the all-length claim. No independent mathematical audit or external certificate has been obtained.
