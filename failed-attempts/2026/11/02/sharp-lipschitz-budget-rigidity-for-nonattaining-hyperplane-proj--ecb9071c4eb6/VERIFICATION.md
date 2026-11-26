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

The signed measure has total variation one and no atoms. For each t the representing measure of evaluation after P is δ_t−h(t)μ, with the two summands mutually singular; taking the supremum of their total variations gives ||P||=1+||h||∞ directly. Equality |μ(h)|=||h||∞ for nonzero h would require opposite constant normalized values on the two open halves, contradicting continuity. Pairing midpoint reflections gives the sharp bound 2 min(R,Lu) for the difference, attained simultaneously by the clipped ramp. Its weighted integral is R−Cα R^(α+2)/L^(α+1) for R≤L/2, otherwise L/L*. This proves feasibility and root uniqueness on the stated branch. Positivity of the density, continuity, and Lipschitz saturation between the two clipping points force the same ramp; at the critical budget endpoint saturation forces slope L and the optimal sup norm fixes the intercept. Let b=α+1 and q=2R/L. The scalar equation is (L/2)[q−q^(b+1)/(b+1)]=1. At q=1 the bracket is b/(b+1) and its deficit at q=1−z is b z²/2+O(z³). Hence R=L*/2−sqrt((L−L*)/b)+O(L−L*). At large L the increasing branch tends to R=1 and substitution gives R−1=Cα L^(−b)+O(L^(−2b)). This yields the unrestricted infimum 2 with nonattainment. The α=0 exact solution L(1−sqrt(1−4/L))/2 also checks both regimes. The frozen checker was inspected but not executed; its reported quadrature checks are bounded, not the proof.

## originality

FAIL

A distinct indexed result on symmetric signed densities gives the same optimizer, exact threshold and scalar equation even in its explicitly stated power family, as well as a stronger high-budget expansion. The one component not expressly stated there, the power-family square-root coefficient at feasibility, follows by an elementary local expansion of that very equation at its specified critical root. The indexed record is catalogued later than the frozen record; this is assessment of demonstrable existing coverage, not a claim of earlier public priority or copying. The older literature separately covers nonattainment and the max-norm dual problem but does not itself state the full finite-budget theorem.

## value

FAIL

Quantifying projection norm versus a Lipschitz budget is a natural problem, and the cusp is a useful reading of the tradeoff. But the exact curve, uniqueness and high-budget behavior are already covered in the indexed comparison, and the remaining stated power-family cusp is a local Taylor consequence of its identical scalar equation. No additional independent range, invariant or obstruction is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
