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

Oliveira's Theorems 7.1 and 7.2 identify the equal-branch affine map and the row-omission matrix, respectively. For S=XY with X columns (ε,u,−v) and Y rows (1ᵀ,−e₀ᵀ,−eₙ₋₁ᵀ), YX is precisely the frozen N; the constant-through-cubic coefficients of det(I−tS) follow by expansion and Sylvester's identity, also at n=2. Vanishing of the cubic forces B=0 when a=1 and A=0 when b=1. In the former case the linear and quadratic coefficients would force s=0 and eA=0 despite A≥1; in the latter they force s=−1, but having no up-switch and a final down-switch gives s=n−2. With a=b=0 the other two coefficients vanish precisely when s=0 and e=f, since A−B=(f−e)/2 and e≠f would give A+B>0. Cayley–Hamilton on YX yields S⁴=0. In characteristic zero Newton's identities also show that vanishing of all power traces forces nilpotence. At n=2 balance forces unequal last signs, and at n=4 three distinct equal signs preclude balance. For n=2m≥6 choose the common sign and m−3 remaining positions for it. The ratio of twice that binomial to the central binomial tends to 1/4, giving the stated Stirling asymptotic. The unsigned row sum lower bound gives at least (n−1)^k walks per starting vertex in the qualifying cases. The supplied checker was inspected, not run; it constructs the stated M and checks characteristic coefficients, word counts and S⁴ for lengths 2–9. The algebra, not that finite test, proves the result.

## originality

FAIL

The frozen result is correct, but the decisive finite-word cubic is already in a distinct indexed same-day record, 1dd240625b4a, Proof step 1, not merely suggested by its asymptotic headline. Its E,U,V are s,e,f, its coefficient −(E+b) equals bf−s, and its quadratic-in-t and cubic-in-t coefficients AU−BV+Eb and U(Ba−Ab) coincide with the frozen ones using bf=−b and af=a. This broader exact formula specializes to the classification by setting the three coefficients to zero, and counting the balance and three fixed signs is an elementary binomial specialization. This is demonstrable coverage, not a claim of which record was written or posted first, and it is not an inference of exact counts from a weak limit alone.

## value

FAIL

The exact-zero question is natural and the difference from unsigned growth is useful context. As a distinct finding, however, the criterion and count are direct specializations of the already indexed exact signed cubic for the same words: coefficient vanishing and a binomial count give the advertised refinement with no new structural input. The frozen claim gives a useful exposition of that consequence, not a materially independent exact invariant under the review standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
