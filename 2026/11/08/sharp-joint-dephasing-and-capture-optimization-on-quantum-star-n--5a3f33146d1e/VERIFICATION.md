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
Run `python verify.py` from this package directory with `numpy` and `sympy` installed (see `requirements.txt`). The code is a standalone checker that constructs the full one-excitation complex Lindbladian independently of the reduced proof equations. It ran to completion with `PASS: 103 symbolic and independently evaluated Liouvillian/optimization assertions`.

Exact symbolic checks cover the seven integrated identities, formula, derivatives, convex-limit identities, and the large-size algebraic stationary constant. Independent full-matrix checks compare 20 cases across five star sizes and four physical parameter triples; nested bisection validates joint optimum equations through \(N=10000\). The tests are finite and do not prove the all-size theorem: the matrix stability, exact integrated equations, strict convexity, and asymptotic compactness/selection are established in `RESULT.md`. Neither experimental confirmation nor independent expert audit is asserted.
