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

For centered X the explained variance is exactly sum_y M_y^2/P_y with all P_y>0 for contrast below one. The Walsh expansions follow from the independent common-contrast likelihood; sign reversal gives evenness. To justify the uniform Lipschitz order-six remainder, choose a complex contrast disk where the absolute sum of nonconstant denominator terms is below 1/2 for every threshold vector. Step-function moments are uniformly Lipschitz from their changing intervals; on the disk both the rational expression and its threshold differences are bounded, the latter by C_k times threshold distance. Cauchy coefficient bounds and a geometric tail give the stated Lipschitz estimate on a smaller disk. At fourth order the terms are E[L2^2+2L1 L3-2L1 L2 Q1+L1^2(Q1^2-Q2)] with L_j the numerator and Q_j the denominator Walsh degree j; E[L1 L3]=0. At t_i=1/2+d_i, b_ij=O(||d||^2), a_i=-2d_i and a_ij=1-2|d_i-d_j|, so only -2 sum c_i c_j a_ij generates the linear +sum|d_i-d_j|/4. The order-two loss is -sum d_i^2/2+sum d_i^4. Compact uniform order-two convergence brings every optimizer to the repeated midpoint; the quadratic loss and linear difference bound then force O_k(epsilon^2). Sorting reduces the scaled energy to a square around (2i-k-1)/4, with unique sorted maximizer and gain k(k^2-1)/96. Uniform scaled convergence plus comparison to this feasible trial design proves the claim for all global optimizers. The positive scaled spacing implies their eventual distinctness. Independent polynomial-cell calculations checked exact dyadic coefficients through order six in 28 finite designs, k=2..8, with replication and perturbed offsets; replay /workspace/branches/spectral_design_replays.js, thresholdCheck. Frozen CHECKS.txt reports 40 finite inequalities; verify.py was inspected but not executed. Neither finite check proves uniqueness at finite contrast or a growing-budget limit.

## originality

PASS

The strongest checked overlaps are an earlier exact reflected pair and a distinct same-day adaptive two-query result comparing against unrestricted parallel pairs through order four. Neither states nor entails the unrestricted fixed-k>=3 spacing coefficient or sharp replication gain at order six. Related nonadaptive coding and finite-blocklength studies use different admissible questions, regimes or losses. This is an assessment on inspected statements, not an exhaustive priority claim.

## value

PASS

At leading order the globally optimal thresholds are indistinguishable from full replication, so neither first-order weak-channel information nor an exact pair design determines whether spreading helps for arbitrary budgets. The result resolves where every global optimizer goes at the first scale that distinguishes locations, and computes the first positive value advantage with explicit dependence on budget, without imposing symmetry. This is an intrinsic design question, not a routine reparametrization or a numerical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
