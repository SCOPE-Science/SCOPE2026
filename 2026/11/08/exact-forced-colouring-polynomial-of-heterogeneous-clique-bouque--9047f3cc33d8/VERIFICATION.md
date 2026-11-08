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

# Computational reproducibility

Run `python3 artifacts/verify.py` from the extracted package root. It explicitly constructs each labelled clique bouquet, enumerates every initial partial assignment with a named chromatic palette, applies local colour forcing in a fixed deterministic eligible-vertex order, rejects non-proper final assignments, and tallies the forcing assignments by seed cardinality. The result is compared with the closed polynomial using a separately coded coefficient calculation.

The exhaustive tests use twenty-one specified blade vectors, including degree-two, friendship, mixed-size and complete-graph boundary examples; the largest tested graph has eight vertices. A second integer-identity loop covers \(2\le s\le14\), \(1\le t\le6\) and every \(1\le a<s\) for a family of larger symbolic parameters. A successful execution ends with `VERIFY_OK`.

This finite verifier cannot prove the all-parameter theorem or historical originality. The general proof is in `RESULT.md`. The file has no external Python dependencies or network requests.
