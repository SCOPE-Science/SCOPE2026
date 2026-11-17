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

Rank-of-apparition and Lucas valuation theorem give v_p(U_n)=e+v_p(n/r) on multiples of r and zero otherwise at odd p, including ramification where r=p and e=1. Möbius transform is supported at r p^j with coefficients p^e-1 and p^(e+j-1)(p-1), nonnegative. Dold denominators yield minimal repair r/gcd(r,p-1). Split ranks divide p-1; inert ranks divide p+1 but exceed 2; ramified ranks p. Binary valuations differ by parity of P, yielding repairs 2 versus 3. Discriminant P^2+4 is nonsquare for P>=2, so Chebotarev/Dirichlet gives density 1/2. Independent direct recurrence and Möbius enumeration tested 77 (P,p) combinations for indices 1..120, corroborative only.

## originality

PASS

The complete even-parameter P>=2 subfamily was already published 2026-10-12, including the same odd-prime repair, binary repair 2, and prime density. This subset is explicitly credited rather than counted as novel. The surviving contribution is the uniform extension to every odd P>=3, including the distinct binary Möbius tower and optimal repair 3, together with a parity-unified classification. Classical Fibonacci P=1 and valuation formulas are earlier ingredients, not asserted new. No covering odd-P theorem found in targeted Resultary and primary-source inspection; best-of-knowledge.

## value

PASS

Extending the complete local dynamic realizability spectrum from only even P to all odd P, including the precise dyadic exception and optimal repair, closes a natural parity gap in a classical Lucas recurrence family. It gives exact all-prime orbit-count positivity and splitting-density results, not simply recomputation of one small index.

The dated certificate retains the supplied scientific assessment, sources and limitations.
