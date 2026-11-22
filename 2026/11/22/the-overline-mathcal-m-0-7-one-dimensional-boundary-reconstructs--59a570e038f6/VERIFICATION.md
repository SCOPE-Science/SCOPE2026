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

# Reproduction and limits

From a directory containing both attached auxiliary files, execute:

```sh
python3 verify_boundary7.py > reproduced.json
cmp reproduced.json CERTIFICATE.json
```

The checker uses the Python standard library only. The source constructs the \(56\) permissible leaf splits by seven-bit masks and tests split compatibility for every three- and four-split subset. Independently, it inserts leaves into all edges of binary trees and contracts internal edges, then asserts equality of the resulting \(1260\)- and \(945\)-element sets. For each of the fifteen partitions of seven it computes exact cycles on both sets and verifies the one-dimensional injectivity, the four-degree obstruction, the five-degree sufficiency and sharpness, and exactly four zero-dimensional collision pairs. `CERTIFICATE.json` contains complete numerical output, not a substituted log.

The argument is an exact finite classification of all permutation classes, so it proves the claimed universal finite-field statement by Galois descent. It is **not** a computation of rational points of each positive-dimensional stratum, of cohomology or Chow groups, or of any higher-marking moduli space. Independent audit has not been performed.
