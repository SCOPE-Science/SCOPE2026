---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The map is square-preserving: each coordinate is a bilinear interpolation of its four corner values in [0,1]. All states except the two stationary corners have interior first images. The neutral fixed equation gives x=X(y); Q'=1+ac/R²>0 gives one neutral point on each H chord. Direct substitution gives the defect ΔH=εx(1−y)/b, not εx(1−y). Along each chord the first-coordinate derivative is the difference of two convex combinations, with absolute bound q*=max(1−min(a,b),c,ac/b)<1, uniformly up to its ends. The x-update is independent of ε, and the neutral projection is Lipschitz; subtracting the projected x at the next H gives |eₙ₊₁|≤q*|eₙ|+C|ε|. The reduced scalar Euler remainder per step is therefore O(|ε|q*ⁿ+ε²). Over n|ε|≤T the geometric sum and discrete Gronwall give O(|ε|) in H including n=0; taking floors adds O(|ε|). State-space approximation starts at δ>0 because the remaining q*ⁿ is then O(|ε|); on-curve initialization eliminates that term. Under H=Q(t) the reciprocal unsigned drift is (R²+ac)/(t(1−t)R); differentiating the three logs gives this expression, positive on (0,1), with the stated divergent endpoint logs. At the attracting corner the Jacobian characteristic polynomial at one is |ε|, with derivative tending to a+c at (0,0) and b+ac/b at (1,1); the simple Perron root thus has the stated first-order rate, and the other root stays inside the unit circle. Passage is in the first-crossing sense of the neutral-level coordinate H, not exact equality of the perturbed state to a point on the curve. H is monotone for fixed sign; nonzero limiting drift at interior target levels and the uniform H estimate justify the passage clock. The frozen symbolic and numerical checker was inspected, not executed.

## originality

PASS

Credit the explicit map-specific passage clock, the compact-slow-time first-order discrete error, and the matching endpoint rates as a quantitative result. The map, neutral fixed curve and fixed-parameter convergence are not new. The closest same-map sources were compared with their actual parameter conventions and continuous/discrete statements; the 2011 access gap limits historical priority without establishing coverage.

## value

PASS

When a neutral continuum splits, knowing the eventual attracting corner does not predict how long a trajectory remains near earlier neutral states. The explicit clock gives transition times between interior levels for a natural previously studied model, separates the short transverse transient from the slow motion, and makes the scaling and rate constants comparable to the local spectrum. It is a quantitative advance over qualitative endpoint selection, not a claim about a stochastic finite population.

The dated certificate retains the supplied scientific assessment, sources and limitations.
