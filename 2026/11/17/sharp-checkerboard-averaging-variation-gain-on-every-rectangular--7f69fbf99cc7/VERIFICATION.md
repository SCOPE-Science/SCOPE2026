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

The projection has exactly two class means and every grid edge crosses colors, so V(Pf)=e|mean_B-mean_W|. Orient edges black to white. An edge load with black incident sum 1/b, white sum 1/w, max load 1/(2b), certifies |mean_B-mean_W|<=V(f)/(2b). For even mn a spanning Hamiltonian cycle with each edge load 1/(2b) supplies the certificate. For odd mn, the source gives eight explicit Hamiltonian snake paths and nonnegative divergence-preserving flows, mixed with weights (m-1)/(m+n-2) and (n-1)/(m+n-2); its explicit interior/boundary edge formulas show every load <=1/(2b), with corner-edge equality. The corner impulse (degree two and class size b) attains e/(2b), where e=2mn-m-n. Independent fresh exhaustive enumeration of 103,234 nontrivial cuts on seven small grids gives the exact value; independent LP feasibility of capacitated divergence flows succeeds on five odd grids including 7x7. Infinite-grid proof relies on explicit symbolic edge estimates, not these finite LP checks.

## originality

PASS

The sharp odd-by-odd grid norm and bounded eight-path flux solve a two-dimensional constrained cut problem; known coarea/flow theory supplies the framework, and cyclic/path two-color projector results supply related special geometries, but not the odd grid capacity bound or full rectangular sharp norm. Even-size cycle upper bounds are acknowledged as a simpler known mechanism.

## value

PASS

A graph-TV exact operator norm for a natural two-class averaging map exposes a sharp stability boundary (only 2x2 nonexpansive), a parity correction in odd-area grids and a near-two amplification limit. The explicit nonnegative eight-snake certificate resolves a nontrivial odd-grid combinatorial obstruction and gives reproducible sharp worst-case corner data, relevant to graph smoothing and cut-based variation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
