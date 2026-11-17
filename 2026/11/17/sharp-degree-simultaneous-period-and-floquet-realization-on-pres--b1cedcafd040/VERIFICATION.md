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

Run `python3 verify.py` with NumPy, SciPy and SymPy. In the supplied execution, the checker reports exact symbolic radial/angular identities and total-degree calculations; independent numerical quadrature and ODE integrations of ten prescribed circles in four configurations, including two same-sign nonunit multipliers, passed. The degree lower bound is a mathematical divisibility argument given in `RESULT.md`; a finite experiment cannot establish it for all integers and all real parameters. The checker does not certify the absence of other cycles (none is claimed), global completeness, or independent historical priority. The independent audit has not been performed.
