---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

With n odd, p∤n and squarefree (x+2)D_n, genus g=(n−1)/2. Cited q²-maximality gives π²=−q as a genuine endomorphism using semisimple faithful ℓ-adic Tate action. Thus χπ=(X²+q)^g and |J(F_q)|=(q+1)^g. At odd ℓ|q+1, Hensel split into ±1 roots with rank g each implies ℓ-primary factors (Z/ℓ^vℓ(q+1))^g. At 2, branch points −2 and roots z+z⁻¹ with z^{2n}=−1; q≡3 mod4 makes all branch points rational, so full J[2] rational; q≡1 mod4 makes g switched pairs plus two fixed, giving exactly g rational 2-rank (invariant representatives because two fixed coordinates obstruct complement cocycle). For q≡1 mod4 v2(q+1)=1; for q≡3 mod4 put A=(π−1)/2, then A²+A+(q+1)/4=0; at v2(q+1)=2 A is a unit, and for v2≥3 the polynomial has separated 2-adic roots, splitting rank-g summands with elementary divisors 2 and 2^{a−1}. Chinese remainder yields the displayed groups. Reviewed exact pinned `verify.py` script: checks rational curve points, branch 2-torsion, compatible predicted factors in ten q=p examples; these are only corroboration, not an independent group computation or proof for all powers.

## originality

PASS

Best-of-knowledge exact rational Jacobian elementary-divisor classification beyond previously known maximality and minimal automorphism results. Same-family Borges–Reis full text was inaccessible despite lawful attempts and remains a significant, named residual risk; absence of access alone is not negative originality evidence.

## value

PASS

Exact abstract finite rational Jacobian groups in an infinite unbounded-genus family with minimal geometric automorphisms are natural arithmetic invariants not determined by maximality or total point count. The sharp change controlled by q mod 4 captures nontrivial integral 2-adic structure; relevant beyond table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
