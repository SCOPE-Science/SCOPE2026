---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

All posterior normalizations are positive. Relative to the common base measure, the ratio for indices i<j is a positive constant times (u/(1-u))^(j-i) on (0,1); the atom at 0 can only add to the lower-index posterior and the atom at 1 can only add to the higher-index posterior. The one crossing gives both stochastic order and TV equal to the maximum CDF gap. The endpoint CDF gap dominates every posterior gap; expanding a pair of mixed rows as a convex combination of posterior differences bounds its TV by the endpoint TV, which the rows at 0 and 1 attain. Equality in the endpoint densities gives the stated theta, and an atom at theta contributes zero. Positive overlap on the interior gives TV<1, including the possible zero case. Regularity of finite Borel measures gives continuous [0,1]-valued approximations of the maximizing indicator in the two endpoint integrals, proving the oscillation supremum. The symmetric joint kernel gives stationarity; Jordan decomposition gives the TV bound, sharp for the two endpoint point masses in one step. The uniform integral is 1-2^(-n).

## originality

PASS

Limited to literal theorem scope: the arbitrary finite-Borel-measure statement, including singular and atomic bases, is broader than the exact Jacobi theorem located in the prior record. The Jacobi and uniform formulas themselves are covered. No inspected prior general theorem states the evaluated endpoint diameter for this whole measure class; the ease of transferring the earlier proof is assessed separately under value.

## value

FAIL

The retained difference from the exact Jacobi result is a routine extension of its proof, not a new sharp estimate requiring any new idea for singular measures. In the old proof replace the Lebesgue densities of posterior beta laws by the posterior Radon–Nikodym densities b_(n,k)/Z_k relative to the common base measure. In the likelihood ratio the base cancels; the same odds powers give the same two-by-two minor signs, CDF ordering, and endpoint sandwich, without beta integrals. The polynomial minors extend to u=0 and u=1 by continuity independent of whether the base charges those points; regularity handles the continuous test functions. The new threshold only substitutes the generalized normalizers. Neither the uniform formula nor a new singular-base asymptotic, extremal phenomenon, or contraction calculation remains as a distinct substantive result. The class of arbitrary bases is natural, but the exact invariant transfers mechanically from the closest proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
