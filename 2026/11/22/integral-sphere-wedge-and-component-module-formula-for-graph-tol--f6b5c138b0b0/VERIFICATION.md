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

# Reproduction of checks

Run `python verify.py` in an environment with a recent Python 3 and SymPy installed. The script constructs the top simplices for the exact tolerance definition, directly derives top boundary columns, computes binary ranks by sparse elimination for all 100,416 nontrivial pairs \((G,t)\) on labeled graphs with at most six vertices and \(2\le t\le4\), and compares each predicted rank to the independent component/independent-set formula. Its integral examples compute Smith normal forms of signed top boundary matrices and test that every nonzero invariant factor equals one. The recorded stdout is supplied in `verification_output.txt`.

These are finite computational checks only, not exhaustive evidence for arbitrary graph size. The universal proof relies on the explicit chain identification with exterior powers, the saturated edge-difference lattice, and the standard attaching-map classification for wedges of \(t\)-spheres with \(t\ge2\). The independent audit channel has not been performed.
