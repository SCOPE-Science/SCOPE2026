---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS: The Walsh degree-four endpoint projection norm is exactly E|K_{4,n}| by finite group convolution. The coordinate recursion K_{4,n+1}=K_{4,n}+epsilon K_{3,n} gives nonnegative increment E(|K3|-|K4|)_+ and, by sign-change identity, a weighted sum over adjacent parity nodes of the quartic P_N(s). Its explicit four simple roots are separated by more than the node step two, so exactly the claimed pair of positive-root intervals contribute, with exact binomial factors. Zero increment iff all four roots lie on the parity lattice. Integrality of both squared roots forces D_N^2=6(2N-3)^2+10; the two Pell seed orbits under multiplying by 5+2sqrt(6) grow geometrically, proving O(log X) possible plateaus. The n=7 plateau and finite range cutoff are separate: only n<=10^100 is computationally excluded, not all n. Independent new exact-integer derivation checked polynomial, increment and plateau arithmetic on N=5..60.

## originality

PASS

PASS best of knowledge: the norm expectation formula and general Krawtchouk zeros are prior; the new exact consecutive-dimension increment, parity-root iff plateau and two Pell-sparse possible families were not implied by full inspected general norm/asymptotic material or by the separate cubic plateau classification.

## value

PASS

PASS: The degree-four projection norm is an established natural operator invariant. Exact equality conditions and logarithmically sparse possible plateaus illuminate a genuine arithmetic boundary for monotonicity, distinguished sharply from cubic infinitely frequent plateaus and from an unfinished Pell census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
