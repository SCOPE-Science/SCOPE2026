---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The full four-row Fourier synthesis matrix is Parseval. Subtracting the erased-column contribution gives λ_min(S_E)=1−λ_max(Φ_E*Φ_E). Removing the diagonal phases gives NΦ_E*Φ_E=4I+B_E up to conjugacy, where the off-diagonals are the signed r_d evaluated on actual increasing-label differences. For the consecutive candidate, the odd eigenvector gives −b_N and the even sector gives x²−b_N x−2a_N²=0. Its positive root is the largest: b_N≥0 for N≥8, and at N=7 the independent certificate gives −b_N<2.91<β_N. For N≥11, r_2>6/5 by the cosine bounds in the proof; the positive main-lobe product 4 cos t cos(2t) decreases up to π/4, and the magnitude in the sidelobe is at most 8/(3√6), obtained by maximizing 4u(1−2u²). At N=10, r_2=1 and the remaining circular distances have magnitudes <1, 1, 0 for d=3,4,5 respectively. A nonconsecutive triple has at most one adjacent pair. Taking entrywise magnitudes in the Rayleigh quotient and comparing with the positive-off-diagonal matrices with entries (a,b,b) and (a,a,b) proves a strict Perron inequality since a>b>0. For N=7,8,9 an independent rational computation on unordered cyclic gap triples certifies s<6.34,8.01,10 and β_N>2.91,3.69,4.34 respectively. Here s is the sum of the three squared off-diagonals; trace zero and Cauchy–Schwarz on the other two eigenvalues give λ_max(B_E)²≤4s/3. The three strict rational gaps verify uniqueness in those orders. The Vandermonde property of any four retained columns proves the bound is positive, and the consecutive triple has exactly N distinct translates.

## originality

PASS

The checked evidence supports a distinct exact all-N comparison of the top erased-block singular value for four fixed consecutive frequencies and three arbitrary cyclic sites. Earlier or separate sources cover closely related erasure criteria, contiguous blocks, or the same minimax lower-bound theorem with fewer frequencies; none of the checked statements supplies this four-frequency optimization with its signed sidelobes and exact equality cases. The most plausible inaccessible finite erasure table is a named remaining risk, not evidence of either coverage or noncoverage.

## value

PASS

This gives a sharp adversarial stability guarantee for a natural lowpass sampling frame: an exact lower squared singular value usable under three arbitrary losses, and a characterization of every worst mask. The normalization and the equality cases matter for comparing sample geometries. The four-frequency sidelobe and the separately certified small cyclic orders make this more than replacing a parameter in a three-frequency result or computing a single known contiguous block.

The dated certificate retains the supplied scientific assessment, sources and limitations.
