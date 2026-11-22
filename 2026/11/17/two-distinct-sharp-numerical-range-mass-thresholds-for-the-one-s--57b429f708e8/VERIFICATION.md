---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Fourier transformation sends the bilateral shift to a multiplication symbol F(k)=M sigma3 + (c sin k-ic(1-cos k))sigma1. The Hermitian support matrix has eigenvalues ±sqrt(M²cos²theta+c²(sin(k+theta)-sin theta)²). Maximization over k gives the exact 1+|sin theta| factor. With s=|sin theta|, Q(s)=M²+c²+2c²s+(c²-M²)s²; its extrema yield w=2c for M<=sqrt2 c and M²/sqrt(M²-c²) above, while min sqrt Q is sqrt(M²+c²) below sqrt3 c and 2c above. h has directional corners only at theta 0,pi, giving two vertical nondegenerate faces at x=±sqrt(M²+c²) of half-height c²/sqrt(M²+c²). Frequency values attaining the Hermitian support occur on a measure-zero set, so no boundary point belongs to the actual numerical range; convexity then gives its open interior. Independent 60,001-point s-grid optimization at c=.7,1 and masses crossing both thresholds reproduced all extrema to <1e-7; the proof, not this grid, covers all masses and angles.

## originality

PASS

Best-of-knowledge finding after comparing actual statements and consequences, not titles. The four structured checks and specific full/partial source inspections below separate previously known inputs from surviving contributions.

## value

PASS

The complete numerical-range geometry (not just operator norm or spectrum) for a physically motivated nonnormal lattice Dirac discretization. Two sharp and different mass thresholds, exact flat faces, and boundary nonattainment are natural operator-theoretic invariants and are nontrivial explicit optimizations beyond the general matrix-symbol numerical-range principle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
