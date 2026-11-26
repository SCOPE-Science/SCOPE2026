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

The unitary transform in the two-site cell index gives the stated blocks. Their determinants are (ab/2)(cos(2π α)−cos(2π k/q)) in the supercritical regime. The leading coefficient and roots with multiplicities of T_q−1 give the exact determinant, including its sign. Each vanishing block has rank one; the two interior resonant frequencies are distinct, whereas the critical case has just k=0. Subcritical block determinants stay ≥1−a−b. The largest singular value is attained at k=0 by entrywise monotonicity after removing phases. At either zero the determinant has slope magnitude πab sin(2π α) and the other singular value tends to √S_*. A nearest sample gives an O(1/q) upper bound on the minimum, so every minimizing sample lies within O(1/q) of a root by the local two-sided linear bound and compactness away from the roots. The relative Taylor error there is O(1/q), even when the nearest distance is unusually small. This gives exactly the stated constant and the three approximation regimes. Transposition preserves all singular values.

## originality

PASS

The independently supported distinction is the exact all-grid inverse-conditioning law and rank-loss classification for this positive, genuinely two-periodic finite blur. Neither Fourier block diagonalization, Chebyshev products nor the Diophantine mechanism in deconvolution is new on its own. No inspected distinct source states or implies the full finite-grid law and its sharp Euclidean constant for this family.

## value

PASS

For an elementary positive local blur, invertibility at every finite size does not imply even a polynomial conditioning bound. The result identifies the fixed phase that decides which resolutions are unusable and gives the sharp perturbation scale on the others. This is a useful explicit benchmark separating inverse-conditioning pathologies from one-step amplification and from FFT implementation effects.

The dated certificate retains the supplied scientific assessment, sources and limitations.
