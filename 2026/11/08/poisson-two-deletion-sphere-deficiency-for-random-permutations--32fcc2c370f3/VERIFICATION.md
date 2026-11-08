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

Run `python3 CHECK.py` with standard Python 3. The checker enumerates 46,224 permutations of lengths 4–8 and 400 reproducible random larger permutations, comparing direct standardized spheres to the deterministic bound. (Total 46,624 cases.)

The proof of the infinite law uses: (a) the deletion-equivalence graph and nearby-pair deterministic inequality on disjoint bond events, (b) bounded expected nearby-pair count, (c) vanishing probability of overlapping bonds, and (d) factorial-moment convergence to Poisson(2). Exhaustive finite enumeration does not establish the limit; the published notes include its complete mathematical argument.

No independent audit has been carried out. Historical priority is not guaranteed by search results.
