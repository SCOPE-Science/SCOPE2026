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

# Exact reproducibility checks

The supplied C program reconstructs the 24 group elements and their multiplication from permutation images, enumerates each strictly increasing four-index support exactly once, constructs the 24-by-24 regular convolution matrix and computes its rank in the prime field of order 1,000,000,007. A proof in `RESULT.md` shows every integral minor has absolute value at most \(2^{24}\), strictly smaller than the prime. Therefore the modular rank equals its characteristic-zero value with no heuristic prime avoidance. The C program also closes the three normalized support differences under group multiplication to determine subgroup order, verifies all rank and subgroup multiplicities and exits nonzero on a mismatch.

The separate `independent_verify.py` reconstructs the group afresh, partitions all 10,626 supports into 34 exact two-sided-translation/inversion orbits, and uses exact rational arithmetic to calculate the rank for each representative. The orbit sizes give the identical histogram. The program `block_verify.py` then constructs the dimensions \(1,1,2,3,3\) Fourier blocks via standard permutation and sign-twisted representations, verifies the rank sum on all 34 representatives, and counts 18 distinct block-rank profiles.

To reproduce, execute the four commands in `RESULT.md` within the package directory. Reference outputs are included in five accompanying `.out`/`.tsv` files. Actual code execution and comparison with these outputs were performed. The result does not claim bounds on singular values, arbitrary coefficients, larger groups, or independent human verification.
