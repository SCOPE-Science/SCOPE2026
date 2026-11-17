---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

All perfect monomial structure matrices yield monomial algebra isomorphisms: multiplying distinct image basis vectors forces disjoint coordinate supports. The directed support permutation decomposes uniquely into cycles. For a weighted length-l cycle the diagonal rescaling invariant is the coefficient product with powers 2^(l-1),...,1 mod (F_q^×)^(2^l-1). One cyclic shift squares the invariant. Stabilizers have g=gcd(q-1,2^l-1) diagonal choices and l/h rotations; cycles of identical orbit type permute by wreath product. Burnside gives a_l=1/l sum gcd(g,2^r-1), and the independent-multiset product generating series follows. The asserted sharp maximum follows from h>=1 and prod m_i!<=m! with equality for unweighted cycles. Critical boundary l=1 and q=2 are included. The proof is universal; code finite tests are only corroboration.

## originality

FAIL

Prior full published Oct 27 single-cycle result already proves exactly the doubling-orbit normal form, Burnside class count and cycle automorphism orders; same-day published weighted-cycle result independently states the identical one-cycle orbit/automorphism formulas. The present all-cycle assertion is the formal free multiset decomposition and wreath-product automorphism bookkeeping from these known single-cycle theorems; the maximization is a direct factorial domination with all unweighted cycles. Nothing substantively new remains in the original classification.

## value

FAIL

Although general monomial algebra classification is a natural subject, adjoining disconnected cycles introduces only standard multiset products and permutation wreath automorphisms once the exact earlier one-cycle arithmetic theorem is available. The displayed maximum is a tautological optimization over integer partitions, without a novel nontrivial evaluation or structural phenomenon. The covered original cannot be accepted on its own significance or code.

The dated certificate retains the supplied scientific assessment, sources and limitations.
