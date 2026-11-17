---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Linearized Fourier eigenvalues yield rc=1+2/(1+u) and a transverse simple critical m=±1 pair; other three eigenvalues remain inside unit disk. Quadratic B map, zero cubic derivative, and h11/h20 nonresonant homological corrections produce exact cubic radial coefficient -(u+3)^2 P/(2(1+u)^2 Q). Independent SymPy substitution verified symbolic coefficient identity, cubic sign brackets and positive roots 0.606103247 and 1.270962528. Descartes plus sign alternation ensures exactly two positive roots, not merely observed roots. Strong resonances u=1/3,1 and zeros of P excluded; theorem only local. A pole/denominator and clipping-inactive arguments were checked.

## originality

PASS

Published three-site balanced oriented logistic-ring primary result has negative cubic coefficient everywhere and no criticality reversal. The five-site Fourier mode interaction involves a different second harmonic (k=(sqrt5-1)/2) and exact cubic P with two positive zeros; this is not a direct parameter substitution. General disordered logistic systems show instability but the full primary appendix was inaccessible, so retain possible coverage risk rather than disqualifying solely for access.

## value

PASS

The exact two reversals provide a mathematically motivated bifurcation phase diagram: crossing the same first instability can generate attracting or repelling invariant circles depending on the oriented coupling strength. The low-dimensional ring is the smallest next case after the uniformly supercritical three-site ring.

The dated certificate retains the supplied scientific assessment, sources and limitations.
