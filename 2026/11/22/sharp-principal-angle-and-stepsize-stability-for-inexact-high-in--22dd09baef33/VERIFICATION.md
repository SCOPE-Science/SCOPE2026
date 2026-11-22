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

# Reproducible calculations and proof boundaries

Execute `python verify.py` with the Python standard library (no external dependencies). The script constructs rational orthogonal approximate projector bases, verifies the exact two-reflection symmetric-part identity, and checks nonnegativity of every principal minor of the resulting contraction-gap matrix at three sizes: \(n=2\), \(n=4\), \(n=6\). It verifies the two-dimensional sharp boundary \(\eta_*=14/125\) for \(\cos\vartheta=4/5\), \(\sin\vartheta=3/5\), \(L=5\); the endpoint is an isometry and a slightly larger step expands. The exact \(45^\circ\) test expands for positive step.

Optionally execute `python numerical_stress.py` (requires NumPy; fixed seed 271828). Its deterministic study of 1,000 instances with dimensions 2, 3, 5, 8, 12 and all possible interior indices verified the projector identity and the claimed contraction inequality for random admissible frames. This numeric study is a defect screen only and is not required for reproduction of the exact certificate. No finite experiment establishes universal validity; that follows from the proof's orthogonal-product and energy inequalities.

No nonlinear objective, changing metric, nonorthogonal-frame or unweighted-norm guarantee is verified. The available primary literature supports a best-knowledge historical comparison, but a complete independent priority audit is not represented by these checks.
