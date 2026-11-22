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

A connected weighted Dirichlet problem has a unique voltage h in [0,1] with terminal values 0 and 1. For every f, Hf=f_a+(f_b-f_a)h, so G(Hf)=|f_b-f_a|G(h). The triangle inequalities over pairs involving a or b give G(f)>=(n-1)|f_b-f_a|, sharply attained when all interior inputs coincide between their two boundary values. Summing h boundary-interior pairs yields G(h)=n-1+sum_{interior unordered pairs}|h_i-h_j|. The sorted interior gap sum has coefficients j(m-j), whose maximum floor(m²/4) proves sharp universal envelope floor(n²/4)/(n-1), including m<=1. Equal interior voltage is equivalent to all equations theta*c_{ia}=(1-theta)*c_{ib}; connectedness suffices even if the interior subgraph is disconnected. The n-node endpoint path has h_j=j/(n-1), giving n(n+1)/(6(n-1)). An independent exact-rational path check n=2..8 corroborates that specialization. The actual Git RESULT.md and source checker were inspected; finite tests do not establish generality.

## originality

PASS

PASS (bounded best-of-knowledge). Graph Dirichlet voltage/hitting probability is the same h; it does not by itself specify the induced complete-pair Gini operator norm. Sharp path amplification and conductance-level nonexpansivity require the specific voltage-gap calculation; the checked earlier results do not logically entail them. Material full texts and relevant primary sections checked; remaining historical-equivalence risks retained.

## value

PASS

Finite harmonic interpolation is a standard mathematical construction, but its precise response in an all-pair dispersion seminorm is not captured by the maximum principle. The exact graph-dependent norm, equality geometry, conductance classification and growing path loss quantify a meaningful discrepancy between harmonic regularity and complete-pair stability. It is an intrinsically motivated sharp functional-analytic result, not a random numerical instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
