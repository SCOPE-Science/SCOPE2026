---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

I independently enumerated all C(12,4)=495 masks; exactly 61 independent quartets. Enumerating every nonempty 12-vertex subset gives 1415 K and 2679 T simplices and the exact f-vectors in RESULT. Rebuilt deterministic row-major vertex-toggle matchings: K 697 pairs, residual critical 1 vertex and 20 5-cells; T 1329 pairs, 1 vertex and 20 4-cells. Independently built entire directed Hasse graphs, respectively 6160 and 13744 cover incidences; topological sorts visited all nodes with no gradient cycles. Forman therefore proves integral wedges, stronger than Betti numbers alone. Signed reduced Lefschetz trace enumeration for 1,R,C,RC yields (20,0,-4,0) on both; the independent 20 square-triples permutation has character (20,0,4,0) and column sign twist gives same rational character. Modules over Q[V4] are determined by characters. Standalone verify_grid_robust.py was inspected and independently reproduced in separate local script; exhaustive finite enumeration is a genuine finite proof here, not sampling or assertion from a log.

## originality

PASS

IMPORTANT direct prior art: Bayer et al arXiv:2209.13503 Table 2 *already states beta_4(T)=20 for G(3,4)*; its Section 5 uses Morse matchings to obtain Betti data and says homotopy wedge shape is suggested, not fully proved in the inspected material. The claimed novelty is therefore only verified integral wedge homotopy for K and T together and Klein-four character (20,0,-4,0), not tabulated rank or definitions. Filakovsky and Chandrakar cover other grid/threshold ranges; prior 4x4 total3 symmetry results do not imply this statement. A hidden prior computational wedge certificate is the material residual risk.

## value

PASS

The rectangular 3x4 grid with robust parameter four is the smallest non-edge-gluing three-row case explicitly outside broad k<=3 grid theorems, so the object/parameter are motivated before any computation. An exact integer wedge decomposition and a nontrivial Klein-four reflection character from a rigorous finite Morse/Lefschetz certificate are mathematical structure not mechanically implied by the ALREADY KNOWN beta_4(T)=20 table. The table rank itself and the Alexander-dual equality are not claimed new. A finite self-contained case can be useful while the arbitrary-grid conjecture remains open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
