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

Torus orthogonality gives M=sum_d C(d)^2 for the full radius-two axial hexagon. C(0)=19 and the two directions of every nonzero lag contribute equally, so the integrated defect is M-361. A global sign flip changes neither M nor defect, giving exactly 2^18 distinct center-positive assignments. Independently ran python3 /workspace/review_evidence/recompute4.py. Instead of lag updates it summed squared integer coefficients of P^2 by unordered site sums, with terms doubled for two distinct sites. This computes the same fourth moment by Parseval and runs across all 262144 masks. It found moments 467,475,483 first, with counts 72,28,144, respectively; the maximum was 3259. Independent orbit traversal by the four generators (rotation, reflection and the two coordinate sign characters) preserved the minimizing set and yielded least masks 3441,8151,10446, each with 24 elements and exactly the stated negative coordinates. Hence there are 144 minimizers before sign normalization, and the sharp gap is eight. As a cross-check, each squared lag term has fixed residue modulo four from overlap parity and hence M has fixed residue modulo eight; there are nine odd positive-lag overlaps, yielding residue three. For the claimed discrete Fourier transfer, all difference coordinates lie in [-4,4], so grid periods at least nine keep all lags distinct modulo the grid. This proves only the stated full support and real-sign fourth moment.

## originality

PASS

Best of current knowledge: the inspected same-support geometry is not new, but the exact single-array aperiodic energy minimum, attainable next value and complete equality orbits on the unpunctured binary support are not supplied by the related results inspected. The exact matching indexed entry is the frozen result itself.

## value

PASS

The full second-shell hexagon is a standard, previously studied array geometry, and the integrated squared sidelobes are a natural exact single-aperture objective, different from complementarity or peak sidelobes. The optimum, gap and all symmetry classes give a usable exact benchmark for this geometry. They do not follow from the trivial moment lower bound or a first-shell classification and have value even without a larger-shell theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
