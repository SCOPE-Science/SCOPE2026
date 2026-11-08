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

The algebraic Walsh formula is proved in RESULT.md via the generating function of binary Krawtchouk polynomials. `check_capped_even.py` was run from these supplied files using standard Python 3 and ended with `EVEN_CAPPED_HAMMING_WALSH_CHECKS_OK`. It checks dimensions eight through thirteen at cap four and finite examples for even caps two, four, six, and eight. All universal claims depend on the displayed proof, not the finite output.

The critical nonstandard verification is the cubic factorization and quadratic lower bound for cap four: the quadratic has global minimum at least \(c(3m^2-21m+47/4)/24>0\) for \(m\ge7\). The derivative comparison establishes a unique root in \((0,1)\), and the general even-cap result follows from uniform Krawtchouk bounds. Exact numeric threshold values printed by the checker are not independent certificates. Historical originality remains bounded by availability of the original metric-transform sources.
