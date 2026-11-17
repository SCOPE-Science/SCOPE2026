---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For rooted perfect binary T_h, ancestor-closed subset concepts include empty ideal and satisfy N_h=1+N_{h-1}^2, yielding 2,5,26,677. The 2^h leaves are VC-shattered, so Ldim>=2^h. For h<=2 cardinality bounds match. For h=3, at any root/internal query the negative branch has respectively 1,27,157 concepts with Ldim at most 0,4,7. At a leaf query the positive branch is the product of three independent sibling ideal classes of heights 0,1,2, with Ldim 1+2+4=7 by standard product additivity. Thus no depth-nine mistake tree exists; Ldim is exactly 8, first strictly less than floor(log2 677)=9. All 0<=h<=3 proof cases handled.

## originality

PASS

Standard Ldim recurrence and cardinality are established, but the h3 conclusion needs comparing each depth of the first queried vertex and showing every leaf-positive branch splits as a 1+2+4 product; standard entropy inequality alone permits dimension nine. The general class-size upper bound floor(log2|C|), VC lower bound, and product-additivity theorem determine lower-height cases but do not alone give the all-first-query obstruction at h=3. General query-compression results and online tree learning prove different learning guarantees, not the 677/8 first-gap classification.

## value

PASS

The first strict mismatch between entropy/counting and optimal adversarial online mistake complexity in a canonical nested hierarchy is a motivated exact finite threshold, distinguishing adaptive query difficulty from class size at the 15-vertex boundary. It is a natural online-learning invariant of rooted-tree ideals, not an arbitrary relabeling or isolated computational curiosity; claims of a general h formula are deliberately avoided.

The dated certificate retains the supplied scientific assessment, sources and limitations.
