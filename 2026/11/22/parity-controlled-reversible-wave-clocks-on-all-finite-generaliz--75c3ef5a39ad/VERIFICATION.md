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

The following two self-contained Python 3 files are included in this record:

- `verify_symplectic_examples.py`: constructs the symplectic generalized quadrangles \(W(3,p)\) for \(p=2,3,5\), checks the exact incidences, compares \(A^3\) and \(A^4\) against the predicted bipartite all-ones operators, checks \(T^8=I\) or \(T^{24}=I\) and rejects all proper divisor orders, and compares predicted and directly computed dimensions of \(\ker(T^k-I)\) for \(k=1,2,3,4,6,8,12,24\).
- `verify_grid_and_duads.py`: independently builds the duad–syntheme generalized quadrangle and two thin point–line grids, uses dense matrix multiplication and elimination over \(\mathbb F_2\), and verifies exact periods, projector identities, Jordan multiplicities and fixed-space dimensions.

Both scripts were executed successfully from the exact files included in the result. This is computational corroboration only. The infinite-family period and rank formulas are established by the mathematical derivation in RESULT.md, which is sensitive to the precise definitions and parity cases. No external independent audit is asserted.
