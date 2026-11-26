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

Retain the validated correctness reconstruction. For target (1,c), set u=x+y, v=xy, z=u+1: the reciprocal condition is v(cu+c+1)=u(u+1). Off c=0,1 the three excluded u-values are 0, (c+1)/c, 1; at each remaining u the quadratic for x,y splits into two distinct nonzero roots exactly at absolute trace zero. The two simple rational poles have different exponent two each, giving genus one; they each contribute one rational point. The regular fibers at 1 and infinity contribute two points each, making the correction six. Hasse gives a positive generic count for q≥16. The axes reduce to the absolute trace of 1+1/u excluding the inverse indices zero and one; origin returns correspond to nontrivial cube roots of unity; on the generating hyperbola the repeated-step count is exactly 3q−5. The retained independent XOR and polynomial-product enumeration gave exact-three supports 1,4,42,256,1023 and at-most-three supports 2,4,64,256,1024 for q=2,4,8,16,32, and R3(1,c)=6,19,6,0,6,0,6,0 in the specified basis at q=8. For the infinite ranges the preceding algebra and Hasse, not the samples, prove support. Two steps never give a nonzero axis target, so once connected the diameter is exactly three. The small-field Frobenius graph explains disconnection for q=2,4.

## originality

FAIL

The diameter is the already known binary Melas covering radius. The direct coding comparison also resolves the main count, not just diameter: Li–Xiong Proposition 3, eq. (7), and Appendix A Proposition 7, eq. (17), give the identical punctured-field trace-fiber count after t=1 and a translation of the remaining coordinate. For generic targets each accepted coordinate yields exactly two ordered quadratic roots, and completing that same Artin–Schreier equation adds the six immediate fibers. Thus the principal exact numerical invariant and elliptic mechanism are a routine restatement of an existing count, even though the older paper uses it toward existence bounds and does not print the frozen full support table. The remaining singular targets and small-field entries are elementary boundary evaluations of the same equations, not a distinct substantive remainder.

## value

FAIL

The retained earlier review correctly found exact targetwise behavior mathematically meaningful in isolation. But the completed comparison shows that the main fiber count and the radius are established in equivalent coding terms, and that the difference is a change of variables, a count of immediate missing fibers, and elementary exceptional evaluations. Those evaluations and the small-field restatement do not supply an independently valuable new invariant or theorem. The presentation can be useful as an exposition of the graph–code equivalence without being a distinct scientific finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
