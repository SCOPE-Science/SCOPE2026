---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

With the identically distributed independent continuous priorities specified in scope, the restriction of the random order to the current feasible set is uniform: a path sharing an occupied vertex can never regain eligibility, and each currently eligible path must be later than the last acceptance. Counting triples gives (X−1)/(S−2) for a step with ΔD=−1, and hence the stated drift and variance. The exact gamma recurrence gives conditional mean preservation of h(S)D at every accepted step with S>3; the cutoff avoids h(0). Its centered maximal fluctuation is O_P(N^(1/6)) by the O(N^(1/3)) sum of variance bounds. Off balance this is negligible against the deterministic N^(2/3) initial term. At early absorption above r_N≈√N, h(S)S≥h(r_N)r_N (the ratio between successive permitted levels s and s−3 is s/(s−2)>1). This barrier is of order N^(1/3) and early absorption is negligible in the critical window. The uncorrected quadratic variation divided by 3^(2/3)N^(1/3) tends to one by a progression Riemann sum. The imbalance correction is bounded in expectation by C N^(1/3) times the sum of s^(−2) above the cutoff; replacing absent steps by zero affects convergence in probability only on the negligible early-absorption event. The normalized maximal jump tends to zero, giving the martingale CLT. The remaining variance O(r_N^(1/3)) is negligible. Bounded remainders would give bounded stopped martingale, inconsistent with a positive limiting probability because the normalized Gaussian has no atom at zero. Thus |M_term|=h(U_N)U_N with high probability and gamma asymptotics give the 3/2 power of the absolute shifted Gaussian, with no missing factor of three. Boundedness gives the macroscopic expectation limit. The two path types with counts m and 4m indeed exactly pack K_(9m,6m), and δ=1/5. Replay: RESULT.md lines 31–139. Read trimer_checks.py and VERIFICATION.md without execution; the small distributions and seeded simulations are not the limiting proof.

## originality

FAIL

An independently indexed Finding states both terminal laws on the same complete bipartite path adsorption chain with the same imbalance quantifiers. Its equal-rate exponential priority representation and the frozen i.i.d. continuous priority representation give the same finite permutation and stopping law. The additional expectation limit and packing illustration are immediate once the macroscopic law is known. There is no substantive uncovered remainder in the frozen claim. This is demonstrated coverage in a distinct record, not a claim about which record was derived first or about priority based on catalogue dates.

## value

PASS

The underlying theorem quantifies jamming for a natural dense adsorption process and identifies a non-Gaussian scale in a meaningful imbalance window. The example shows why packing feasibility alone is not a kinetic prediction. Those mathematical and modeling merits do not undo the exact indexed overlap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
