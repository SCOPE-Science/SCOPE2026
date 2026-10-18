---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For a=||g1||,b=||g2|| and c=abρ<0, published PCGrad directions are gi−(c/||gj||²)gj. Their sum d yields g1·d=a²−c²/b²=a²(1−ρ²), and g2·d=b²−c²/a²=b²(1−ρ²), hence ratio a²/b²; raw sum is common descent iff −ρ<a/b<−1/ρ and norm²=(1−ρ²)(a²+b²−2abρ). At antiparallelity both projected vectors are zero. Direct finite independently constructed vector tests verified 12 cases. Proof is elementary algebra and correct within precisely two-task first-order branch.

## originality

FAIL

FAIL: the defining two-gradient PCGrad projection formula is explicitly present in Yu et al (2020) Algorithm1 and appendix, which also derives overall cosine-squared angular attenuation and identifies gradient-magnitude imbalance and near-antiparallel slowdown. The presented taskwise dot products are immediate single-line consequences of those published formulas, and the raw-sum inequality is direct dot-product rearrangement. As mathematical implications, not only wording matches, the old exact projection already determines every claimed identity. No distinct new theorem survives without merely calculating published vector identities.

## value

FAIL

FAIL: the two-task gradient ratio statement and simple strict-descent interval are routine algebraic deductions from the already-explained PCGrad projection and the definition of directional derivative. No additional genuine motivated obstruction, classification, method, or nontrivial boundary is proved beyond the source algorithm geometry. Correctness and a catchy quantitative restatement are not independent mathematical value under the uniform criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
