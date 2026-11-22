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

# Reproducibility of finite sign certificates

Execute `python checker.py` using Python 3 standard library only. The script checks both the beta-log identity and the collapsed formula for 199 integer values, tests the visible finite monotonic regions, and uses exact rational `Fraction` intervals for four signs. Numerical simulation of normalized independent exponentials is an independent finite corroboration, not an argument for arbitrary sample size.

Certified sign intervals (the computations actually reproduce narrower rational enclosures):

- \(F_{20}\in(-0.006391,-0.006390)\), negative;
- \(F_{21}\in(0.009871,0.009872)\), positive;
- \(G_{54}\in(0.005599,0.005601)\), positive;
- \(G_{55}\in(-0.000463,-0.000460)\), negative.

Actual replay output: `PASSED 899 assertions`. The analytical strict monotonicity and convergence proofs in `RESULT.md` apply to the entire infinite integer range. The finite enumerations are not treated as exhaustive. The standalone code uses a powers-of-two argument reduction and the explicit rational tail bound on the atanh series; the printed floating-point interval endpoints are displays of exact-rationally-certified bounds. No independent mathematical audit has been performed.
