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

# Verification of the finite-state aspiration theorem

The standalone `verify_aspiration_cycle.py` reconstructs from scratch the four transition matrices in each exact witness using logistic switching and no mutation. It checks the stationary linear system, equal currents around the ring, and clockwise/anticlockwise product ratios. The social-dilemma case uses \(a=2\), \(b=1\), \(B=3/4\), \(\beta=4\log2\) and \(A=0,1/2,1\): the exact currents are \(1/2904\), \(0\), and \(-8/2055\). The other case uses \(a=2\), \(b=1\), \(B=2\), \(\beta=\log2\), \(A=2,3,4\) with currents \(-6/14419\), \(0\), \(24/29255\).

The symbolic checks verify the \(B=2\) polynomial factorization and \(B=1/2\) coefficient cancellation. The finite floating-point sample of 18 parameter tuples is a stress test only, and is **not** used to infer validity over all positive parameters. The full result follows from the proof's elementary integral-average monotonicity, exact cycle criterion and stationary conservation. No probabilistic simulation or external certification is claimed. The code requires Python 3 and SymPy and no external input files. This is a self-review; independent audit remains unperformed.
