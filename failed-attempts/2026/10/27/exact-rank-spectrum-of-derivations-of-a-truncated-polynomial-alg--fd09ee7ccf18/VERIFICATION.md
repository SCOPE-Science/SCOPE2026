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

In RESULT.md, admissible f=D(x) are exactly those with m x^(m−1) f=0: the rule f times formal differentiation descends precisely under this condition. For a nonzero f of valuation s, D(x^i)=i x^(i−1)f has leading degree s+i−1 for 1≤i≤m−s with p not dividing i. These nonzero columns have distinct leading degrees and hence are independent; all other columns vanish. The extra endpoint i=m when s=0 contributes nothing because p divides m in that case. The leading coefficient has q−1 choices and the m−s−1 trailing coefficients have q choices each. This proves the polynomial over every F_q and clarifies that the coefficient for t counts the stratum of valuation m−t, not the total coefficient of a repeated rank. The supplied verify_derivation_rank.py was read, not run; its scope is prime fields and the algebraic argument does not rely on those runs.

## originality

PASS

No earlier statement or stronger enumeration covering the complete unrestricted all-m rank histogram was verified. The standard description of derivations is not claimed to be new; the explicit histogram is an elementary refinement. This limited finding on coverage is not a finding of substantive value or a certification of priority.

## value

FAIL

The object is natural, but the entire invariant is obtained by a routine leading-term calculation on the monomial columns of f times differentiation and the elementary count of coefficient strings in a valuation stratum. The divisibility boundary and adjacent rank collisions are immediate from the same calculation. Reinterpreting rank as the codimension of the kernel adds no mathematical problem, and the record supplies no concrete use or gap that makes this routine deduction a substantive contribution. The related square-zero and canonical-type problems involve additional constraints not solved here. No genuinely valuable surviving repair was identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
