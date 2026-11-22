---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The canonical 2x2 two-projection blocks give D=sum_j t_j and C=max_j sqrt(t_j(1-t_j)), for unrestricted t_j in [0,1] because n>=2k. For C<=c the scalar sublevel is [0,a] union [1-a,1]; counting coordinates in the upper band gives the two necessary lower bounds delta/(k-m) and (1-delta)/(m+1), and saturation patterns attain the smaller. Upper bound follows exact feasible coordinate interval; convex fixed-sum polytope plus continuous C gives every intermediate value. Crossover in each integer cell gives sqrt(k)/(k+1). Independent 404 sampled fixed-distance tests across k=1,2,3,7 and direct block formulas corroborate the proof; equality cases and integer endpoints follow from saturation, not sampling.

## originality

PASS

Classical principal-angle decomposition and operator-norm commutator bounds are fully credited. Loring studies perturbations to commuting projections, Aouichaoui arbitrary-idempotent commutator lengths, Bourin–Lee angle identities, and Conde unconditional norm inequalities; none of the inspected material gives the exact fixed-Frobenius-distance, rank-k joint compatibility region and all minimizers. Older equivalent conditional norm inequalities remain a risk.

## value

PASS

The orthogonal Grassmannian chordal distance and commutator norm are natural noncommutativity/geometric separation observables. Their complete attained joint region exposes a sharp quantized commuting-distance valley and rank-sensitive peak not captured by unconditional 1/2 inequalities; this is a mathematically motivated exact extremal classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
