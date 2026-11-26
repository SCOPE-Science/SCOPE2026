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

The asserted spectrum is correct as a multiset indexed by isotypic blocks: d_j^2 is the contribution from block j, not the global multiplicity of a scalar shared by several blocks (notably zero). With normalized area the addition kernel after scaling is U_l(Re(g^-1 h))/(l+1). Character orthogonality diagonalizes this central kernel, and Clebsch–Gordan gives the stated affine E8 recurrence. Central parity cuts the regular representation to 60 dimensions; noncentral angles of denominators 2, 3 and 5 give the exact sixty-step shift after taking inner products, and vanishing of all noncentral kernel entries is equivalent to l+1 being divisible by 30. The independent recurrence gives ranks 59 and 60 at degrees 58 and 59 and the first full ranks at odd 13 and even 20; the shift proves full rank at every degree >=60, not merely within the checked range.

## originality

FAIL

The distinct earlier-indexed 10/25 record supplies the complete block spectrum up to a scalar normalization, the rank and period shift, and stronger parity-specific eventual cutoffs. The frozen all-tight-degree iff is not stated there in that form, but it is immediately implied by the same exact zonal kernel and the available noncentral angles pi/2, pi/3 and pi/5. This is a statement-level coverage finding, not a finding about authorship, dependence or publication priority.

## value

FAIL

An all-degree conditioning or rank classification on this natural configuration would be useful if unknown. Here the complete spectral and rank information already has an explicit equivalent record, and the only identified difference is the immediate three-denominator zero test from the known exact kernel. It does not leave a substantive independent sampling result to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
