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

The excluded origin is 1. In a nonempty antichain, sorting by distinct increasing first exponents forces strictly decreasing nonnegative second exponents, so the size r is finite. Then a_i>=i and b_i>=r-1-i, and the positive decreasing geometric weights give W_(r-1) as the sharp bound for r>=2, with equality only at the full layer. A singleton weighs at most x<W_1. For z=y/x in (0,1), R_d=x(1+(1-z)z^(d+1)/(1-z^(d+1))) decreases strictly to x<1, establishing existence of the maximum and exactly the stated tie rule. R_1=H(x,y)=(x^2+xy+y^2)/(x+y) increases strictly in each positive argument; along (p^-t,q^-t) it falls from 3/2 to 0, giving the unique crossing. Both arguments are dominated by the (2,3) arguments at every positive t, with at least one strictly smaller for another pair. This proves sharpness and the exact equality cases, not just the finite-grid check. An independent Decimal bisection reproduced 0.46067160387338256928301317344350148...; the monotone exact equation, not bisection or a finite simulation, establishes the boundary.

## originality

FAIL

The closed-form specialization is not stated verbatim in the closest paper. Nevertheless, Banks–Martin's published equation (7) and its same-object decomposition mechanically give the exact optimal layer and equality result for two primes at every t>0. The stated Theorem 6 has t>1; the implication here uses the algebraic identity in the proof, not an extension of that theorem by fiat. After the decomposition, the rank rule and sharp uniform exponent follow by evaluating and comparing the two-variable geometric layer sums. This finding is covered by that concrete implication, not rejected because an unrelated weighted-poset paper was inaccessible.

## value

FAIL

The phase boundary is a natural numerical application, but the full two-prime optimum and equality cases are mechanically obtained from a published same-domain decomposition. Selecting a rank via geometric ratios and solving the first-two-rank equality at the dominating smallest prime pair do not add an independently useful unknown exact fact under the review standard. The short coordinatewise proof is useful exposition, but does not change what the frozen theorem supplies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
