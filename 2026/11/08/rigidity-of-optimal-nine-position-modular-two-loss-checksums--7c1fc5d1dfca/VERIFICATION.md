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

# Reproducibility

Run the self-contained `checker.py` with Python 3:

```sh
python3 checker.py
```

It exhaustively visits 3,455,863 prefix search nodes and finds 216 nine-element pair-sum-distinct subsets of the cyclic group of order 56 containing zero. Every anchored set must coincide with one anchored affine image of the representative. It constructs 1,344 distinct affine images, verifies all of their 36 pair sums, and checks the double-counting identity.

An independent C++17 implementation can be run with

```sh
c++ -std=c++17 -O2 independent.cpp -o check_independent
./check_independent
```

Expected stderr includes `nodes=3455863 containing_zero=216 orbit_count=1`. No external dependencies, databases, or network requests are needed for replay.

**Logical completeness:** sorted search with root zero and every possible subsequent greater residue visits each anchored valid nine-set exactly once; a branch is pruned only on a repeated pair sum or insufficient remaining larger residues. The finite run verifies the explicit classification, not the earlier published global minimum-modulus theorem. The archived 2004 numeric minimum and the 2026 checksum motivation are cited separately. This check is self-reviewed, not independently audited.
