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

For b>=3 the successive 1-marker positions a_b(k)=(b-1)sum_j eps_j(k)b^j have gap g_t=(b-2)b^t+1 where t=nu_2(k+1). Adjacent external gaps at a marker have different valuations, so a palindrome with odd marker count cannot have >=3 ones; all one-marker factors are 0^h10^h, 0<=h<=b-2. For even marker count a central pair with gap g_t has a unique symmetric block of 2^(t+1) markers, a translate of W_(b,t+1), and exterior gaps unequal beyond symmetric zero extension: resulting maximal palindrome T_(b,t). Therefore all palindromes with >=2 ones are its centered factors, with length L_t..U_t and parity b. Distinct t have distinct central gaps and no triple overlap; exact formula P_b(n)<=3 and infinitely many sharp overlap lengths follow. Independent direct palindrome-set enumeration verified bases b=3..6 and n<=64; infinite proof is the valuation/symmetry argument.

## originality

PASS

The published Nov 2 finite *ternary* Cantor-word theorem gives P_k(n) at substitution levels b=3 and richness but not general integer b nor maximal palindromic language of the infinite generalized Cantor word. The all-b formula includes even/odd base parity changes and scale-dependent gap structure, so it is not established by merely applying the ternary result. Earlier Cantor papers study k-Abelian/permutation factor complexity; no equivalent universal b>=3 palindromic classification was found in targeted searches. Best of knowledge only.

## value

PASS

A complete language classification and sharp uniform palindromic-complexity ceiling for a standard nonprimitive uniform-morphism family, covering every integer base and all factor lengths, is a natural combinatorial invariant. Explicit globally maximal families and parity/scale intervals are mathematically usable beyond finite sample computations; the base-three antecedent is credited rather than claimed new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
