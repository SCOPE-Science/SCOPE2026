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

I reconstructed f=(xy+1/2)^2+x(1-x+a x²), the actual bounded branch interval r±=(1±sqrt(1−4a))/(2a), and vertical height 2sqrt((x−1−ax²)/x). Substitution z=ax and a standard sine-square elliptic reduction yields precisely 4β^(3/2)[(2−m)E−2(1−m)K]/(3a), with parameter m not elliptic modulus. For increasing a the positive heights and admissible interval strictly shrink, proving nesting. DLMF singular expansions K~log(4/sqrt(1−m)), E=1+(1−m)(log(4/sqrt(1−m))−1/2)/2+... produce 4/(3a)+log(a)−1−log16+O(a|log a|); with δ=1/4−a the exact shear-normalized U,V interior approaches U²+V²≤1, whose Jacobian gives 4sqrt(2)πδ. Independently expanded the actual polynomial cofactor to zero and integrated five nontrivial a-values against the elliptic expression at >40-digit precision. The known 2004 existence theorem is explicitly assumed; a regular algebraic oval is not proven to be isolated from just a cofactor check.

## originality

PASS

Best-of-knowledge original quantitative geometry of a known 2004 quartic algebraic cycle: existence and uniqueness of the algebraic oval are prior, but the exact Euclidean area map, sharp logarithmic correction and collapse coordinates were not obtained from inspected primary accounts. Unavailable original 2004 full text remains a specific priority risk.

## value

PASS

The enclosed area and its normalized degeneration are natural geometric invariants of a canonical algebraic limit cycle. The strict monotone area coordinate, genuine logarithmic finite correction, and two different limiting shapes supply more than a routine substitution or re-labeling. This exact quantitative endpoint information could be used when comparing bifurcating algebraic cycles or area-based measures in the classical family; it is not already mechanically supplied by the existence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
