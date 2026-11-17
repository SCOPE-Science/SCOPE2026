---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For gamma>1 and positive row-normalized weighted edges on finite connected loopless bipartite graph, the inverse response g=f_{1/gamma} has g=f_gamma^{-1}. Maximizing x_i over A and using x_j≤g(p) over B, strict averaging equality at a maximizing vertex forces every neighboring B state to g(p), and connectedness propagates equality across all vertices; hence the equilibrium set is exactly A=p and B=g(p), 0≤p≤1. For unweighted K_{m,n}, exact averaged ODE has H=1+(gamma−1)b, L=gamma−(gamma−1)a, invariant R=H/L. Differentiation proves (L²)′=2(gamma/R−L²), hence the explicit e^(−2t) formula for a,b and e^(−t) within-part deviations, all initial cube states and endpoints. Checked fetched verify.py and independently verified conservation and initial/limit bounds. No stochastic urn trajectory claim.

## originality

PASS

Tang–Adler–Ajorlou–Jadbabaie give the identical response map and stochastic model, but the inspected primary paper restricts its main equilibrium isolation discussion to nonbipartite networks, notes marginal reciprocal-bipartite Jacobian, and does not derive the full continuum or exact continuous-time complete-bipartite flow. Earlier SCOPE nonconsensus uniqueness result expressly assumes nonbipartite support. The nontrivial first integral and every-initial-state selection are best-of-knowledge original.

## value

PASS

Reciprocal biases on bipartite graphs are exactly a marginal, nonisolated equilibrium regime in nonlinear opinion systems. Classifying its entire equilibrium manifold and integrating dynamics from arbitrary heterogeneous initial conditions resolves a substantive boundary left by generic nonbipartite theory. The invariant gives a precise selection law and rates, useful for degenerate nonlinear network flows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
