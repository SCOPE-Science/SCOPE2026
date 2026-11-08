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

# Verification details

Analytic checks: (i) the Green function satisfies the correct cyclic resolvent recurrence including the source delta; (ii) independent sign-product orthogonality yields the binary quadratic variance; (iii) the discrete Fourier transform of the squared Green sequence has a uniquely smallest Nyquist frequency for even \(n\); (iv) the resulting Rayleigh equality characterizes both minimizing signings; (v) finite geometric sums give the sharp variance, its strict comparison to two independent full probes, and all limits. Each quantified statement is proved in `RESULT.md`.

Computational checks: `python checker.py` with Python standard library `fractions.Fraction` (no external packages) yielded `PASS 33861 exact-rational assertions: n=4,6,8,10,12 and r=1/5,1/2,4/5`. The packaged `checker_output.txt` records this result. These tests check finite cases and do not independently certify the universal theorem.

Unverified extensions: arbitrary weighted or odd cycles, general trace-estimation algorithms, and inexact linear solves. Originality remains a best-knowledge comparison of inspected publications, not an assertion of exhaustive literature coverage. No independent audit was carried out.
