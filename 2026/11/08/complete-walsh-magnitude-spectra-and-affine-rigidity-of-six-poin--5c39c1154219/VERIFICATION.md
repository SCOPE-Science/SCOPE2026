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

Run the bundled `CHECK.py` with Python 3; no dependencies are required. Its complete six-subset enumeration for dimensions three and four uses integer-only XOR, rank, and Walsh-sum arithmetic. The predicted class counts in dimension four are \(840,6720,448\); the program tests them, all magnitude multiplicities, and one canonical representative for each of the four types in dimension five.

Observed final line: `CHECK_OK exact_subsets_3d=28 exact_subsets_4d=8008 canonical_5d=4`.

This numerical run verifies finite instances, not all ambient dimensions. The all-dimensions claim follows from the supplied affine-relation classification, the pair-sum fourth-moment identity, and the exact integer linear system. A relevant general Boolean-function paper could not be compared in complete full text, so the literature-overlap assessment has that explicit limitation. Independent mathematical audit has not been performed.
