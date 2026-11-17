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

The standalone program `check_double_star.py` uses the Python standard library, traverses each induced component rather than assuming the formula, and compares it with the four hub-status conditions. It calculates the complete mod-two homology for all small instances and computes signed Lefschetz numbers of both the hub-fixing and hub-swapping automorphisms, comparing the character to the augmentation exterior-power formula. Run with `python3 check_double_star.py`. The output in `check_output.json` was generated directly by that command.

The exact output reports 54 graph/threshold combinations, 4,174 independently checked faces, 576 leaf-only group/threshold tests and 316 hub-exchange tests. The finite checks do not prove the all-parameter classification. The unbounded proof uses contractible face-cover pieces, their exact join intersection, natural Mayer--Vietoris connecting maps and the augmented simplicial chain complex of a simplex skeleton. No computational extrapolation, integral Smith-normal-form assumption or unsupported equivariant homotopy equivalence is required.

No independent mathematical audit has been performed.
