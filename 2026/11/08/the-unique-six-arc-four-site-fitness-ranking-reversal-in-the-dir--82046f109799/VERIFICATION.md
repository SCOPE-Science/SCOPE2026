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

# Reproducible verification

Install Python 3.10 or newer and the packages in `requirements.txt`. From the directory containing all extracted files, run `python verify_symbolic.py` and `python verify_numeric.py`.

The exact-symbolic script enumerates all \(2^{n(n-1)}\) loopless adjacency patterns within the stated vertex/arc bounds (restricted to at most six arcs for four vertices), tests strong connectivity in both orientations, and deduplicates under all vertex permutations. It checks all isomorphism-class counts, constructs the \(2^n-2\) transient-state absorption equations, and verifies all nonzero site differences by exact rational functions of fitness. There are 113 nonidentically-zero comparisons; exactly one has a shifted-numerator polynomial with positive sign variations, and that one belongs to the stated directed graph. It verifies the explicit rational identity and the unique-positive-root certificate.

The second script independently builds and solves the witness graph's absorption system with standard-library exact fractions, using seven rational values of mutant fitness, including the neutral case, and checks the polynomial identity. Its matrix solver does not reuse the symbolic library.

The computations were rerun from the provided script files and both reported `PASS`. The finite graph census is exhaustive *only* for the bounded vertex and arc classes. The root uniqueness for the entire continuum of fitness values is obtained by polynomial sign arguments; finite spot checks alone would not establish it. No independent scientific audit was performed.
