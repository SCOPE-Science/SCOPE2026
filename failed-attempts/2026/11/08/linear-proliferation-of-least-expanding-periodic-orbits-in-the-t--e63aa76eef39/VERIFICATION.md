---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For each non-all-L period-n symbolic word, the Jacobian is a signed monomial matrix; right visit count t determines coordinate permutation. For t not a multiple of three the single three-cycle forces all eigenvalue moduli 2^{n/3}; for t=3q, diagonal exponents are q+c_0,q+c_1,q+c_2 for nonnegative left-block counts. For n>=4, the minimum normalized modulus 2^{1/n} occurs exactly when t=3 and a cyclic left-gap is zero. Marking a right visit counts n/3[C(n-1,2)-C(n-4,2)]=n(n-3) words; any nontrivial repeated word with three R would have all three positive equal gaps and fail the condition. Hence n-3 primitive n-cycles. Independent enumeration of 3-R words for n=4,...,12 confirms counts 4,10,18,28,40,54,70,88,108; all-n conclusion rests on proof, not finite data.

## originality

FAIL

FAIL. The complete all-dimensional prime-divisor onset and weakest-multiplier census published November 2 includes dimension M=3 and prime p=3, yielding exactly the minimum raw eigenvalue modulus 2, normalized 2^{1/n}, exact extremal number E_3(n)=C(n,3)-C(n-3,3)-C(n-4,2)=n(n-3), with the same three-right/zero-gap characterization. It even counts every weakest-multiplier class and supplies primitive witnesses.

## value

FAIL

FAIL. There is no independent extremal fact here: the minimum, equality words, their count, primitivity, and cycle count follow from the stronger published all-M and all-n histogram. The special calculation is mathematically correct but a dominated specialization, not a motivated new invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
