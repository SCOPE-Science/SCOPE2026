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

# Reproduction and scientific limits

Use Python 3 (standard library only) to run `python3 verify_book.py`. The script constructs every nonempty face of the degree-two matching complex of the triangular book independently from graph incidence; it also constructs all faces from the \(J_n*J_n\cup_{K_{n,n}}c*K_{n,n}\) formula. For each \(2\le n\le10\), exact set equality, the augmented face counts, mod-two simplicial boundary ranks and Betti ranks are checked. Compare stdout with `verification_output.txt`.

This computation is a finite check only; the all-parameter theorem depends on the explicit cofiber proof in `RESULT.md`. The abstract statement that every map from a connected graph to a simply connected target is nullhomotopic follows by contracting a spanning tree and checking that images of the remaining generators represent the identity in the fundamental group. The join/smash equivalence and the cofiber-of-a-null-map splitting are standard CW topology. No external homotopy certification or equivariant statement is asserted.
