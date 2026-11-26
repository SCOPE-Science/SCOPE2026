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

The uniform fixed-weight source corresponds bijectively to a uniform weak composition of N into m=k+1 gaps. Only positive gaps give coupons; decreasing one positive gap distinguishes its output, and its probability is G_i/N. Tail-sum inclusion-exclusion and counting positive selected coordinates with sum u give the exact A_{m,s} formula, including N<m and the one-marker formula. The small case m=2,N=3 averages the four means 1, 7/2, 7/2, 1 to 9/4. For the limiting law, the uniform grid converges to the uniform simplex and zero coordinates have probability O_m(1/N). Dirichlet integration makes the t-draw count vectors equally likely, so the ratio of positive to weak compositions gives the stated integer-time tail; its first-order coefficient is m(m-1). For the finite mean, coefficient extraction from -log(1-z)/(1-z)^(m-1) gives N A_{m,1} = (m-1)N/(N+m-1) times (H_{N+m-2}-H_{m-2}), which fixes the harmonic constant. For 2<=s<m, the mass at total u with selected coordinates positive is bounded by C_m u^(s-1)/N^s; hence the truncated reciprocal sum for u<=epsilon N is O_m(epsilon^(s-1)). The inverse Beta moment is therefore the correct limit (m-1)/(s-1), and s=m directly gives 1. Integrating [1-mx-(1-x)^m]/x^2 gives the alternating sum m-1-m H_{m-1}. Thus the finite mean expansion is proved independently of distributional convergence. The frozen verification notes and checker were inspected, not executed; finite checks do not establish this expansion.

## originality

PASS

This pass credits the deletion-source finite-size law, particularly the explicit logarithmic mean and constant for every fixed marker count. The limiting collector law, including its heavy-tail coefficient and infinite mean, is already covered by a more general indexed Pólya-urn result and is not an independent originality credit. The frozen record makes its contribution jointly with the deletion-source finite-size law and does not claim the mixture identity as new.

## value

PASS

The precise finite mean answers a repeated-read cost question that the limit law cannot answer: rare sources with a very small positive gap dominate the mean although a typical source has a tight cover time. The leading logarithm and constant quantify that discrepancy for each fixed marker count and keep zero gaps correctly out of the support. The useful part is the finite mean analysis, not renaming the known Pólya collector.

The dated certificate retains the supplied scientific assessment, sources and limitations.
