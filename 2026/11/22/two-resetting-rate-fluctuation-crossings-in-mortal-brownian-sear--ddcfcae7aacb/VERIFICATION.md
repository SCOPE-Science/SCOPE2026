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

Renewal at the first reset gives the immortal transform 1/(1+qA(q+ρ)); independent exponential mortality tilts this transform to φρ(m+u)/φρ(m), normalized by the probability of success. Logarithmic differentiation gives V−M²=−(2A′+mA″)/(1+mA). Since A″=H/(4z⁶)>0 for z>0 by H′=e^z(z²−3z+3)>0 and H(0)=0, the sign of CV−1 is that of B(z)−m, with z=√(m+ρ). Expanding the numerator of B′ gives G/z²=−6 plus positive powers with positive coefficients: g₄,…,g₁₀ are positive directly, and for n≥11 P(n)≥30 and a doubling induction shows 30·2ⁿ>16n³+320n. Thus G/z² has one positive simple zero, and B has a strict nondegenerate maximum; B″(zc)=−4zcG′(zc)/H(zc)²<0. At the boundary z=√m the sign follows from B(z)−z²=z³e^z(1−z)/H(z). Together with B(1)=1, zc>1, mc<zc², and the subsequent zero of B, this proves the counts and signs, including the excluded zero-rate equality at m=1 and the admissible double root at mc. The high-precision independent check recovered mc≈1.10642822093643738483 and ρc≈0.28424024613180761599 and both rates at m=1.05; it compared moments at 12 parameter pairs. Replay: /workspace/branches/46a31644-dec4-48b3-8590-ae91fd3d2fa3/independent_crossing_check.py. The supplied check.py and verification notes were read, not executed; the infinite coefficient argument, not a finite scan, proves uniqueness.

## originality

PASS

Radice has the same conditional moments and a numerical investigation of the equality, including the approximate upper mortality cutoff. The supported distinct claim is the global admissible-root classification, the exact single-maximum characterization and double-root threshold, and the nonempty two-positive-crossing regime for the same-start reset rule. No match other than the assigned record itself states this classification in the inspected sources.

## value

PASS

The exact classification resolves a narrow qualitative regime easily lost in numerical searches: two positive rates delimit a higher-relative-fluctuation window when both zero and large reset rates give sub-unit conditional CV. The proof establishes the unique boundary and its multiplicity for all admissible mortalities and corrects a single-crossing reading of the prior numerical treatment without making an optimization claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
