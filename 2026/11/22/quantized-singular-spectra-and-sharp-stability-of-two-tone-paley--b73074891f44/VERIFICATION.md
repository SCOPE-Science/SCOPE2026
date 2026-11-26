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

Plancherel with zero extension gives T*T=(1+r²)I+r(S_h+S_h*) for h=2η; neither diagonal term is clipped in the stated codomain. Reindexing the input interval by residue mod h is a unitary map to the sum of L² fiber intervals tensored with finite path spaces. At integral q the only length is q a.e.; at nonintegral q the two listed lengths occur on intervals of the stated positive measures, except the omitted length zero when q<1. Sine diagonalization gives the entire finite spectral list, with each eigenvector tensored with a separable infinite-dimensional L² space. Coprimality of consecutive denominators excludes duplicate cosine fractions, including in the case of only length one. The extrema come from length m and are attained on a set of positive measure. The lower Gram eigenvalue is (1−r)²+2r(1−cos(π/(m+1)))>0. For r=1 the half-angle formulas give the inverse bound, condition number and η↓0 limit, and the ceiling gives the one-sided jump at each exact threshold. The packaged finite checks are not a proof of the fiber or spectral assertions and were inspected, not executed.

## originality

PASS

Best-of-knowledge pass for the full positive-measure fiber spectrum and attained sharp gains of this two-tone multiplier. The known finite path spectra and the Fourier translation identity are ingredients, not separate originality claims. Neither the related catalogue result nor the inspected primary exact spectral or multiplier results cover the adjacent-length compressed translations needed here.

## value

PASS

This is a minimal nonconstant multiplier for which a pointwise zero of the symbol makes a naive lower bound useless. The exact inverse gain specifies the attainable stability and condition number, including discontinuities at bandwidth thresholds, and the full spectral levels distinguish the short and long chains. This is useful beyond a mere norm estimate or the known finite path computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
