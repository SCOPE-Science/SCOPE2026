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

For the specified scalar lookahead update, zero/full curvature, 1/L step, equal nonzero starting iterates, and iid draws, the first success produces state (0,a), and g>=1 misses multiply its nonzero predecessor by -c_g, where c_g=beta(1-beta^g)/(1-beta). Thus the first adjacent successes, which occur almost surely, give exactly the first permanently zero state; the two-state waiting-time equations give (1+p)/p^2. The squared renewal kernel at a gap of length g+1 is p q^g c_g^2, and accounting for the first success and its trailing misses gives H=1/[(1-qz)(1-K(z))]. Independently, the moment recursion for (E x_n^2,E x_n x_{n-1},E x_{n-1}^2) has rows (q(1+beta)^2,-2q beta(1+beta),q beta^2), (q(1+beta),-q beta,0), (1,0,0); its resolvent agrees with H. K starts at zero and diverges at 1/q, with strictly positive coefficients at every degree >=2, so its crossing of 1 is simple and unique on the convergence circle of H. The residue yields the stated positive prefactor, and K(1)-1 has the sign of q beta(1+2 beta)-1, also giving the exact critical limit. An independent bounded path/GF comparison obtained 27 exact equalities for horizons 0–8 at beta=3/4 and p=1/2, 7/15, 1/4. The frozen script was not run; this finite replay is not the pole proof.

## originality

PASS

Best-of-knowledge pass for this exact Nesterov extinction and second-moment law, not for pathwise extinction with moment growth as a general phenomenon. The closest indexed theorem has the same nilpotent success map and a closely analogous gap calculation, but requires a unipotent miss map and gives two-sided norm bounds, not this coordinate generating function and simple-pole equivalent. Existing stochastic-Nesterov and lifted moment results do not establish the complete bound claim.

## value

PASS

This is a concrete counterexample to inferring mean-square convergence from exact almost-sure termination for an interpolating stochastic lookahead optimizer. The transition curve, critical positive limit and exact rate answer quantitative questions for a natural scalar quadratic test case; they are not just another example of moment growth. It does not imply a general optimizer theorem or assume that both individual component objectives are strongly convex.

The dated certificate retains the supplied scientific assessment, sources and limitations.
