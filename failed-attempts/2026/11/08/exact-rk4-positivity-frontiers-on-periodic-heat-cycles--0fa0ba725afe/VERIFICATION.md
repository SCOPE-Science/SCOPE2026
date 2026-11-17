---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For n>=3, the RK4 update is a circulant with nine-point Laurent coefficients a_{0..4}; true entries are their sums by residue j mod n, so examining all residues proves endpoint positivity for arbitrary cycle length. Positive factorizations handle distances zero/two/four; monotone cubics yield thresholds n=3,4,5 and unaliased or wrapped distance-three coefficients yield n=6:1/2, n=7:4/7, n>=8:1/2. Fourier largest Laplacian eigenvalue Λ_n gives spectral cutoff β/Λ_n, equal to positivity only n=3,4. Independently expanded all shift coefficients symbolically for n=3..9, checked mass conservation, critical cubics and distance-three aliases. The analytical residue/monotonicity proof handles all n; finite symbolic instances are checks only.

## originality

FAIL

The published October 13 complete path/cycle theorem gives all identical positive-step intervals, including all exceptional cubic roots and no-reentry, for exactly the same periodic heat generator. This source was read in full; stronger prior coverage is decisive.

## value

FAIL

The complete natural exact table is mathematically useful but has already appeared in an earlier theorem that covers a strictly larger graph family. Recomputing the same table and adjoining a textbook Fourier/spectral-radius comparison does not establish separate value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
