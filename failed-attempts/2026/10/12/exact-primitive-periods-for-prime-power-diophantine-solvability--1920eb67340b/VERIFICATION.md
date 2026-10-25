---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Reconstructed the Gamma/inverse parity equivalence with both integer solution formulas and exclusivity. For m=p^e odd and E the even reduced residues, the exact sum S=(p-1)(p^(2e-1)+1)/4 satisfies 4S congruent p-1 modulo p^e and is a unit. An output period t induces a multiplicative E-stabilizer b^{-t}; summing forces b^{-t}=1, so N=phi(m) divides t; N itself is a period. The unique order-two unit -1 swaps parity, proving half-period anti-symmetry and balance. Independent exact checks covered 240 primitive-root cases for prime powers <=500 plus spotchecks of both Diophantine alternatives. Finite computations corroborate but are not an infinite proof.

## originality

FAIL

Strong prior coverage was found under the equivalent terminology of modular reductions of maximal-length primitive sequences: Zhu and Qi (Math. Comp. 2008) establish injectivity of reduction modulo M for odd prime-power recurrences and M not a p-power. For M=2, the period of the reduced degree-one primitive sequence cannot be shorter than the original period, giving this exact-period claim once the conventional degree-one instance is admitted. Wang–Hu 2015, Theorem 8, fully restates and reproves the dominating modular compression principle. A degree-one scope caveat remains because that exposition globally assumes n>1, and complete 2008 text could not be accessed; this is not represented as a claim of having read the original article. Even independently, classical base-2 and prime cases are established prior art. The submitted full-period assertion does not survive as an independently new theorem on the available published-coverage evidence.

## value

FAIL

The original binary word is a natural exact-period invariant, and the even-unit moment offers a clean elementary certificate. But the asserted full-period conclusion is subsumed by the broad pre-existing modular-compression injectivity result, while the half-period complement and zero-one balance follow immediately from the unique involution -1 in the cyclic unit group. Under the final submitted claim there is no separately motivated unknown invariant, new classification, or boundary established beyond the prior theorem. Independent correctness and reproducibility do not alone make a covered specialization a valuable new mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
