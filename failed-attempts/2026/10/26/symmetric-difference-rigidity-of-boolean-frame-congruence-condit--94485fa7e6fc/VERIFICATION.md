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

In RESULT.md:25–46 the instance (a,0,a) forces f(0)≤f(a), since u⊕v≤u implies v∧¬u=0. The instance (a,0,b) for a≤b then forces f(a)≤f(b), using f(a)=(f(a)⊕f(0))∨f(0). Set u=a∨b; u⊕a≤b implies f(u)∧¬f(a)≤f(b) by monotonicity, and therefore f(u)=f(a)∨f(b). Conversely, join preservation applied to the common part x∧y and the two disjoint differences gives f(x)⊕f(y)≤f(x⊕y)≤f(z) for x⊕y≤z. These steps require neither atoms nor a normality assumption. A coordinate with bottom value 1 is constant; every other coordinate is the OR of a uniquely selected set of the n input bits (including the empty set). This gives (2^n+1)^n, 2^{n(n−c)} for prescribed bottom of size c, and 2^{n²} for empty bottom. In the source example, 5⊕1=4 but 7⊕1=6 is not below 4 in bitwise inclusion. Static inspection of checker.py:5–57 and VERIFICATION.md:19–25 confirms the stated finite scope: all maps for n≤2, only coordinate-form maps and the explicit bad example for n=3. The general proof, not that diagnostic, establishes the claim.

## originality

FAIL

A distinct earlier Resultary finding, SCOPE-the-symmetric-difference-cep-hypothesis-is-exactly-boolean-addit--fc81d7d34f64 (2026-10-12), already has the same universal equivalence, the same labelled census, and the same counterexample to the motivating paper's assertion about Example 2.2. The fixed-bottom refinement is the immediate independent coordinate count obtained by forcing constant one on exactly C, with 2^n options at each remaining coordinate. No material distinct result survives. This establishes earlier catalogue coverage, not a claim about external publication priority.

## value

PASS

The mathematical content is a useful structural correction, not just a small example: it eliminates an allegedly weaker sufficient condition as a route to nonadditive examples and clarifies what is being counted on finite Boolean frames. That utility is already available in the earlier finding and does not overcome the originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
