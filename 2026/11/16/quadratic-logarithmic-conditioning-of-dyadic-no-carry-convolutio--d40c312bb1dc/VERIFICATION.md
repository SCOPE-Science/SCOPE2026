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

Every allowed binary digit pair is (0,0),(1,0),(0,1), so the cyclic Fourier coefficient factors over j as ∏(1+ζ^(2^j u)+ζ^(2^j v)). For a power-of-two M, any two Mth roots z,w satisfy |1+z+w|≥||1+z|−1|=|2cos(πt)−1|≥3|t−1/3|≥1/M; the concavity/chord and tangent estimates cover t∈[0,1/2], and 3∤M ensures separation. Thus σ_n≥2^{−n(n+1)/2}. The explicit conjugate frequencies u_n=(2^n−(−1)^n)/3,v_n=−u_n modulo 2^n are simultaneously within 1/(3·2^(n−j)) of primitive cube-root cancellation at each digit scale; Lipschitz bound 4π gives σ_n≤(4π/3)^n2^{−n(n+1)/2}. Triangle inequality makes max multiplier 3^n, so κ=3^n/σ and log2 κ/n²→1/2. Does not prove exact finite minimizers.

## originality

PASS

PASS best-of-knowledge for the quantitative n²/2 logarithmic conditioning coefficient and explicit two-sided bounds, not for qualitative zero-freeness. The primary Lam–Leung theorem implies no odd-weight 3-term sum of 2-power roots vanishes, and Fourier digit factorization is standard, but neither states the scale-by-scale lower modulus or an all-digit simultaneous cube-root near-cancellation witness. Resultary semantic search located the current record and unrelated finite convolution spectra, not a dominating same dyadic no-carry bound.

## value

PASS

PASS: No-carry pairs form a canonical binary/Sierpinski digit set and invertibility is insufficient for stable recovery. Its exact quadratic-exponent condition growth exposes a sharp asymptotic obstruction to cyclic convolution inversion, supported by genuinely uniform dyadic separation and a matched explicit near-extremal family. This is stronger than an elementary nonzero-multiplier observation; no exact finite minimizer is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
