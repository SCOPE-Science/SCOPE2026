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

Run `python3 verify.py` under Python 3.9 or later with no third-party packages, and compare standard output with `expected.txt`. The program independently reconstructs the graph distances and checks all triples, constructs the complex predicted by the decomposition, performs exact mod-two boundary reductions over all faces, and checks the signed reduced Lefschetz number of selected automorphisms against the predicted degree-one and top integral representation characters.

Ten parameter vectors were tested, with up to four parts and up to nine vertices. The program processed 388 faces including empty faces. It tests within-part transpositions wherever available and a swap of two equally-sized first parts where applicable. A success result means those *finite* instances agree; no finite computation is asserted to establish the all-parameter theorem, integral torsion-freeness, or the full integral group-module structure. Those follow instead from the homotopy-pushout, join, and natural pair-sequence arguments in `RESULT.md`.

No outside verification, independent review, or external certification has been carried out. The first posted date for the motivating source was checked against its arXiv page. Exact source comparisons and remaining originality risks are in `REVIEW.md` and `AUDIT.json`.
