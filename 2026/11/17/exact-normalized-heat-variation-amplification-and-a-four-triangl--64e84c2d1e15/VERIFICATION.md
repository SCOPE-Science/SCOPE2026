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

# Reproduction and boundaries

Run `python3 CHECK.py` from the directory containing this document. The checker uses only Python's standard library and exact `fractions.Fraction` arithmetic. It independently assembles every friendship graph and row-normalized Markov generator, then reconstructs the claimed heat interpolation from eigenspace identities \(Q C=0\), \(Q U=-U/2\), \(Q V=-3V/2\). Rational values of \(q=e^{-t/2}\) permit exact evaluation of the full semigroup polynomial at explicit times.

The recorded execution returned:

```
GENERATOR_POLYNOMIAL_IDENTITIES_PASSED 48
EXHAUSTIVE_BINARY_CUT_INEQUALITIES_PASSED 32724
EXACT_PAIR_WITNESS_ATTAINMENT_PASSED 36
ARBITRARY_SIGNED_INPUT_INEQUALITIES_PASSED 1800
AMPLIFICATION_THRESHOLD_COMPARISONS_PASSED 29
ALL_NORMALIZED_FRIENDSHIP_GRAPH_HEAT_TESTS_PASSED
```

Exhaustive cuts are only within the stated finite graph-size and rational-time tests. These tests do not establish the theorem in all dimensions or continuous times, which instead follows from the analytical linear-system solution, cut reduction, and scalar maximization written in `RESULT.md`. No external or independent proof verification has been performed.
