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

Four tensor-projector eigenvalues 0,p,q,p+q give D,E_p,E_q,F exactly. Independent SymPy/Sturm checks of all seven pq≤12 pairs found no positive diagonal root and only the expected h=0 off-diagonal roots; independent 15-term bivariate shifted-coefficient expansions for (2,7),(3,5),(4,4) have strictly positive coefficients, covering every pq≥13 integer pair by symmetry. F numerator has strictly positive positive-h coefficients; at h=12/(p+q) D is negative above the threshold. The E_m cubic sign at m=37 has the displayed positive quadratic certificate; m=38 has negative witness at z=15 and Descartes gives exactly two positive zeros. Independently evaluated examples: (2,7) negative diagonal -4937/690899; m=37 positive edge 15/2523067 and m=38 negative edge -10/665323 at z=15. Finite evaluations support but do not replace symbolic infinite-parameter proof.

## originality

PASS

The earlier complete square-rook theorem genuinely covers the square all-entry part, but not the unequal rectangular product theorem or separate adjacent threshold 37/38. General absolute-monotonicity results cannot determine these exact graph-specific entries. Best-of-knowledge original surviving assertions remain, with prior square contribution explicitly limited.

## value

PASS

Rook graphs are natural two-factor lattice/line graphs, and the exact all-time stochasticity frontier pq=12 separates a Markov transition from an unphysical negative heat step. The independent 37/38 adjacent entry cutoff exposes a second sign mechanism even where diagonal positivity already fails; this is a motivated exact infinite-parameter classification, not a small numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
