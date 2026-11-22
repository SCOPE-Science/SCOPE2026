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
# Reproducibility

Run `python3 check_windmill.py` with Python 3 and the standard library. The script independently constructs finite labelled graphs containing the named friendship parameters, enumerates all possible adjacency assignments to fresh tuples, and rejects any graph with a four-clique. It compares these direct counts to the derived local transfer, then checks weighted independent-set upper bounds and strict extremizers for small arities. Its output is saved in `verification-output.txt`.

Actual successful checks:
- 88 direct finite extension-diagram cases, including all internal tuple graphs in the tested arities and base sizes
- 432 small weighted extremal comparisons
- The exact ordered pair-channel counts for one and two petals

Unverified by computation: universal quantification over tuple arity and number of petals, the classical Kruskal–Katona theorem, asymptotic concentration outside the finite test range, and historical priority. These require the mathematical proof and independent literature assessment.
