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

The proof is analytic. The bundled `verify.py` is a self-contained Python standard-library checker of the full \(N^2\)-dimensional (unreduced) Liouvillian and the two time formulas, together with convexity and asymptotic tests. Run `python verify.py`. The delivered source passed 106 assertions. This finite replay does not verify the theorem for infinitely many graph sizes; Sections 1--5 of `RESULT.md` do that.

For positive \(\gamma\), long-time capture probability is proved to be one from a Hilbert--Schmidt monotonicity argument. The interpretation of the boundary \(\gamma=0\) is restricted to a nontrap same-part source when \(m=2\), for which the reachable coherent subspace has no dark state. No assertion about competitive bulk loss or mixing-time cutoff is made.
