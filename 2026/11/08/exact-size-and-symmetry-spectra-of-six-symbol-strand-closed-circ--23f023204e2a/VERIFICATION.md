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

Place `direct_verify.py`, `chamber_verify.py`, and `representatives.csv` together in one directory and run:

```sh
python3 direct_verify.py
python3 chamber_verify.py
```

The direct program enumerates exactly \(3^9=19683\) independent three-state complement-orbit choices, rejects directed cycles using DFS, and prints the complete \(16\)-coefficient size distribution. It independently forms all equivalence orbits of the complement-preserving \(48\)-element permutation group, counts each class by size, and verifies all \(220\) rows of the included representative table.

The second program enumerates \(48\cdot2^9=24576\) symmetric-order/subset pairs, deduplicates their resulting codebooks, and verifies the complete labeled distribution independently. It computes the number of equivalence classes by a fixed-point Burnside calculation, not the first program's canonical-representative method. For one and two complement pairs it checks the smaller totals \(3\) and \(65\); for three pairs it checks \(8383\) and \(220\).

Actual replay results:

```
DIRECT_VERIFY_OK blocks= 9 codes= 8383 max= 48 inequivalent= 220
CHAMBER_VERIFY_OK 1 3
CHAMBER_VERIFY_OK 2 65
CHAMBER_BURNSIDE_VERIFY_OK 3 8383 220
```

Both programs print the exact coefficient vectors in the finding. The exhaustive enumeration is a proof of these specific finite coefficients because its finite state space and acceptance test have an independently explained bijection; it is not a proof of unclaimed general-alphabet formulas. No independent external assessment was performed.
