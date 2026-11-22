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

# Reproducibility and boundaries

Run both supplied standard-library Python programs from the same directory as these files:

```sh
python tripartite_wave_check.py
python tripartite_direct_check.py
```

The first program directly constructs the adjacency and reversible-wave matrices over \(\mathbb F_3\), computes matrix powers independently and compares exact modular nullities against the proposed all-time formula. It passed 1,232 comparisons at 22 time indices for each of 56 size triples, and checked sharp global orders by all proper divisors.

The second program uses literal coordinate-by-coordinate updates and exhaustive temporal-orbit traversal for four small graphs, totalling 597,780 states. Its observed orbit data are:

- \(K_{1,1,1}\): primitive orbit lengths/counts \(1:9, 3:78, 9:54\).
- \(K_{1,1,2}\): \(1:3, 3:2, 4:6, 10:24, 12:4, 20:96, 30:16, 60:64\).
- \(K_{1,2,2}\): \(1:1, 2:1, 4:60, 5:16, 6:1, 10:16, 12:40, 20:960, 30:16, 60:640\).
- \(K_{2,2,2}\): \(1:1, 2:4, 4:1638, 6:39, 12:14196, 18:27, 36:9828\).

All computed populations sum to the full state-space sizes after multiplying each orbit count by its orbit length. The programs do not implement a symbolic proof for all sizes; the proof in `RESULT.md` establishes the all-size factorization. Characteristic-three finite-field extensions are handled by preservation of ranks under scalar extension, not by claiming exhaustive search over those fields.
