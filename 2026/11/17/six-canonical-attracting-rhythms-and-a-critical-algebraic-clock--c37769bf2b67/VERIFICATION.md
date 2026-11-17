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

# Mathematical verification record

The analytic proof establishes the global-in-time statements. The standalone `verify_triad.py` requires Python 3 and SymPy and checks directly:

1. Expressions for three interaction derivatives \(A,B,C\) and both coefficient faces.
2. Exact symbolic characteristic polynomials at synchrony, each splay orientation, and a pacemaker.
3. The nonzero cubic gradient potential at the lower boundary and positive quadratic/quartic terms at the upper boundary.
4. Rational examples \(r=2,s=9/10\), \(r=5/2,s=5/4\) within the open coexistence cone and \(r=2,s=1\) on its algebraic edge.

Observed execution: `VERIFY_OK characteristic_polynomials=3 critical_potential_derivatives=4 strict_examples=2 algebraic_boundary=1`.

Finite symbolic tests do not independently certify the local-potential proof, the entire infinite-time asymptotic, the implicit-function continuation or historical priority. No independent audit has been performed.
