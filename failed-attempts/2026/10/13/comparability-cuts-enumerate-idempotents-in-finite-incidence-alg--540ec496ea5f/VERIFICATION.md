---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Let P be a nonempty finite poset, q any prime power, J the zero-diagonal radical of its incidence algebra and e_S the diagonal indicator of S. The published explicit conjugator of Khripchenko–Novikov Theorem 3 belongs to 1+J and acts transitively on every diagonal fiber. The stabilizer is 1+C_J(e_S); its codimension equals the number of strict comparable cross-cut pairs c_P(S). Orbit-stabilizer gives exactly q^{c_P(S)}, even when q is even. The sum over S follows. For chains, c_P(S)=|S|(n-|S|); antichains yield 2^n; degree/leading coefficient are the maximum-cut data. Independently enumerated all transitive naturally ordered posets of size ≤4 at q=2 and ≤3 at q=3, comparing literal convolution idempotency with the cut formula (60 cases). Finite checks corroborate but do not prove the universal statement.

## originality

FAIL

FAIL: A directly dominating, previously uncredited full-text source was found: Ivan and Michael Gargate, arXiv:2009.04243 (2020), Theorem 1.1 and §§3–4. For odd q, its necessary-and-sufficient upper-triangular (k+1)-potent entry conditions with k=1 state that every off-diagonal entry between unequal diagonal labels 0 and 1 is free, while equal-label entries are determined. Restricting to incidence algebras zeroes incomparable entries; transitivity makes those constraints compatible. For each poset labeling S, exactly c_P(S) allowed entries are free, giving q^{c_P(S)} and the claimed sum directly. Section 4 explicitly treats counts of (k+1)-potents in finite incidence algebras. This is strong prior coverage regardless of the absence of the phrase comparability-cut polynomial. The excluded characteristic-two extension follows immediately from the 2008 conjugacy theorem; MaxCut degree and coefficients follow tautologically from the enumerator. The claim is mathematically true, but the original all-poset finite-field counting contribution is covered.

## value

FAIL

FAIL: The exact arbitrary-poset idempotent count over odd finite fields is a direct k=1 specialization of prior classification and finite-poset counting. Calling the exponent the comparability cut, and reading its degree/max-coefficient as MaxCut, are immediate relabelings of the prior free-coordinate census. The characteristic-two extension uses the same elementary conjugacy/orbit count and supplies no separately motivated new structural boundary or difficulty. The submitted package supplies no substantive uncaptured contribution beyond this covered result; correctness and a new proof do not alone make it valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
