---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

F(t)≡1 modulo t and F(1)=1 handle equal and unit operands. In a minimal nontrivial pair 2≤a<b, c=F(a)/b is positive and smaller than a, and bc≡1 modulo a gives c²F(b)≡F(c) modulo a. Thus (c,a) is a smaller solution, impossible. This proves the graph claims as well. Gcd-class grouping gives nH(n)=Σ_{d|n}dφ(d), with local factor (p^(2α+1)+1)/(p+1). In the squarefree two-prime case H(pq)=F(p)F(q)/(pq), and p∤F(p), q∤F(q), so the two cross-divisibilities are precisely the integrality condition. For a single prime the self-divisibility is impossible. No claim on p² or longer cycles is needed. The supplied finite output and code were inspected, not executed; the argument is universal by descent.

## originality

FAIL

Mills (1953), Section 5, Theorem 3, p. 217, already states exactly the positive-integer minus-sign reciprocal system and its singleton solution. His general equation and chain classification also cover this as A=−1. The arithmetic consequence is immediate from that theorem and the already published gcd-sum product/reciprocal-prime reduction; the graph interpretation is equivalent. This is known coverage, not a failed search or a mathematical counterexample.

## value

FAIL

Eliminating a two-prime dependency would be useful if unresolved. Here the main result is a repeat of a published classification, and the graph and arithmetic parts are direct restatements or routine substitution into the known reciprocal-product reduction. No independent new obstruction or genuinely distinct valuable remainder is delivered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
