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

The geometric sources give the transitive 36-point orbit, dihedral order-ten stabilizers, reflection axes, and faithful stabilizer action on the five incident lines. The unique order-five subgroup of each stabilizer bijects the orbit with the 36 such subgroups; the stabilizer is its normalizer. A stabilizing involution cannot have the point as isolated center because then it fixes the pencil pointwise; hence its axis is incident. The five such involutions exhaust the incidences at that point. I constructed the matrix independently: cycle each five-element subset and enumerate its reflections j↦k−j, deduplicating the reflection sets. This gives 81 vertices, 180 edges and the two stated degrees. The cofactor determinant and Laplacian characteristic polynomial confirm connectivity, the claimed spectrum products and 2^56·3^24·5^25 trees. Exact integer Smith form gives 1(52), 2(8), 4(3), 20, 60(8), 1800(8), with multiplicities in parentheses. The finite graph proof neither assumes sampled geometry nor uses the other Wiman strata.

## originality

PASS

The Wiman geometry and the full-strata arithmetic result are real overlaps; the specific integral group of the quintuple-only Levi graph remains distinct on the checked evidence. This is not a priority certificate.

## value

PASS

The highest-multiplicity points form a distinguished orbit of this complex reflection arrangement, so the graph is motivated independently of its output. Its full integral divisor class group is a reusable exact invariant, substantially more informative than its incidence counts or tree number. The all-strata group does not substitute for the distinguished-stratum invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
