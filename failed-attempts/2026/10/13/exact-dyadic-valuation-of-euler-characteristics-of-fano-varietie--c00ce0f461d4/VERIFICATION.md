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

For the smooth complex cubic d-fold the normal sequence gives the top Chern coefficient of (1+H)^(d+2)/(1+3H), integrated with degree 3. Expanding, or using the coefficient recurrence T_(d+1)=−2T_d+d+2 with T_0=1, gives X=χ(Y_d)=((−2)^(d+2)+3d+5)/3. The precise smooth specialization of Galkin–Shinder Corollary 5.2(1) gives χ(F_d)=X(X−3)/2. X is odd for even d and even for odd d. After multiplying the even factor by 3, its linear term is respectively 3d−4 or 3d+5, strictly between 0 and 2^(d+2) (check d=2 and d=3 and increase d by two). Hence its valuation is smaller than d+2 and is unchanged by adding the signed power of two. The factor 1/2 subtracts one. Inverting 3 modulo 2^(t+2) gives one class of the required parity on each branch, including classes 2 and 3 modulo 4 at t=0. The independent replay `python3 /workspace/checks/finite.py 5` uses the Chern recurrence, verifies the sample values and checks the valuation through d=5000; the valuation argument, not this range, establishes the infinite claim. The frozen checker compares a direct Chern sum only through d=200 and tests valuations through d=5000, as clarified in VERIFICATION.md.

## originality

FAIL

The valuation expression was not found verbatim. It is a mechanical arithmetic specialization of the prior exact Euler formula and the standard hypersurface Euler formula: split the two factors of X(X−3) by parity, discard the odd one and the higher-valuation term in the even one, then invert 3 for residue classes. No new geometric or number-theoretic input is needed. This is coverage by direct implication, not evidence that the same congruences appeared in print.

## value

FAIL

The smooth cubic Fano Euler number is a natural invariant and the residue statement is correct, but it recasts an already explicit invariant by standard parity, unequal valuations, and a linear congruence. The record supplies no independently needed dyadic obstruction or further structural information beyond that mechanically obtained arithmetic; it does not meet the requirement for a distinct worthwhile exact fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
