---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

The final claim is mathematically correct. Full finite chain bases have 25,200,600,600,120 faces; fresh independent F3 Gaussian elimination gives boundary ranks 24,176,423, whence dim H2(F3)=1. The eight-term join cycle z is closed and not a boundary; independent coordinate computation and full checking of the actual 60-term certificate from certificate.json prove ∂w=τz+z on all 600 oriented triangles. Row and column generators send z to -z exactly, and group conjugacy gives the product-sign factors. Shareshian–Wachs / Jonsson independently prove integral H2=Z/3, and the H1=0 connectivity premise makes integral to mod-3 reduction injective. Thus tau acts -1 integrally. Barycentric subdivision removes inversions, and exactness of C2 coinvariants over F3 yields H2(ordinary quotient;F3)=0. Only this board and degree are proved; finite check is exhaustive for the finite complex, not a result for all board sizes.

## originality

FAIL

Previously published October 18, 2026 result for precisely the same ordinary 5-by-5 chessboard complex and its diagonal transposition explicitly proves tau_*=-1 on integral H2=Z/3 and the full (S5 x S5) semidirect C2 character. It also proves the ordinary quotient has no three-local H2 and has a strictly stronger 3-local homotopy classification, wedge of 28 localized S3. The November 8 claim is a corollary/special case, hence no original surviving assertion. The same exact 60-term transpose boundary identity already occurs in the October proof, though the generator/coordinate presentation differs.

## value

FAIL

The natural object and invariant are inherently mathematically motivated: the first square chessboard with integral three-torsion, its missing bipartition-swap character, and an ordinary quotient. However, the exact distinguishing fact, full sign action, and quotient vanishing were already published on October 18, with a stronger complete 3-local homotopy classification. The November 8 paper contributes a redundant second 60-term boundary derivation but no newly determined non-implied natural invariant or structural lemma. A previously established stronger theorem makes this version unpublishably duplicative under the shared value standard, rather than intrinsically uninteresting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
