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

# Reproducibility and limitations

The standalone `CHECK.py` uses Python 3 standard libraries only. Execute `python3 CHECK.py` in the directory containing the extracted files. A successful exact run prints the eight PASS lines reproduced in `CHECK_OUTPUT.txt`.

The checker reconstructs all twelve vertices as ordered pairs of distinct tetrahedral labels; their eighteen undirected edges are obtained from common first coordinates or reversal. It tests all 495 induced eight-vertex subgraphs, constructs the 252 complementary facets, and closes these under taking faces. Every absent triangle receives an explicit existing-vertex cone filling. The resulting simply connected two-skeleton has integral cycle-lattice rank 55. The code checks signed chain composition, computes the full third simplicial boundary, and obtains 143 integral unit pivots with zero residual. Mod-two reduction independently confirms its rank. These yield the exact integral homology groups.

The wedge decomposition is a mathematical consequence of the simply connected two-skeleton and the primitive integral degree matrix of the three-cell attaching maps. The code does not certify bibliographic uniqueness and does not constitute an independent external audit. No computations or missing artifact paths are required from other packages.
