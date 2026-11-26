---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The states are six-subsets of the fixed plane, with no quotient by projective automorphisms. Testing every line is equivalent to testing absence of collinear triples. An independent implementation tested all 54,264 candidates, found exactly 168 states, and reproduced the certified SHA-256 02ec2a9578cdf81b7773f1feeda922c745a0e539c8dbce7a8f76e91cd61d3694. It exhausted all 14,028 pairs: overlaps 0 through 3 occurred 840, 6048, 3780 and 3360 times, with the respective common-neighbour counts 4,5,16,11, and overlaps 4 and 5 never occurred. Noncomplete 40-regularity and positive common-neighbour counts for every nonedge give eccentricity two for every vertex; three is the first feasible replacement size. The parity classes have size 56 and cross-degrees 20. The independent integer matrix check reproduced the annihilating polynomial and traces 168,0,6720,73920,3346560. Symmetry and the distinct roots make the multiplicities uniquely determined by the five traces; 3360*11/3 gives 12320 triangles. Replay: /workspace/branches/2cee3254-5d1e-4a11-8d8f-e49be98c7391/independent_check.py and independent_result.json. The frozen verification scripts were inspected, not executed.

## originality

FAIL

A distinct indexed result covers the exact labelled exchange graph, the threshold and distances, and the entire common-neighbour table. Classical design data give the parity classes, and the spectrum, triangle count, and equitable cross-degrees follow from that table and those data by the incidence calculation below. The matched indexed entry is later-dated; this is a finding of substantive coverage in the audited corpus, not a claim of earlier publication or independent origin. Mere static overlap counts alone would not imply the common-neighbour table.

## value

FAIL

A complete exact reconfiguration answer on this natural design would be useful if distinct. Here the table and threshold add no distinct finite information to the matched result, and the spectrum and triangle count are mechanical consequences of that table and the classical incidence data. The frozen proof recomputes those consequences by enumeration and exact matrix arithmetic without obtaining a separate structural or downstream result. Exact verification is valuable as corroboration but is not a new exact-invariant contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
