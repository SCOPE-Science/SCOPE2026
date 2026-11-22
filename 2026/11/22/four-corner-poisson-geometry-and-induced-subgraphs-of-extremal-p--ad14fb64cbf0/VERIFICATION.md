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

# Verification

Run `python3 verify.py` with standard Python 3 in the same directory. It successfully exhaustively tests the inversion graph of all 46,232 permutations of sizes 2 through 8, with 725,756 degree/complementary degree identities, 60,548 exact corner-adjacency identities, and 14 exact expected-corner-count / factorial moment identities. Successful output:

```
PASS permutations=46232; degree_identities=725756; corner_edge_identities=60548; exact_moment_identities=14
```

The checker uses only the standard library and has no external input files. The analytical proof, not enumeration, establishes the infinite four-Poisson-process limit and the marked induced-graph convergence. A finite check does not certify asymptotic novelty, nor do failed literature searches prove priority. Independent validation has not been performed.
