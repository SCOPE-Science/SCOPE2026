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

With p=j+k and q=j−k the lattice imposes matching parity. The two center phases mod 1 are independent Haar phases. Below the half-phase, each interval has 2n integers plus an independent extra with probability 2s; above it, each has 2n+2 minus an independent deficiency with probability 2(1−s). Translation by (1/2,1/2) modulo the original lattice interchanges the same- and opposite-parity cases without changing the extra/deficiency indicators. This yields both mass functions, including the endpoints (a point mass at s=0, two equiprobable counts at s=1/2). Tilings give the exact area mean. With interval sizes M_i=2n+floor(2s)+H_i and parity imbalances e_i in {0,±1}, the count is (M_1 M_2+e_1 e_2)/2; centering and dividing by R leaves H_1+H_2−2{2s} plus a uniformly O(1/n) term. The claimed distribution and variance limits follow, including degeneracy. The submitted checker uses the parity transform and finite grid tolerances; it does not verify a variance identity, despite the wording in RESULT.md. The separate raw lattice-count replay at /workspace/branches/6294677e-a367-4c59-b483-104ad5e5cdec/four_atom_replay.py checked representative supports and rational mean/normalization identities, not the all-phase probabilities; the latter are analytic.

## originality

FAIL

The table is not expressly printed in the inspected prior work, but it is mechanically implied by the fixed-angle line-count formulas in Holgate (1990), pp. 484–485. This is not an inference from the variance of the total alone. Holgate gives the law of the number M of intersected lines (parameter w/u), the two-valued count per line (parameter l/d), the pair-offset construction and the covariance c(x,y) of the two interval counts conditional on the line geometry. At 45 degrees the line offsets alternate by half a lattice spacing: consecutive equal-parity lines are identical for counting, so only two Bernoulli indicators H and G remain. Substituting w/u=2R and l/d=R gives M in {floor(2R),floor(2R)+1}, and the per-line indicators both have mean s. Substituting y=1/2 in the interval-count formula, or using its two half-shifted intervals directly, gives Pr(H=G=1)=max(0,2s−1). Their means and that probability fix the entire joint law. The count is nM+ceil(M/2)H+floor(M/2)G, with the order of H,G interchangeable; substituting the two M probabilities gives both submitted tables, including the boundary cases. The normalized limit is an immediate consequence of those tables. Thus the overlap is exact by specialization of the published line-level formulas, even though their stated purpose was a variance calculation.

## value

FAIL

A full probability law would indeed be a useful benchmark for fixed-orientation randomized lattice counts, beyond simply quoting a variance. Here the exact four-atom result reduces to the existing rational-slope line formulas with just two alternating offsets, and the fluctuation statement follows directly by scaling the resulting atoms. The frozen claim supplies no substantive mathematical advance beyond that mechanically recoverable special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
