---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Distance three makes each coordinate projection injective, so |C|<=q; at equality the rows have form (i,f(i),g(i)) for bijections f,g. A shift-one splice is possible exactly where g(i)=f^2(i); a shift-two splice is possible exactly where that equality holds at g(i). Complemented reversal sends row i to row t(i)=c(g(i)); the middle position gives t=f^{-1}cf and t^2=id ensures that the final position matches. This proves both directions of the stated classification. In the binary case any nonempty closed code would have size two, but f can only be the identity or c, both forcing g=f^2=id. The explicit four- and six-symbol blocks were checked against the literal conditions. Disjoint complement-stable blocks preserve distance and closure, and cross-block splices use symbols from both blocks, hence cannot equal a row. Every even q>=4 is a sum of fours or a six plus fours. An independent exhaustive replay pairs each smallest unused first symbol with its mate's first symbol, tries all unused middle-complement pairs, and checks literal splices and coordinate distinctness, without assuming the permutation inequality. It verifies the exact four-symbol list, both orbit sizes 2 and 4, and the counts 0,6,160,8988 for q=2,4,6,8.

## originality

PASS

Best-of-knowledge pass for the simultaneous length-three synchronization, closure and maximal-distance problem, in particular the full-size classification and exact four-symbol census. The strongest distinct statements available concern genuinely different constraints; access to several plausible prior full texts remained incomplete.

## value

PASS

Length three is the natural first case for the specified simultaneous word-boundary synchronization, complemented reversal closure and one-substitution correction. The important content is not the coordinate upper bound but its exact attainability away from the binary obstruction, an efficient equality test for every paired alphabet, and the complete four-symbol census with its genuine relabeling symmetries. The census determines design diversity at a natural parameter point rather than evaluating an arbitrary small slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
