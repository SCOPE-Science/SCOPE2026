---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Independently checked companion matrix A^4=I+2B and parity pattern 0011 of T_n. For r>=3, A^(2^r)=I+2^(r-1)B_r, giving four-periodic parity for both T_j and increment coefficients; binomial doubling remainder is divisible by 2^r for odd e and 2^(r+1) for even e. Base eight terms establish the two exact congruences and subsequent induction covers every n>=0, e>=3 and r>=3. Direct windows r=1,2 give gcd valuation 0,1. Separate modular recurrence independently checked 8736 windows with e in a bounded range: finite corroboration, not infinite proof.

## originality

PASS

PASS best-of-knowledge: The prime, exponent and recurrence order differ; no known cited general recurrence theorem specializes to this exact even/odd exponent dyadic-window law. No stronger prior theorem found with the exact odd/even all-exponent power-window conclusion; the matrix induction is a genuine additional argument.

## value

PASS

A uniform sharp two-adic gcd threshold for all nonlinear powers of a natural third-order recurrence provides a nontrivial divisibility classification with a genuine parity-of-exponent phase split, not a routine substitution from order-two Fibonacci identities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
