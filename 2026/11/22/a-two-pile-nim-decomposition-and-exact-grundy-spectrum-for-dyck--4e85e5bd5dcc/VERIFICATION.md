---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For a Dyck prefix ending at i and Dyck suffix starting after j with j≤i, their overlapping height constraints force total balance H=0, and the union covers a nonnegative path. Thus non-Dyck words have separated maximal Dyck ends and a nonempty invariant core: extending past a maximal end would require a Dyck end of the core, since appending a balanced nonnegative excursion cannot restore a still-positive height to zero. Each move cuts off complete primitive factors at one end; for a Dyck word this is a single heap, and otherwise the two end counts are independent Nim heaps. The intersection with (ab)*b(ab)* really is the equal-count language, proving nonregularity. The unique decomposition gives q=(1−p)^2/(1−2z)−(1−p); the common high bits in k and k xor g yield the geometric residue-block denominator. At z=1/2, the fixed-count pair has leading pole 2^(−k−l−2)/(1−2z), and these limiting masses sum to one. The loss series expands as 1/[3(1−2z)]+(4√2/9)(1−2z)^(-1/2)+constant+O(√(1−2z)); at −1/2 only a weaker square-root term occurs. Since |p(z)|≤1/2 on the closed convergence disk, there are no competing denominator zeros there. Coefficient transfer gives the stated probability and correction. Read the supplied scripts and saved output without executing: the finite checking report overcounts the tested residue identities, since verify_series.py lines 67–78 skips the assertion for g=8,…,15 (2M=32>N//2=30); only eight reach it. This is nonessential corroboration, not a defect in the all-length proof. Exact replay locators for the mathematical checks are RESULT.md lines 62–95 and the residue loop in verify_series.py.

## originality

PASS

The strongest same-day material covers the one-sided primitive-count game or a different bilateral language of moves, not the two-sided invariant-core game. Credit the existing one-sided Catalan/geometric result and two-sided word-subtraction framework separately. The two-sided decomposition and ensuing exact xor spectrum and loss asymptotic are distinct on the available evidence; no day-level ordering or definitive historical priority is inferred.

## value

PASS

A natural context-free move language on both ends yields a complete normal-play classification. The invariant core provides a structural reason the two ends are independent during play, while the all-length spectrum and one-third loss density quantify the effect of adding the second end. This goes beyond the standard Catalan formula or the ordinary Nim sum rule separately.

The dated certificate retains the supplied scientific assessment, sources and limitations.
