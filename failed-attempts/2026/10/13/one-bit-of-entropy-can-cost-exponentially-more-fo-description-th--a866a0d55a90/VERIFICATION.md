---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For fixed monadic vocabulary k>=2, the type multiplicity vector of U consists of t=2^k entries n/t and that of B of two entries n/2. Jaakkola–Kuusisto–Vilander Theorems 1 and 8 give 3m_(ell-1)-3 <= C(M) <= min(3m_ell+c_tau,6m_(ell-1)+c_tau) with c_tau=15k2^k. Plugging the vectors gives 3n/t+O_k(1) versus 3n/2+O_k(1). Since for fixed k the leading terms are positive, the ratio tends (3/2)/(3/2^k)=2^(k-1); Shannon entropies of uniform supports of size 2^k and 2 are k and 1. Independently checked coefficients and ratios at k=2,3,6,10. The result is NOT a uniform joint asymptotic with growing k.

## originality

FAIL

The published CSL 2025 paper supplies the exact general inequalities in Theorems 1 and 8 for arbitrary ordered unary-type multiplicities and Section 6 explicitly notes nonmonotonicity between entropy and FO description complexity. The entire claimed leading coefficient pair and factor 2^(k-1) are obtained by direct selection and substitution of the uniform multiplicity profiles. This prior broader theorem logically covers the proposed family without needing to print its ratio verbatim. Hence the scientific originality axis FAILS.

## value

FAIL

Despite the potentially useful pedagogical example, the actual mathematical computation is a one-line specialization of two published sharp-leading-order bounds plus Shannon entropy of two uniform distributions. No novel structural theorem, new bound, independently motivated unknown invariant, or difficult boundary is proved. The phrase exponential in k does not alter that k is held fixed in the n-limit; the packaged item is mechanically implied by prior work and is not independently valuable as new mathematical research.

The dated certificate retains the supplied scientific assessment, sources and limitations.
