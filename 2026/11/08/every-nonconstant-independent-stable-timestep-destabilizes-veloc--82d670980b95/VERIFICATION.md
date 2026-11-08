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

`verify.py` reconstructs the displayed velocity-Verlet matrices, checks \(\det M(h)=1\), verifies the positive preserved quadratic form for fixed \(h\), checks the complete symbolic commutator trace identity, tests a finite grid of admissible rational timestep pairs, and checks exact stability under deterministic alternation for \(h=1\) and \(h=6/5\). The checked assertion count and outputs are in `verification_output.txt`.

**Reproduction:** Install the requirements in `requirements.txt`, then run `python verify.py` using Python 3. The reference run used SymPy 1.14.0 and passed 861 checks. The finite checks do not imply the almost-sure limit: the proof combines the exact commutator, an analytic projective-orbit argument, Furstenberg's positive-exponent theorem, and the strong law of large numbers. The general random-product theorem is externally established, not computationally or independently re-proved here.
