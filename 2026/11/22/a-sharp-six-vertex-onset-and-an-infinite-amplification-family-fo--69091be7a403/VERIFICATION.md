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
# Verification scope

Analytic proof: exact edge balance and optional stopping on finite connected trees; explicit rational double-star weights; a strict one-root sign analysis on the six-vertex example; monotonicity on at-most-five-vertex trees by bidegreed classification plus a complete four-vertex-orbit sign certificate for the five-vertex fork; symbolic family derivatives and limits.

Reproducible finite checks: install Python 3 and SymPy, place `verify.py` alongside this document and execute `python verify.py`. This independently constructs finite-state copying probabilities from degrees, tests weighted martingale drift for every nonabsorbing mutant configuration on the stated four small double stars at four mixing parameters, checks rational and sign identities, and validates exact family limits. Output: `PASS 1514 exact one-step identities and symbolic checks`.

The checker does not prove every finite order or every real parameter by enumeration; the written algebraic proof supplies those universal steps. The theorem has not received independent validation. No external independent-audit evidence is asserted.
