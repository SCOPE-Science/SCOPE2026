---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For each n>=4 and Hamming weight residue r, the complete quadratic Walsh Gram has entries m_|I symmetricdifference J| under the uniform *conditional* mask probability, with the exact mod-three root-of-unity m_j and m_3=-3m_1,m_4=-3m_2. Permutation-isotypic decomposition gives the stated 3x3 trivial T, 2x2 standard S repeated n-1, and scalar 1-5m_2 repeated n(n-3)/2; multiplicities sum to 1+n+n(n-1)/2. For each representation type, restriction to selected shells has Vandermonde rank min(3,h0), min(2,h1) or min(1,h2), respectively, giving exact rank and the exceptional (n,r)=(7,2) null polynomial (W-2)(W-5). Full independent mask enumeration and numerical Gram eigenvalues for n=4..8 and r=0,1,2 reproduce every block eigenvalue and rank. The exact conjugacy for paired residues and exponential moment estimates prove the two asymptotic squared condition ratios; no finite range is claimed as a universal paired-optimality threshold.

## originality

PASS

Qualified originality for the complete *three*-residue degree-two sampling design, particularly paired nonsymmetric masks and their threshold/asymptotic comparison. The previously published degree-two spectrum of the sign-sum-zero residue and the general rank/slice machinery are explicitly excluded from novelty.

## value

PASS

Fourier sampling by Hamming-weight congruence class is a natural symmetric Boolean sampling design. The full quadratic band is the first one with nontrivial pair harmonics, and determining which masks recover it injectively plus relative sharp noise conditioning is substantive. The two-at-n7 boundary, three-block spectrum and paired-versus-third asymptotic are independently meaningful beyond the known one-class and degree-one specializations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
