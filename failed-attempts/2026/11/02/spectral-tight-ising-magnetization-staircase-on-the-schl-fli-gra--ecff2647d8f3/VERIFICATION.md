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

The line-intersection construction yields the skew graph with degree 16, 216 edges, and common-neighbor parameters 10 and 8. On the mean-zero subspace the strong-regularity equation A²=2A+8I+8·11ᵀ gives eigenvalues 4 and −2. The indicator decomposition gives e(T)≥k(k−3)/3, and b(T)=16k−2e(T) gives the rounded upper bound, with complements covering the other half. An independent implementation enumerated all 134217728 subsets, checked the sector visit totals against binomial coefficients and the update against direct edge sums, and reproduced saturation and every labelled count. The successive slopes in the k≤13 cut envelope are 16,12,8,4,0; maximizing B(k)−(h/J)k gives exactly the plateau magnetizations and the four-sector ties at the stated fields. At zero field the four sectors k=12,13,14,15 have optimum cut 120, giving energy −24J, the stated counts at M=±1 and ±3, and total 1037376. The positive critical sector sums are 630444, 138000, 10035 and 208. Global spin reversal accounts for the negative fields.

## originality

FAIL

A distinct existing indexed record, 0fea274efa26, gives the same complete mathematical claim: the all-cardinality cut profile, labelled counts at every cardinality, five plateaux, and every critical and zero-field degeneracy and sector. The floor form of its profile is algebraically identical to the ceiling form here. The coverage is exact and leaves no distinct main result for acceptance; it is not a correctness objection or a judgment of historical priority. The mirror path for the matching record bears a later date than the path of the frozen record, and there is no finding here about who established the result first.

## value

FAIL

A complete field-dependent cut and degeneracy law for this natural finite graph is a worthwhile invariant in itself. As a distinct finding here, however, no additional meaningful invariant survives the exact indexed match. Alternative witnesses and an independent reproduction give confidence in the common result, but do not add a new mathematical conclusion to the existing table and theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
