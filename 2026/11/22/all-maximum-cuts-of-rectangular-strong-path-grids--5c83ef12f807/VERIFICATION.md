---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Verified the unordered labelled-cut convention and edge count. With rows of length L, the increment partitions into L−1 edge-disjoint triangles on (x_i,y_i,y_{i+1}) and leftover edges x_Ly_L and x_{i+1}y_i. At equality the leftover edges are cut: the two constraints from x_L make y_{L−1}=y_L, so the last triangle makes x_{L−1}=x_L, and backward induction forces opposite constant rows. For alternating x the exact increment is L plus the number of interior disagreements and the number of changes in the agreement bits. For L≥3 both costs vanish only for y=x; for L=2 either constant agreement bit works. A monochromatic boundary therefore costs at least r(L−1) on an r×L board with equality exactly in row stripes. On an a×a square the prefix costs at least a(a−2); a final-row increment of a−1 forces a constant boundary and hence row stripes, while any other increment must be exactly a and the prefix must be the unique shorter-side column stripe. Appending a column to a narrower optimal prefix must pay exactly a−1, which propagates the unique column stripe from the square. K4 has three balanced cuts and only one has a monochromatic final column. I also checked the scalar formula directly: in the same induction the square either has constant-boundary lower bound a(a−1), or prefix plus increment at least a(a−2)+a. The rectangular extension and explicit stripes then give (a−1)b uncut edges without an external hypothesis. Inspected verification/check_king_cuts.py and VERIFICATION.md without executing them; the anchored enumeration and integer transfer recurrence are corroboration, not the proof.

## originality

PASS

The scalar optimum and existence of an alternating optimum are established prior results. Pass applies only to the equality-case classification for free rectangles with labelled vertices, modulo side exchange. The verified primary source supplies optimality certificates, not the rigidity analysis; the available evidence does not establish an earlier covering classification.

## value

PASS

A complete ground-state/optimal-partition description identifies when a free boundary selects one stripe orientation and accounts for the exceptional K4. This is a structural result for a natural graph family that beyond the known optimum supplies a useful rigidity and degeneracy criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
