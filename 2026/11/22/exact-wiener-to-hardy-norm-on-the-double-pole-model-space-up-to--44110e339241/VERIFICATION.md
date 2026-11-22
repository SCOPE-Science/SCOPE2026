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

# Exact verification

The proof reduces an infinite Wiener coefficient sum to three absolute linear forms and then computes their Hilbert operator norm by a two-dimensional Gram inverse. Critical inputs: convergence of \(\sum r^k\) and \(\sum kr^k\) for \(r<1\); exact Gram inverse; off-diagonal pairings \(A,-B,C\); the factorization \(BC-A(B+C)=r^3(1+r)^3(1-2r)(1+2r)\); equality of the two coefficient-tail phases at the Riesz extremizer.

Run `python checker.py` in an environment with SymPy installed. The checker reports exact identities and rational-parameter tests, not a numerical search for an infinite optimum. The analytic proof establishes the global maximization for the complete parameter interval. No independent audit has been conducted.
