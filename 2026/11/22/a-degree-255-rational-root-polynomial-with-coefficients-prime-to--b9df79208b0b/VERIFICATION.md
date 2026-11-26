---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The factorization gives exactly the two rational roots and degree 255. Modulo 2, (1+X)^256=1+X^256, and division by 1+X gives 256 unit coefficients for exponent 255. Modulo 5, the digit vectors (2,2,4,0) and (3,3,0,1) give A(X)A(X⁵)B(X²⁵)(1+X¹²⁵), where A has coefficients (1,1,3,3,1,1) and B=(1,1,1,1,1). In H=A(X)A(X⁵), the nonzero residue classes of the exponent modulo 5 each get one nonzero product in the coefficient range. The exponent-zero class has neighbor sums 2,4,1,4,2 and boundary units. Its first six and last six coefficients combine to (3,2,1,1,2,3) modulo 5. Since deg H=30, the spacing-25 shifts never have triple overlaps and their overlaps have exactly these six coefficients. The resulting G has degree 130 and unchanged end blocks, so the spacing-125 shift has the same six overlap coefficients and all coefficients survive. The integer gcd requirement and conditional lower bound follow. Independently calculated every coefficient using the signed binomial-sum formula over ℤ (`python /workspace/review_checks/3.py`): gcd(c,10)=1 for all 256, with residue counts 1:74, 3:102, 7:20, 9:60, agreeing with the frozen output (uploaded code inspected only). No finiteness or extremality claim is proved.

## originality

PASS

Best-of-knowledge pass only for the explicit witness at the pair {2,5} and the resulting lower bound, not for the parity identity or a resolution of the general-pair problem. The motivating publication's abstract is specific about {2,3} for its two-prime theorem. Ranked Resultary matches were compared where germane; the exact self-hit is the frozen claim, not earlier evidence.

## value

PASS

The prime pair is motivated by a coefficient-avoidance degree question, and an explicit degree 255 is meaningful evidence against a small universal bound modeled on the sharp {2,3} case. It solves 256 nonvanishing conditions by a transparent digit and overlap argument and gives a benchmark for future bounds. It is not claimed to settle the existence of a bound or be a record degree.

The dated certificate retains the supplied scientific assessment, sources and limitations.
