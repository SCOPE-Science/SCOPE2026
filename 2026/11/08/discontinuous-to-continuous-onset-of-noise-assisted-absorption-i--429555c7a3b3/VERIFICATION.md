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

The theorem's proof is algebraic and analytic. Exact-rational computational checks are supplementary.

Reproduce the independent model check with `python verify.py` using Python 3.9+ and no third-party dependencies. It constructs a 9-by-9 generator acting on the three occupations and real and imaginary parts of the three coherences, solves the integrated survival equation by rational Gaussian elimination, and compares the resulting trace with the derived closed formula. It tests 294 parameter triples, including nonzero positive sink rates, both signs of detuning, and zero and positive dephasing, plus rational threshold witnesses. The observed output is: `PASS: 294 exact-rational, nine-variable resolvent comparisons; threshold witnesses pass`.

The global phase diagram is proved by an exact difference quotient, rational minimization on its admissible domain and a sign/convexity argument, not inferred from a finite grid. This checker does not certify completeness of the literature comparison, any enlarged quantum network, the validity of Markovian noise at arbitrarily high rates, or independent peer review.
