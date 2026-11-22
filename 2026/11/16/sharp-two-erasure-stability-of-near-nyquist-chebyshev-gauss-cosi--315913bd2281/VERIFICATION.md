---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The N×N probability-normalized DCT-II is orthogonal. Complementing its N−2 retained degree columns and two omitted rows reduces the surviving squared spectrum to N−4 unit eigenvalues and the two eigenvalues of the explicitly given 2×2 highest-cosine block B. Squared Frobenius norm and squared determinant of B give T_{jk}=(2/N)Σ sin²θ_i(1+4 cos²θ_i) and D_{jk}=16 sin²θ_j sin²θ_k(cosθ_j−cosθ_k)²/N²; strict cosine monotonicity proves invertibility. For N≥5 the D/T lower comparison, spacing inequalities for all other adjacent/nonadjacent pairs, and the edge-pair upper Rayleigh bound prove precisely two reflected endpoint-neighbor minimizers. The six pairs at N=4 are checked separately by exact radical values. Taylor expansion T*=25π²/N³+O(N^-5), D*=9π^8/N^10+O(N^-12) yields λ*~9π^6/(25N^7). The ordinary condition number is the square root of the stated squared-condition ratio. Independent local Python reconstructed all 451 sampled DCT/complimentary spectra for N=4..14 and both minimizers without depending on saved run logs.

## originality

PASS

The exact N-dependent worst singular eigenvalue and unique Gauss-grid two-erasure patterns are not established by the inspected related DCT-I Chebyshev–Lobatto theorem or by the open generic gap-filling article. General Fourier-submatrix SVD identities supply the complement method but do not, as inspected, settle the strict all-pair minimizer or seventh-power constant. The nearest 2021 DCT interpolation full text was inaccessible through authorized routes: this is a concrete priority risk, not evidence against originality.

## value

PASS

Loss of exactly two quadrature observations at the near-Nyquist sampling limit is a natural polynomial reconstruction stability question. Every pair is recoverable but worst endpoint-neighbor loss has a sharp seventh-power squared conditioning blowup, determining design-sensitive robustness and an exact universal extremizer within the model. The nontrivial all-pair comparison and exact coefficient are more than a routine determinant calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
