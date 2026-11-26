---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Reviewed the zero-diagonal open-neighborhood convention, including centers on supports, and reproduced the whole census independently. In F_7[i] the norm of a+bi is a^2+b^2 and is u^8 on nonzero u; the square test is exactly membership of the norm in {1,2,4}, with zero excluded. Replay /workspace/audit-replay/4.py traverses unanchored increasing supports, partitioning all 49 centers by traces as each vertex is appended. Both splits of every previous trace cell must be nonempty; a failed prefix legitimately precludes a shattered superset. Counts are (1,49,1176,18424,199920,4704) exactly; 49 centers rule out 64 required traces at size six and thus all larger sizes. Applying the 2352 explicitly defined semilinear maps to each of the displayed representatives gives 2352 distinct images per orbit, disjoint, with union all shattered five-sets; this verifies freeness for the named group without claiming it is the full automorphism group. Enumerating the five four-faces of each five-set gives exactly 11760 faces of degree two and no positive degree other than two. All other 188160 shattered four-supports are maximal by heredity, and five-facets also exist. Counts and replay output are in /workspace/audit-replay/4.txt. The exact computation is a finite exhaustion for this one graph, not a bound extended to other fields.

## originality

PASS

Best-of-knowledge pass on the full arbitrary-support polynomial and the free orbits and facet-extension distribution. The quadratic-residue VC framework is known. The exact historical priority of the bare VC dimension at 49 remains unresolved and is not needed for this distinct census. Neither generic VC statements nor fixed consecutive character tests give the full arbitrary-support result in the material accessed.

## value

PASS

The quadratic-residue translate class is a standard finite-field test of shattering. Order 49 is a small quadratic-extension case in which five queries are possible but six are ruled out, so the rank limit is natural. The exact fifth-face count, its two symmetry types, and the nonpure maximal fourth layer describe incidence structure a researcher cannot recover from VC dimension or strong regularity alone. This is a complete finite classification, not significance inferred from a single software run or a selected witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
