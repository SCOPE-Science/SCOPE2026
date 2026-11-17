---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For all integer n, C_t(d) is equivalent by binomial finite differences to rational prime-adic congruence of Q_{d,t,c}(-1) for every c<d. Root-of-unity filtering yields Q=(-1)^c/c! times H with H=sum_{j>=1} (-d)^{jt} e_{c-jt}(1,...,c), so all infinite n quantifiers reduce exactly to finite integer valuation conditions at c=0..d-1. When t>=d, all sums vanish. Exhausting 2<=d<=36, 1<=t<=d yields upward closed valid order sets for d<=35 and at d=36 valid {15} union {17,18,...}; explicit c=32,t=16 rational witness is 196839814746004676662011581276685234/1506938033147421875 with v2=1<2 required, whereas all c<36 pass at t15. d1 trivial. This is a complete finite minimality proof not a heuristic extrapolation.

## originality

PASS

The earlier finite-test lemma supplies a method, not the complete finite computation or minimality. The derived exhaustive valuations, explicit C15 positive certificate and C16 negative witness are additional precise arithmetic results; a classification outside exceptional moduli cannot decide this exceptional mixed-prime modulus. Miska classifies fixed small orders (particularly 1<=t<=5) and moduli with prime factors larger than t. At d=36,t=15/16, both prime factors 2 and 3 are <=t and outside the stated large-prime theorem, so that criterion does not imply the claimed adjacent-order failure or first modulus.

## value

PASS

The least modulus at which increasing the cyclotomic root filter order destroys a universal binomial congruence is a natural boundary and counterexample to an intuitive monotonicity principle for Miska congruences. Sharp d=36 threshold and exact t spectrum provide a reusable arithmetic benchmark for p-adic congruence structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
