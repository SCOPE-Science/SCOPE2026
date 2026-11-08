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

Run `python verify.py` with SymPy installed. The program reconstructs weighted proximal projections using exact matrix inverses, derives the two-dimensional real state map from the full update, checks the trace, determinant and Jury expressions, and verifies the minimization identity responsible for the ratio boundary. It checks the exact threshold \(q=3+2\sqrt2\), \(\rho^2=1/3\), and an entirely rational divergent witness with \(q=6\), \(\rho=3/5\). It also runs 95 exact rational-grid checks strictly inside the proposed universal stable region.

Expected output:

`VERIFY_OK exact prox reduction, two-period spectrum, sharp threshold, critical endpoint, rational divergence witness, 95 rational-grid cases`

The symbolic computations verify stated algebra, not the absence of prior covering literature. Finite grid tests are not an exhaustive proof of the all-parameter theorem; the analytic derivation in `RESULT.md` establishes the parameter-complete claim. No independent audit is represented.
