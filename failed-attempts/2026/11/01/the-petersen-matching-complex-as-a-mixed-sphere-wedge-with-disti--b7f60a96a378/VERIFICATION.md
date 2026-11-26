---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Independent replay (python3 /workspace/branches/independent_petersen.py) generates all 331 nonempty matchings by recursive disjoint-edge extension, checks the 160 pairs and acyclicity on all 975 Hasse arcs, and obtains one critical vertex, five 2-cells, five 3-cells and zero integral differential. Hurewicz identifies each 3-cell attaching class with its degree vector in the simply connected wedge of 2-spheres, so these attachments are null. The replay builds actual integral cycles lifting the critical cell generators and transports them by signed label permutations before projecting; exact traces are (5,−3,1,2,0,−1,0) and (5,1,1,−1,1,−1,0) in the seven stated classes, without modular lifting. These are the signed point character and the 2-set permutation character less the point character, respectively. After equivariant subdivision, quotient chains are orbit coinvariants with rational coefficients, and averaging identifies homology with invariants; the sign-twisted point module contributes precisely one invariant on A5 and none on S5, and the Specht module contributes none on either. This proves rational quotient homology, not a quotient homotopy type or an integral module classification.

## originality

FAIL

Earlier 10/18 and 10/25 indexed records expressly identify the same rational modules for the same natural action, and the 10/25 record e49761e9c933 already gives both rational quotient conclusions. Distinct same-day records directly exhibit the same wedge and same representations; date alone does not assign priority. Earlier exact wedge citations in the inspected 10/25 records strengthen the coverage, but the direct same-object substantive overlap is decisive without inferring priority from the same-day records.

## value

FAIL

Distinguishing equal-rank homology modules and comparing symmetry quotients are meaningful questions, but their answers and the wedge type are already covered. The frozen work adds no integral module, equivariant wedge, integral quotient homology, or other distinct mathematical conclusion. The alternate verification is confirmation, not a surviving new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
