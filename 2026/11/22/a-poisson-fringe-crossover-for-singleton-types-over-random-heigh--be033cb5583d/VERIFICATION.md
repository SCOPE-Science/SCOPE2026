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

# Verification of the finite identities and asymptotic checks

`verify.py` uses only the Python standard library and runs independently from the proof. It enumerates all balanced finite cross-comparability graphs with shores of sizes one, two, and three, checks exact integer ideal and biclique counts, and compares exact rational averages with the finite binomial identities. Direct ternary new-point comparison enumeration verifies selected induced poset extensions using transitive closure. Additional high-order rational-free floating computations illustrate approach to the mixed-type expectation constant for fixed shifts. The actual successful stdout is preserved in `verification_output.txt` and ends in `VERIFY_OK`.

The proof of the infinite theorem consists of the exact one-point type classification, a Markov ideal bound, shared-row second moments for every fixed fringe size, and a uniform summability estimate dividing large fringes into three small-side regimes and a macroscopic both-side regime. Numerical verification is not substituted for any limiting proof. Independent mathematical audit and historical-priority certification have not been performed.
