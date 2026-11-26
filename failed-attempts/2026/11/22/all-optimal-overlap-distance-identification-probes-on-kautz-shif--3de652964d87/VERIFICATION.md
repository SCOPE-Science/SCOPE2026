---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

FAIL

The theorem is true, but the frozen sufficiency proof makes a false overlap assertion at RESULT.md line 29. With q=3, n=5, targets u=01010 and v=02012 have common-prefix length k=1. Take p=1020 and s=pu_2=10201. The maximum proper overlap with u is 2 and that with v is 4, not k. The missing argument is that the selected probe has overlap at least k+1 with its corresponding target and the two maximal overlaps cannot be equal at any length >=k+1, since the targets' prefixes then differ. A probe that is a target separates directly with distance zero. This establishes the theorem independently but does not validate the frozen proof as written. Necessity follows from prefix twins and the directed overlap formula; counting then multiplies one factor (q-1)z^(q-2)+z^(q-1) per class. A separate BFS check exhausted 4,096 minimum transversals at q=3,n=4 and certified all 18,336 target pairs at q=3,n=7 via the existence of a class containing two distinguishing probes; these bounded checks do not prove the general claim. The source script was inspected, not run. No repair was delivered because the corrected classification is covered by prior work.

## originality

FAIL

Feng, Xu and Wang, arXiv:1107.4140v1 (20 July 2011), Sec. 2, prove the arbitrary one-omission resolving-set assertion for strongly connected line digraphs, not just a numerical dimension. Their direction convention reverses the distance channel here. Reversing the base digraph makes the assertion exactly the Kautz prefix-class characterization, and the counts and ranking/sampling follow by independent choices. The cited Rajan comparison misses this stronger primary source.

## value

FAIL

A complete characterization of independent resolving choices would be useful if unknown. Here the general characterization is already proved, and the specialized enumerator, optimum count and sampling instructions are its direct product reformulations. The short correction to the overlap proof does not produce a distinct worthwhile new invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
