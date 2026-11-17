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
# Reproducibility and verification

Run `python3 verify.py` in the directory containing the standalone script. It requires the Python 3 standard library only and terminates by assertions if any check fails.

The script generates every tetrahedral facet of \(C_m*C_n\) using independent cycle-edge pairs, enumerates every two-element face and all three complementary-edge partitions, and compares the constructed simplicial double against a separately generated \(K_{m,n}\sqcup(C_m\times C_n)\) graph. It explicitly checks the nonexistence of cross-block adjacencies, the total counts \(m+n+mn\) vertices and \(3mn\) edges, and every connected component's integral first Betti rank by \(e-v+1\). For the factorwise dihedral action it enumerates transformations, confirms vertex and edge orbits in each graph block, and exhibits an endpoint inversion in the direct-product block. Results for all 49 ordered pairs with \(3\le m,n\le9\) passed; the claimed theorem only requires \(m,n\ge4\).

Recorded output is in `verification_output.txt`; its last line is exactly `JOIN_CYCLES_DOUBLE_EXACT_PASS (49 ordered parameter pairs)`. The output also gives representative component counts for four sample parameter pairs. The source code and output are bundled as complete standalone artifacts with byte counts and cryptographic hashes.

The mathematical proof of the infinite-parameter statements is contained in `RESULT.md`: complete facet classification, parity/synchronized-walk connectivity, integral spanning-tree reduction, and the quotient edge-inversion argument. The finite checks are not a proof by induction, exhaustive enumeration of infinite parameters or independent external assessment. The source complexes, groups and quotient are all defined explicitly in the result.
