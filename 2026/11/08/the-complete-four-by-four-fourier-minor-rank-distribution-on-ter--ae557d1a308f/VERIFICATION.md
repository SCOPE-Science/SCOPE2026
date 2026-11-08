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

# Reproduction and mathematical boundaries

Run `python3 checker.py` in a Python 3 environment. No third-party packages or external datasets are needed. The checker exhaustively enumerates projected column subsets of sizes one through four in the nine-point and twenty-seven-point local spaces; evaluates every required rank from exact Eisenstein-integer minors; independently verifies it by split-prime modular elimination under a determinant-norm bound; and reproduces the local histogram and global counts in dimensions three through six. Success is indicated by `TERNARY_FOURIER_RANK_CENSUS_PASS`.

The all-dimensional conclusion does not follow from those sample dimensions: it follows from the displayed exact affine-orbit classification, complete finite local histogram, combinatorial fiber occupancy identities, and symbolic polynomial simplification. The finite checker certifies the nontrivial local table; the written proof supplies the extension to every dimension. It is not an independent external audit, nor a historical-priority certificate.
