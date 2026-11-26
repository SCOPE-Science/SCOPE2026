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

Burns explicitly quotes the four Deutsch–Sagan zero-index families. Moving the shifts to the left, n+1 has unit 2 at odd valuation or 4 at positive even valuation in two families, and −(n+2) satisfies the same rule in the other two. Nonnegative progression parameters meet every finite cylinder of each shell; the only extra limit points are −1 and −2. The disjoint partition X=A ⊔ B ⊔ 25X has A=10+25Z_5 and B=100+125Z_5. Adding shell pairs gives full cosets at 10,20 mod 25 and 75,100 mod 125, plus 25P⊂125Z_5; differences are exactly the three mod-25 cosets 0,10,15, since A−A fills 25Z_5. The translated P,D,−P branches are disjoint modulo five. With p_1=1,p_2=3, the recursion p_k=2·5^{k−2}+2·5^{k−3}+p_{k−2} gives p_k=(5^{k−1}+1)/2; D has one class at depth one and 3·5^{k−2} thereafter. Hence the sum support has size 3 and then 8·5^{k−2}+1. The decreasing cylinder unions give Haar measure 8/25, and the X partition gives measure 1/20 for X and 1/10 for the two-branch closure. For any four signs, selecting signed A slots (or signed B slots) gives five consecutive integer net coefficients, one per mod-five residue. A nonzero leading target chooses at least one slot, whose full coset supplies all higher digits. Divide by 25 for valuations ≥3 and take zeros for zero. The five branch totals −8+r exhaust the mod-five residues and three terms miss residue 3. Projection commutes with closure here because finite residue cylinders are open and closed, so this gives congruences with actual nonnegative indices, not exact integer equalities. Inspected verify_motzkin_sumsets.py and VERIFICATION.md without running uploaded code: the finite support checks extend through 5^6, and the finite signed check tests every nonzero multiple of five modulo 125 (zero follows from four zero inputs). The all-depth argument does not depend on that replay. No formal or expert attestation is asserted.

## originality

PASS

The published zero-index set and its ordinary density are prior. The supported distinction is the full compact two-sum image (including membership in exceptional congruence cylinders), all-depth support formula, and sharp four-term coverage by a signed valuation lift. No equivalent exact additive assertion was identified in the inspected sources.

## value

PASS

For a canonical modular zero-index set, knowing density or a recognizer does not tell which congruence classes sums reach, whether an exact representation exists at every depth, or the sharp covering order. The explicit self-similar obstruction for pairs and uniform signed lift for four give direct membership and representation tools for this natural, fixed prime case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
