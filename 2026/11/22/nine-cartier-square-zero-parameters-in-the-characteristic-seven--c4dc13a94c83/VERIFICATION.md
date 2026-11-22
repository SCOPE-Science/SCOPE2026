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

# Verification and boundaries

For every characteristic-seven parameter \(t\notin\{0,1\}\), symbolic coefficient extraction gives \(A=-5t^4(t+1)\), \(B=5(t+2)(2t+1)\) and \(V=-2(t+1)\). The unique potentially nonzero image under \(\mathcal C^2\) is \((A+B V^7)^{1/49}\omega_2\). The polynomial \(A+B V^7\) has the nine simple roots listed in `RESULT.md`, all in \(\mathbb F_{49}\), by direct factorization in characteristic seven.

The standalone `verify_cartier_char7.py` uses only Python's standard library and independently rebuilds numerator coefficients from powers of \(x(x-1)(x-t)\), then checks Cartier ranks by exact finite-field row reduction. It checks all 47 smooth parameters over \(\mathbb F_{49}\), verifying the nine roots and the two branch-invariant values. The test was executed successfully on the embedded script's exact bytes.

The finite test is not an infinite-field proof. The symbolic Cartier formulas, polynomial identities, root factorization, and valuations supply that proof. A separate mathematical review or historical-priority certification has not been performed.
