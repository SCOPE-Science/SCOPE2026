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

The complete standalone script `verify.py` uses only Python's standard library and exact `fractions.Fraction` arithmetic. Run with `python3 verify.py`. It computes the stochastic first-effective-event average separately from the theorem's direct majority-indicator expression, enumerates the subsequent forced transition graph, and declares nonconsensus only upon detecting a repeated state. It checks \(18{,}544\) labeled initial states over \(27\) structures and compares fair-Bernoulli exact averages over all profiles against the closed binomial-tail formula for \(46\) structures. The four named small examples are asserted exactly. The program reports `PASS` only if every comparison agrees.

The finite tests do not prove the universal all-size claim. The proof independently establishes the initial-event decomposition, the sharp private-vs-intersection inequalities, the closed alternating communication class, and the fair-initialization averaging identity. No independent external scientific audit has occurred.
