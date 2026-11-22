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

# Verification and reproducibility

The theorem concerns every real side triple \(0<a<b<c\), not just a finite grid. Its proof is the exact sphere-to-plane two-sheet Jacobian, an explicit sign inequality, feasible six-vertex spherical-great-circle enumeration, and Gauss–Bonnet area. The accompanying `checker.py` is a separate numerical diagnostic and cannot certify the infinite quantifier.

Run `python -m pip install -r requirements.txt` and then `python checker.py`. It reconstructs all feasible vertices from the six defining halfspaces, computes the hexagon area by spherical-triangle decomposition independently of the inverse-sine expression, and checks the two algebraic lifts. Six distinct boxes are checked. For each box, \(2^{17}\) deterministic low-discrepancy spherical samples test the exact ambiguity probability within absolute tolerance \(0.0025\), totaling 786,432 sampled views. Its largest observed discrepancy is substantially below that tolerance.

The constant in the joint-density boundary singularity is established by a local sheet calculation, not by the sampling test. The range infimum and supremum are geometric limits and are not attained by pairwise-distinct edge triples.

The paper-based comparisons used arXiv:1110.0671 and arXiv:1203.2464 with actual PDF sections inspected, and the available abstracts of arXiv:2608.03305 and arXiv:2609.26202. The last broad source was not inspected in full, which leaves a genuine priority limitation. No independent audit is claimed.
