---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The full frozen RESULT.md proof expands Walsh quadratic forms in nonzero XOR-character coefficients c_s=2 sum of matrix entries in each matching. Parseval and exact without-replacement finite population sampling give Var(H_k)=(n-k)/(k(n-1)) sum c_s^2; Rademacher quadratic forms give (4/k)sum_{i<j}Aij^2. Cauchy-Schwarz on n/2 edges per XOR matching proves ratio <= n(n-k)/(2(n-1)), with equality iff coefficients are constant on each matching. A=I+epsilon P_s, 0<epsilon<1, gives SPD equality with condition number tending to one. Shared random diagonal signs give expected c_s^2=4 sum_matching Aij^2, hence exact (n-k)/(n-1) factor. Independently evaluated the n=8,k=3 subset distribution to obtain 20/7 sharp ratio and n=8,k=7 boundary 4/7. Matrix must be non-diagonal for ratio; n=2,k=1 equality, k=n Hadamard variance zero. Finite experiments corroborate, not prove, general n.

## originality

PASS

PASS after distinguishing the known shared random-sign variance reduction from the sharp unmodified, uniformly subsampled Hadamard variance envelope. Neither indexed signed-color probing nor the inspected stochastic probing variance formula establishes the exact XOR-matching equality class. Hadamard-specific trace-probing work by Fika–Koukouvinos remains a serious historical-priority uncertainty because its full text was unavailable.

## value

PASS

A sharp worst-case counterexample to the assumption that a deterministic Hadamard frame sampled without signs always reduces Hutchinson trace variance; equality geometry, near-identity SPD witnesses, and exact query-budget reversal make a concrete matrix-estimation design result. Previously known sign randomization is appropriately segregated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
