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

For the unitary normalization U of F_G the restricted matrix is a compression between coordinate subspaces, so its singular values are at most one; its squared Frobenius norm is |R||C|/|G|. Equality occurs exactly when each nonzero singular value is one. With Q=UP_CU*, the defect of P_R Q P_R from idempotence is the positive operator ((1−P_R)QP_R)*((1−P_R)QP_R), hence equality holds exactly when P_R and Q commute. Its mixed block has Fourier-indicator entries at χψ⁻¹ for χ in R and ψ outside R. A character difference η is absent from this block exactly when η preserves the complement of R: inclusion follows from absence and upgrades to equality by finiteness. Thus commutation means support of the Fourier transform of 1_C is contained in H_R, which by inversion is exactly H_R-perpendicular periodicity; the dual assertion follows by exchanging the restrictions. At order twelve stabilizer size divides 6 and 12/|H_R| must also divide 6, so the only cases are orders 6 and 2. The first gives 2 parity choices for R and 20 antipodal-union choices for C; the second gives 18 non-parity antipodal-union choices for R and 2 parity choices for C. Thus the analytically classified rank-three stratum has 76 pairs. For the full census, independent translations preserve rank by diagonal rephasings, and a fresh computation with different primes regenerated all 80 orbits and 6400 representative pairs, weighted by the orbit-size products to cover all 853776 set-pairs. The matching ranks modulo 50053 and 50077 are exact: a nonzero k-minor has nonzero integer norm bounded by k^(2k)≤6^12 from the four conjugate Hadamard bounds; vanishing in both reductions would force its norm divisible by 2506504081>6^12. A minor detected in either field certifies a nonzero complex minor. This verifies exact weighted counts 76, 5376, 150564, 697760 and independently checks the rank-three configurations. The calculation is exhaustive through symmetry, not 853776 separate eliminations.

## originality

PASS

Credit the classical Fourier uncertainty ideas, low-rank subgroup constructions and adjacent full-spark and rank-incidence results. The supported distinct claim is the complete half-size rank stratification and its exact minimum-rank pairs, with a general annihilator-periodicity equivalence. The available statements do not give or imply that combination. The Kronecker-product literature and potential data behind an aggregate minor count remain material priority risks; the pass is on available evidence, not a finding that either inaccessible source does not cover it.

## value

PASS

Sampling at half the ambient dimension is a natural square Fourier recovery problem, and order twelve admits genuine subgroup obstructions at exactly half size. Knowing which row sets fail full spark does not distinguish the 156016 singular pairs by nullity or identify the exact 76 deepest failures. The census supplies that distinction, while the projection argument explains the deepest failures by a usable necessary-and-sufficient dual periodicity criterion rather than a table of individual witnesses. This gives an independently useful finite benchmark and a structural result for arbitrary finite abelian groups.

The dated certificate retains the supplied scientific assessment, sources and limitations.
