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
# Finite exact verification

Run `python verify.py` in the directory containing this file. The checker independently enumerates all connected edge subsets of size \(a+b-1\) in small complete bipartite hosts, determines marked distances by breadth-first search, and compares the resulting exact rational tail probabilities with the formulas in `RESULT.md`. Its matrix-tree cofactor calculation uses fraction-free elimination, not the factorized determinant identity in the proof, to check the contracted-path count for all positive part sizes through eight. Further exact rational checks establish nonincreasing survival tails and terminal vanishing up to size 29.

The run completed with `PASS 83789 exact assertions`. No floating-point simulation, external symbolic package or unproved computational extrapolation is needed. The finite computation does not establish the universal theorem or its limit; the independent mathematical steps are the contraction cofactor, path enumeration, telescoping and product asymptotics. No independent scientific audit has been performed.
