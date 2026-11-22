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

Symbolic verification was performed with the standalone `check.py` in the same package. It checks the pair-product identity, the numerator of the log-curvature, and the two-step derivative-comparison identity with exact SymPy simplification. The program also checks 1,500 parameter settings with 25 independent simplex schedules per setting, verifies the rational four-step example, and numerically computes two transition roots. Its output is included in `verification_output.txt`.

Finite numerical experiments supplement, but cannot establish, the global statement. The global result follows from strict convexity in the pair product, unimodality of \(\log q(t)/t\), and a single-crossing derivative. The phase diagram is proved for every \(a>0\), \(b\geq0\), \(H>0\) and integer \(N\geq2\), including zero-length steps and all tie cases.

No third-party reproducibility review, independent mathematical audit or publication-priority certification has been performed. The result does not claim accuracy optimization or computational speedup.
