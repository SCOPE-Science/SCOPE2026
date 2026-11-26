---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

PASS applies to repairs/1/RESULT.md. The frozen proof of uniqueness omitted the feasible interval 1/2<t<1 and asserted a sign at t=1/2 without limiting it to feasible budgets. The latter need not hold off-domain (e.g. μ=q=0.01). The repaired proof restricts all derivative comparisons to |t|≤q; for 1/2≤t<1 it compares t/a(t)≥(1−t)/b(t) and 0<m−a(t)<m+1+b(t) to obtain a strictly positive derivative. For t≥1 both derivative contributions are nonnegative with the first strictly positive; for t≤0 the derivative is strictly negative. Between 0 and 1/2 the two positive terms are respectively increasing and decreasing, which gives the correct feasible zero or the endpoint optimum. The full nonsymmetric uniqueness check uses the strictly positive even minimum eigenvector of the symmetrized matrix: equality in the Rayleigh quotient would require a nonzero diagonal reflection difference to annihilate that vector. The two parity blocks differ by diag(0,2), verifying the extreme eigenvalues and condition number. At t=q the factorizable first term rises strictly on 0<q<1/2 while the other decreases, giving the unique crossing and including equality in the endpoint regime. The ratio of derivative terms strictly decreases in m at fixed t, so the interior root increases with budget and tends to 1/2. At fixed q<1/2 the large-μ boundary difference multiplied by μ tends to a negative value; the small-μ limit of its first term is >1, forcing q_c→0 and q_c/(μ+q_c)→1/[√2(2+√2)]. This gives the two stated threshold asymptotics. Own bisection gave B_c(1)≈0.669854112320272, correcting the last quoted digits, and κ_*(1,1)≈3.681873906750853. Inspected but did not execute CHECKER.py; the finite tests are not the universality proof.

## originality

PASS

The bounded evidence supports the narrow four-path global activation classification, not general condition-number optimization, exact diagonal preconditioning, or the first threshold in any graph design problem. The generic convex framework covers the feasible family, but the reviewed prior statements do not give its explicit optimizer or threshold; bounds on full-text access remain explicit.

## value

PASS

The path is a natural small diffusion network with distinct endpoint and interior costs in spectral effect even when prices are equal. The result determines exactly when a free budget should concentrate only at endpoints, and proves strict global uniqueness against asymmetric candidates, not just a restricted or numerical design. It quantifies the resulting contrast and both asymptotic thresholds and is distinct from routine graph eigenvalue evaluation or a generic optimizer call.

The dated certificate retains the supplied scientific assessment, sources and limitations.
