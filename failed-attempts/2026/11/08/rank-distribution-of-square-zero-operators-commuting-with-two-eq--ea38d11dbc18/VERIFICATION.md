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

Identify Cent(J_m⊕J_m)=M_2(F_q[t]/t^m), preserving base-field rank as image length. Primitive square-zero matrices are GL2(chain ring) conjugate to E12 via Nakayama, count (q²-1)q^{2ell-2}. Valuation layers a<ceil(m/2) each have (q²-1)q^{2m-2} members; determinant uniformity and Smith exponents yield every rank coefficient, with automatic-square-zero high-valuation cone giving P_ell terms. Summing gives h(q²-1)q^{2m-2}+q^{4floor(m/2)} and maximal-rank count (q²-1)q^{2m-3}(q+floor(m/2)(q-1)). Field q=2,3,4 and odd m boundaries treated; all finite fields. Independently compared each coefficient with the earlier chain-ring full rank polynomial for 44 (q,m) choices, q=2,3,4,5 and m=1..11; all match. The all-m proof is the valuation and Smith argument, not these finite examples.

## originality

FAIL

An actual published November 2, 2026 Resultary theorem for all finite commutative chain rings gives the complete 2x2 square-zero image-length spectrum; it explicitly states that for R=F_q[t]/t^m the formula counts precisely square-zero matrices commuting with J_m⊕J_m, classified by Jordan rank. Its valuation-layer, maximal rank, and total formula are exactly the submitted ones. The current result is a strict specialization to equal-characteristic truncated polynomials and m>=3, not a distinct new theorem.

## value

PASS

A complete labeled square-zero rank/Jordan-type census in a fixed nontrivial centralizer is a natural structural invariant in finite-field matrix representation theory. The all-rank formula and maximal-rank distribution are substantive mathematics but are already established in a more general source.

The dated certificate retains the supplied scientific assessment, sources and limitations.
