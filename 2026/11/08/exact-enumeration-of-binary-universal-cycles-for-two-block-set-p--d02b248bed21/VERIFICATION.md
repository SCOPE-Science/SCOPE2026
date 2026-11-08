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

The mathematical proof is in `RESULT.md`. The following tests were actually executed against the standalone program files embedded in the same package:

1. `python3 verify_binary_ucycles.py`: enumerates every indexed binary circular word of lengths \(3,7,15\), checks distinct nonconstant complement-pair windows of respective lengths \(3,4,5\), computes rotation/complement orbits, and checks the cyclic-XOR characterization. Output ends with `DIRECT_CENSUS_OK`; the exact (rooted words, orbit classes) counts were \((6,1),(28,2),(480,16)\).
2. `python3 verify_tree_counts.py`: constructs the exact directed Laplacian of the binary length-\((m-1)\) overlap graph with the zero self-loop deleted, and computes a root-zero minor using fraction-free integer elimination for each \(m=2,3,4,5,6\). Output ends with `TREE_CERTIFICATE_OK` and the resulting integers are \(1,2,16,2048,67108864\).

Both programs use the Python standard library only. The second test uses exact integer division, not floating-point determinants. The first exhausts every indexed word only for the stated finite lengths. Neither can certify the infinite family or historical priority independently. The all-order proof uses adjacent XOR integration, a uniquely missing self-loop, an adjacency-matrix power identity, and the directed matrix-tree and BEST theorems.

Independent scientific audit: not performed.
