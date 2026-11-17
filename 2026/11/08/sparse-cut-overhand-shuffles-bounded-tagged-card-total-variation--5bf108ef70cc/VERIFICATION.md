---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The original package contains a false exact bulk identity: it subtracts (-1)^k q_n^(n+1) instead of (-1)^k q_n^n from Jiang’s eigenvalue. Algebra leaves a nonzero term of size O(n^-1) in the old identity. The complete replacement RESULT.md now sets b_n=q_n^n and proves exactly lambda_{n,k}-(-1)^k b_n = p_n^2(1-(-1)^k b_n)/(p_n^2+q_n ell_{n,k}). This repairs the uniform bulk estimate, retaining the correct n exp(-2ct)+o(1) theorem. Independently checked the exact kernel, symmetry, Doeblin minorization and cosine eigenvalues for n=4,7,16,31 and three cut intensities; this confirms finite identities, not the infinite limit. The corrected low/bulk proof bounds low modes by n^alpha r^{2t}=o(1) and the bulk by O(k^-2), uniformly in starts and integer times.

## originality

PASS

Jiang supplies the complete exact one-card spectrum, an indispensable acknowledged input, but its stated full-deck cutoff is in the fixed-p regime. The corrected finding establishes a separate, uniform p_n=c/n singular chi-square window and a Doeblin-vs-chi-square mixing separation. Jonasson proves fixed-parameter whole-deck bounds, not this two-metric one-card limit. The finite spectrum makes the limit derivable but does not itself state or automatically justify the uniform low/bulk asymptotic. Best-of-knowledge originality is conditional on unaccessed primary sections.

## value

PASS

A natural high-dimensional Markov-chain separation shows uniformly bounded one-card TV mixing but diverging chi-square mixing with an explicit integer-time profile. The spectral low/bulk control is not a mere normalization or routine parameter substitution; both the metric contrast and exact window have identifiable probabilistic use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
