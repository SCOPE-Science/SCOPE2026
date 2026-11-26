---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For a nonzero element a to be fixed on both sides by gh=(i,c,λ), its indices must be (i,λ), the relevant sandwich entry p=p_{λi} must be nonzero, and cp=1. Thus outside the full identity the only domains are {0} and U_e={0} plus the maximal subgroup at a supported position. For e=(i,λ), f=(j,μ), put q=p_{μj}. If g=(i,x,μ), h=(j,y,λ) and xp_{μj}y=p⁻¹, then hg is the idempotent at f. In the coordinates ρ_e(a)=a_group p, the new coordinate is y p a_group p x q=(yp)ρ_e(a)(yp)⁻¹. Conversely arbitrary t is obtained with y=tp⁻¹ and x=p⁻¹y⁻¹q⁻¹. One identity factor alone gives a local identity or bottom; two give the full identity. Distinct local domains meet only at 0, so mismatched compositions are the bottom map on {0}, and matched compositions multiply conjugations (inverse coset labels under right action). Distinct labels are exactly cosets mod Z(G). With one support entry regularity forces one row and column, so the local identity is global; otherwise global identity is new. Minimal nonzero idempotents and their maximal groups recover |E| and G/Z(G) also at infinite cardinalities.

## originality

PASS

The completely zero-simple classification with arbitrary regular sandwich support answers a question explicitly posed in the inspected antecedent. The inverse Brandt, group and zero-free ingredients are not independently novel; the supported distinction is the full zero-matrix class and loss of all support geometry beyond its cardinality.

## value

PASS

The theorem gives the composition law and an intrinsic classification for a standard semigroup class, in direct response to Problem 7.5. In particular, semigroups with very different support geometry and even different finite cardinalities can have the same partial-inner monoid. This follows from the theorem for arbitrary groups and supports, not merely from sample coincidences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
