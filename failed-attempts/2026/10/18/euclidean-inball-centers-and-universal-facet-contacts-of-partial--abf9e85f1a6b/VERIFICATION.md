---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

A length-k prefix has Frobenius normal length sqrt(k), so intersecting the shifted halfspaces characterizes every radius-r center. For m<=n, the n first-row entry lower bounds and the first-row total upper bound give (n+sqrt(n))r<=1. The constant matrix attains equality; equality forces the whole first row and, when square, the first column. The explicit perturbations in RESULT.md lines 50–52 give strict slack in every genuinely unforced inequality, proving the affine dimensions and showing that the listed universal contacts are the only contacts at every relative-interior center. At the constant center only length-one lowers and length-max(m,n) uppers can tie. Deduplicating the top-left lower constraint and checking the distinct facets gives the claimed counts. The wording about uniqueness in line 32 means that the optimal center is not unique, not that an individual ball lacks a unique geometric center.

## originality

FAIL

A distinct indexed PASM/partial-permutation comparison gives the same PASM radius, forced entries, affine-dimension law and relative-interior contacts. It is catalogued later, so this is established coverage in the examined evidence, not evidence that someone published the claim earlier or a conclusion about discovery priority. The full shifted description is exactly the ordinary erosion of Heuer–Striker's known prefix system at the already stated radius. The extra constant-center counts then follow mechanically from that system: a lower is tight iff k=1 and an upper iff k=L; the facet list makes the count immediate. No distinct substantive remainder is established by those counts.

## value

PASS

The complete PASM incenter geometry is a useful classification: it captures nonuniqueness, the square-versus-rectangle change in the affine hull, and the distinction between forced and movable facet contacts in the original metric. This assessment concerns the mathematical content of the whole claim. The extra constant-matrix count alone does not justify a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
