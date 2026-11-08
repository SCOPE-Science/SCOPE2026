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

# Reproduction and limits

Run `python3 check.py` using Python 3. The self-contained script performs sparse multivariate polynomial identities using exact fractions, including the derivative quartic, overlap constraint, transition factorization, and endpoint factorization. It also checks rational parameter instances of the reproducing-kernel formula and numerical bisection for the unique root across several parameter regimes. The diagnostics report an assertion count on success.

The proof for every real \(0<q\le1\) and \(0\le\beta<1\) is analytical; finite computations are not exhaustive proofs. Root existence and uniqueness rely on the displayed strict derivative sign and endpoint signs. The sharp damping minimum follows from an envelope differentiation, not grid search. The two endpoint expansions use local rescaled algebraic equations with simple limiting roots. There is no independent mathematical audit or external certification.
