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

# Verification record

Run `python3 verify_transport.py` using Python 3 and the standard library; no network or external data are required. The program directly evaluates gas and droplet inverse-survival coordinates, verifies the stationary flux inverse using separate numerical quadrature, reconstructs the source's stationary density from its implicit Lambert relation and checks normalized tail integrals, and tests the exact transport formulas and threshold classification.

The reported run passed **1,070 standalone numerical consistency checks**. It returned the dimensionless crowding transition \(m_*=7.32222706837892\ldots\), and at \(m=8,h=1.5,M=2\), \(W_\infty=0.18467338469300\ldots\) and \(W_1=0.15105285647208\ldots\).

The proof of the all-parameter claim uses the exact stationary flux differential equation, analytic inversion, positivity of an integrand and strict concavity. The numerical program is an independent check of those calculations on finite test cases, not a proof of universal quantifiers. In particular, samples cannot certify the global optimum or rule out untested phases. The result has not undergone independent external audit.
