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

# Exact-integer verification

Execute `python verify.py` beside the two CSV certificates. No external Python packages are required. The verified standard output is:

`Q3_SPANNING_TREE_WALSH_EXACT_PASS trees=384 frequencies=4096 orbits=144 rank=2574 lambda=14243/1024`

The checker enumerates every seven-edge subset of the cube and independently evaluates all 4,096 signed weighted Matrix-Tree determinants using fraction-free integer elimination. It agrees with the direct exact Walsh–Hadamard transform of the tree indicator, checks the exact coefficient histogram and two Parseval identities, computes all 48 cube edge automorphisms and their 144 signing orbits, and checks direct projection-kernel sums for every orbit representative. It also checks the complete frequency and orbit certificate files by byte equality with regenerated results.

The result is fully exhaustive for the finite three-cube. The general translation-averaging step is an ordinary mathematical argument independent of computation. No external audit has been performed; the certificate is not an infinite-dimensional assertion.
