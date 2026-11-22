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

Two independent finite, integer-only enumerations were executed successfully:

```
python3 verify_dfs.py
python3 verify_matching.py
```

The exact outputs are included in `dfs.out` and `matching.out`. They agree that there are 1344 distinct Hamiltonian cycle edge sets, zero singleton coefficients at all 32 edges, no zero doubleton coefficients, and exactly 1120 zero triple coefficients. All complete coefficient histograms coincide. The anchored-DFS program additionally checks that the 384 cube automorphisms have 24 triple-support orbits, six of which are zero, and exhaustively enumerates all 16 four-edge vertex-star cuts. Each program uses only the Python standard library and raises an exception on a failed numeric check.

The proof of exhaustiveness of both searches is recorded in `RESULT.md`: every Hamiltonian cycle is an anchored traversal counted in both directions, and equivalently a connected union of two disjoint perfect matchings. Integer summation is exact; there are no sampling claims, unproved asymptotic extrapolations, or external verification assertions. Verification here covers only the stated degree-at-most-three Fourier theorem and its finite cut/orbit certificate. Independent audit is not yet performed.
