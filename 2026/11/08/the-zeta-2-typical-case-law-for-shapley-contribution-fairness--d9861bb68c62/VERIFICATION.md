---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The theorem uses exactly one divisible good and independent productivities of the form \(U_i^s\), where the \(U_i\) are uniform on \((0,1)\) and \(s>0\). The factor is the smallest multiplicative weakening of each agent's Shapley welfare-game benchmark that is jointly feasible with no transfers.

Run `python3 verify.py` with Python 3 and `mpmath` to reproduce the finite checks. A successful run ends with `PASS 1137 checks`; it checks the pairwise representation against the original Shapley formula and permutation enumeration, exact second-order harmonic and integer-power mean identities, strict power monotonicity, and seeded simulation agreement with independently calculated finite-population means. The complete proof of almost-sure and mean convergence is in `RESULT.md`; no finite run can establish an infinite-population assertion. The proof explicitly treats the boundary ranks and uses a summable exceptional-event estimate. All comparisons concern this model only; prior publication priority has not been independently certified.
