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

# Exact verification

Execute `python3 verify_tritangent.py` with the companion `spence_second.txt` in the same folder. The verifier needs only Python 3. It independently reconstructs the 27 divisor classes and 45 canonical tritangent triples, checks the (45,12,3,3) graph parameters and the second catalogue graph, and calculates determinants via exact fraction-free Bareiss elimination.

For each graph, deleting vertices 0, 9 and 20 gives a 44-by-44 integral matrix with determinant \(3^{62}5^{23}\). Exact arithmetic modulo \(3^9\) and \(5^6\), using local-unit inversions, yields the valuation multiplicities displayed in RESULT.md. The prime valuations sum to the exponent of the determinant at each prime, and the determinant has no further prime factors. Successful replay prints `CUBIC_TRITANGENT_CRITICAL_GROUP_COMPARISON_OK`.

The included `spence_second.txt` contains the 45 binary adjacency rows from the second matrix in Spence's published (45,12,3,3) catalogue. The calculation is an exhaustive finite proof for these two matrices; it does not establish priority over every historical graph-invariant table or classify other catalogue entries.
