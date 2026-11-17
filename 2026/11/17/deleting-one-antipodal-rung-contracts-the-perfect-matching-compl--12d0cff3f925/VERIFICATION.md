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

# Reproducibility and limits

Run `python3 verify.py` with Python 3's standard library; the expected output is embedded as `verification_output.txt`. The program constructs the graph and its perfect matchings without referring to the symbolic proof, verifies exact maximal-face overlap, and checks both cone families for even widths \(4,6,8,10,12\). For four widths it performs actual elementary simplicial collapses, verifying at each deletion that a face has exactly one immediate coface and leaves only a zero-cell.

The mathematical proof, rather than the finite program, establishes the theorem for every even width: the seam cut parity precludes exactly one seam, the forced horizontal/seam classes form two cones, their common subcomplex is the odd straight-ladder complex, and the latter is contractible by a two-cone induction. A subcomplex inclusion of finite simplicial complexes is a cofibration, so ordinary CW homotopy-pushout gluing applies. A finite calculation is not an infinite proof. No integral Smith computation or external theorem prover is required for the contractibility claim.

The known intact-ladder wedge-of-two-spheres result is supplied by Agarwal–Basak, arXiv:2608.30601, 2026; the open-ladder contractibility is also independently established in Chandrakar–Singh, arXiv:2407.05809, Theorem 3.3. The latter result is not claimed as new. The result has not been independently audited, and general simplicial collapsibility, odd widths and other edge deletions are outside scope.
