---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

PASS: Reconstructed the two-step GMRES normal equations m1-am2+cm3=0 and m2-am3+cm4=0 for moments m_j=Σb_i²λ_i^j. Strict Cauchy–Schwarz for ≥2 active eigenvalues implies c=(m1m3-m2²)/(m2m4-m3²)>0. Pair expansions show a/c is a positive weighted average of distinct active λ_i+λ_j, hence ≥2μ, forcing every x2_i=cb_i(a/c-λ_i)≥0 if κ≤2. For κ>2 the family diag(1,κ/2,κ) with δ² less than (κ-2)^3/[κ^4+16(κ-1)^2] makes high coordinate negative. Independent exact rational example diag(1,3/2,3), b=(1,1,1/20) gives a=833/545, c=306/545, x2=(527/545,374/545,-17/2180). Two active eigenvalues terminate exactly. Analytic proof all κ; finite witness only corroborates.

## originality

FAIL

FAIL: Published Resultary paper dated 2026-10-04 “Condition two is the sharp second-iterate positivity frontier for MINRES” explicitly covers ALL SPD Stieltjes systems, hence all diagonal SPD systems, and contains the exact SAME weighted pair-sum m1m4/m1m3 moment identity, universal κ2 boundary, same diagonal sharpness family diag(1,κ/2,κ), and SAME δ² threshold. For symmetric A, unpreconditioned exact GMRES and MINRES both minimize identical residual norm over identical K2 and therefore output the identical x2. Full published primary RESULT.md inspected: direct dominating-prior implication, not title coincidence or merely shared parameter.

## value

FAIL

FAIL: The current diagonal GMRES claim is an exact special case of a previously published stronger Stieltjes MINRES theorem via standard GMRES=MINRES residual-minimization equivalence on symmetric matrices; it adds no unproved natural invariant, new boundary, new class or materially novel computation. Exact independent verification of a different κ3 witness does not create a distinct mathematical contribution. Reject scientific claim as covered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
