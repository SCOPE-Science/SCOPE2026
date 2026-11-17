---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The three inverse branches of the explicit map g give L=(0 A;B 0) on two polynomial halves; A is invertible reflection and ABf(y)=[f(1/4-y/2)+f(1/4+y/2)]/2. AB has image the even polynomial space of dimension floor(d/2)+1; triangular filtration has distinct nonzero eigenvalues 4^-k, hence zero is semisimple for AB. Similarity of BA and AB and rank L=(d+1)+(floor(d/2)+1) give precisely ceil(d/2) size-two Jordan blocks at zero, and simple ±2^-k nonzero eigenvalues. The exact second transferred centered coordinate φ gives L²φ=(-1/4,1/4), a -1 eigenmode; C0=1/12, C1=-7/96, Cn=(-1)^n/16 for n≥2. A separately constructed exact SymPy transfer-matrix implementation reproduced charpolys and ranks for every d=0,...,7. The proof, not these finite degrees, establishes all d and all polynomial-pair correlations.

## originality

PASS

Vinod Kumar P B arXiv:2610.39443v1 full accessible HTML proves the sharp minimum entropy ½log2 and square-root interval construction but does not derive this map’s polynomial density-transfer Jordan spectrum; no occurrences of Frobenius or transfer in its accessible full HTML. Classical Yoshida–Mori–Shigematsu 1983 studies tent-map band splitting, Perron–Frobenius eigenmodes and time correlations, but the full primary text was not available (authorized retrieval disconnected VPN). Its abstract cannot rule out all overlap and remains a specified priority risk. Resultary semantic searches of minimum-entropy interval transfer polynomial spectra revealed no stronger covering theorem. Best-of-knowledge O PASS for exact all-degree spectrum and nilpotent part, not for known alternation or entropy bound.

## value

PASS

This supplies the complete finite-degree spectral decomposition, including nilpotent Jordan blocks controlling exactly two-step transients, for an explicit extremal-entropy nonmixing transitive map. Exact correlation modes for all polynomial observables separate entropy positivity from mixing and give a useful solvable transfer-operator benchmark. The result is more than renaming the entropy construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
