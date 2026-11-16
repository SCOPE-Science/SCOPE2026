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

# Exact checks and limits

Execute `python verify_edge_cover_spectrum.py` from the directory containing this document. Dependencies: Python 3, NumPy and NetworkX. The program generates the accompanying CSV files deterministically, and they can be compared byte-for-byte with the provided certificates.

For each \(2\le n\le7\), the script enumerates all \(2^{\binom n2}\) edge masks, marks those meeting every vertex, and performs a complete integer fast Walsh transform. Separately it builds clique masks from vertex subsets and performs an integer subset-zeta transform to calculate the signed independent-set expression. It asserts exact equality of every coefficient, Parseval, edge-cover counts, zero counts, sharp gaps and two-adic properties. For \(n=5,7\) it computes independent-set polynomials and automorphism counts over the standard nonisomorphic graph atlas, and checks that weighted orbit multiplicities account for every vanishing multiplier. At \(n=7\) the independent algorithms agree on all \(2{,}097{,}152\) Walsh coefficients. The expected final marker is `EDGE_COVER_COMPLETE_GRAPH_FOURIER_EXACT_PASS n7_orbits=39 n7_zeros=73115`.

This checker establishes finite statements only; the all-order parity and sharp-gap claims are proved algebraically in `RESULT.md`. The graph atlas class enumeration is used for orbit labels; the full Walsh transform independently verifies the total zero count. No external independent audit has been carried out.
