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

A deleted-matching pair has a length-three interval containing every vertex, including at n=3. Without a selected matched pair, an omitted a_i can only be covered by two selected B vertices with indices different from i, and vice versa. Outside the two full-shore cases, both shores have omissions; if J is nonempty, an index of J is such an omitted A index and forces |J|>=3, and J empty also fails to cover an omitted A vertex. Symmetry yields the disjoint 3+3 threshold. Weighted index states give the matched-pair term; the disjoint k-index assignment excludes 2(1+k+binom(k,2)) choices. Monotonicity then leaves exactly the stated minimal types and gives g^+=n and n+2+20 binom(n,6).

## originality

FAIL

A distinct indexed finding states the same theorem for precisely the same graphs and ordinary geodetic sets, down to all coefficients and the minimal-set types. It also explicitly states g^+=n and the equivalent total minimal count. A qualifying distinct contribution of the frozen finding is not established. This is a judgment of equivalent coverage, not an attribution or a judgment of priority from the displayed dates.

## value

PASS

As mathematical content, the full set classification resolves a natural distance-coverage question for a connected family whose missing edges produce distance-three pairs; it determines the size spectrum and inclusion-minimal witnesses rather than retabulating the scalar minimum. This does not establish a distinct contribution relative to the matching indexed result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
