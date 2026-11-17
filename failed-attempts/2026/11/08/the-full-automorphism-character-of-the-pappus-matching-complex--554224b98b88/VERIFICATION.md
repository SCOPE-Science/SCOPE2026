---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The cubic 18-vertex LCF Pappus graph has 27 edges; its ordinary matching complex has 35,367 nonempty matching faces and 40-dimensional reduced rational H5 using supplied full mod-two boundary ranks and Euler χ~=-40. The submitted source correctly derives signed Lefschetz trace as the independence polynomial at -1 of admissible graph-edge orbits; independent finite code enumerated all 216 graph automorphisms (backtracking adjacency preserving), evaluated the orbit formula per element, found 11 cycle-profile types and trace multiplicities {-4:18,0:81,40:1,-1:36,1:12,4:32,-2:36}, agreeing with published full class function. Source uses a second direct oriented-simplex trace, examined in verify_pappus.py; correctness derives from Hopf trace and rational homology concentration rather than logs alone. All published values and invariant-zero are consistent.

## originality

FAIL

Exact earlier published Pappus matching-complex theorem provides the complete character on all 216 automorphisms, with 11 permutation-cycle profiles and values matching the submitted 13 conjugacy classes. The 13-class partition only refines profile labels and cannot yield a new character. Earlier full invariant dimension is zero; bipartition-subgroup invariant is readily computed from the same known signed trace and subgroup.

## value

FAIL

A complete rational character can be mathematically valuable when unknown, but this same full 216-automorphism class function was already published with all profile values. Partitioning known profiles into thirteen conjugacy classes and deriving a subgroup invariant is a redundant table calculation without a new useful invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
