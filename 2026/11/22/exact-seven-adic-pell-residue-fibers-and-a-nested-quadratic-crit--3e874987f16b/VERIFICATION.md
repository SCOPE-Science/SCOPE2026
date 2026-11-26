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

The initial state (0,1) has least period six mod 7, hence any period is a multiple of six. M^6=I+7A with off-diagonal A_12=10 a unit. The first coordinate of ((I+7A)^(7^j)-I)(0,1) has exact valuation j+1, and M^(6*7^(k-1)) is identity mod 7^k. This proves the least state period and hence the scalar least period. For general h in Z_7, h nonzero, the matrix power difference is 7hA mod 7^(v_7(h)+2), obtained first for integers using the binomial power at 7^v and then by continuity. Since (I+7A)^t is identity mod 7, each normalized difference quotient is its corresponding one-step slope mod 7. Recurrence gives P slopes (3,3,2,0,2,4); for Q on r=3 the slope is (1393-7)/7=198, a unit mod 7. Thus five normalized P branches and the critical Q/7 coordinate are isometric and bijective by unique digit lifting. On the critical branch the norm identity gives P=c sqrt(1+Q^2), choosing the root P=5 mod 7; c=5 mod 49. For w=Q/7, put V(w)=sqrt(2/(1+sqrt(1+49w^2))). The difference V(w)-V(w') is in 49(w-w')Z_7 by rationalizing the differences of the two roots (their sums and the denominators are units), and V=1 mod 7. Hence wV(w) is congruence-preserving with reduced difference quotient 1, an isometric bijection. It gives P=c+49(c/2)u^2. Counting u modulo 7^(k-1) gives seven preimages per square root modulo 7^(k-2), including k=2; the k=1 critical branch contributes one count at residue 5. Root multiplicities follow by the parity of target valuation and the two unit-root lifts; the center has 7^floor((k-2)/2) roots at depth k-2. Regular branches alone cover the four stated balls. Independent recurrence replay through k=6 verified exact first state return, every target count on each branch (generating the predicted critical histogram by direct squaring), and the count at the lifted center; at depth six it obtains 100842 indices, 67228 attained targets and center multiplicity 344. The all-depth proof is analytic, not extrapolated from replay.

## originality

PASS

Least-period lifting and non-completeness are covered by prior literature. The accessible general Carlip–Somer recurrence machinery also gives conditional exact partial counts for irregular subsequences, not merely asymptotic bounds. In the inspected statements it still needs target membership in the appropriate multiplicative orbits and their orders, and its main theorem on outputs divisible by p is not the critical Pell branch (which has unit values). Thus the closed target-by-target square-root law at the explicit center, plus the evaluated four-ball image, is the supported distinct content. Close same-prime Lucas and fourth-power examples do not have the Pell target map.

## value

PASS

Pell is a standard second-order recurrence for which non-completeness at seven was already a concrete arithmetic issue. The result replaces that yes/no fact by a usable exact count at each target and each depth and explains why the image remains four full balls while one nested family has unbounded multiplicity. The coexistence of regular filling and a single quadratic critical branch is a structural distribution result, not just the recovery of the period or an image-density computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
