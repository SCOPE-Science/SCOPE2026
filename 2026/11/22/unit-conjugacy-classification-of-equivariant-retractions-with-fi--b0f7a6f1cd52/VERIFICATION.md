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

## Verification protocol
The attached `verify.py` independently enumerates equivariant idempotents from their actual orbit maps; it does not invoke the conjugacy-orbit formula when constructing the maps. For each test case it checks labeled idempotent counts against the independent root-selection formula, checks the set of observed profiles against the exact coefficient support of the stated Euler product, and checks the size of every profile bucket against the closed orbit-size formula. It also generates conjugation moves using explicit automorphism generators and checks reachability of every element in each profile bucket.

## Executed checks
`python verify.py` completed with `GSET_RETRACTION_UNIT_ORBITS_VERIFIED cases=33`, including cyclic groups of orders two and three and nonabelian \(S_3\). The saved `verification_output.txt` contains the complete console output. This is a finite consistency check of the specified test dimensions, not an infinite proof; the general argument uses a direct rooted-fiber classification, all-phase normalization, and factorial labeling.

## Reproduction and boundaries
Run `python verify.py` using Python 3 and its standard library only. The program's path-independent enumeration is finite; it does not claim exhaustive testing over arbitrary finite groups or arbitrary orbit multiplicities. No independent review has been performed.
