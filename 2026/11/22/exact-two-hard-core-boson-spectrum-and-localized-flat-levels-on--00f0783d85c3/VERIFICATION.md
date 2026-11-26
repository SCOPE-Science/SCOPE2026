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

The unordered-pair hopping matrix is precisely token-graph adjacency with weight one. On each pair of distinct petals the internal hopping is the sum of the two leaf swaps; its tensor sign modes have eigenvalues 2, 0, 0, −2. The double-odd modes decouple. At each petal the single-odd sector is a star of m−1 cross-petal modes coupled to the odd hub-pair mode with weight √2, with central diagonal −1; its contrasts and two-dimensional block give the zero modes and the quadratic. The even sector couples the hub-pair modes both to same-petal pairs by √2 times the identity and to cross-petal modes by √2 times unsigned incidence B. BBᵀ=(m−2)I+11ᵀ has eigenvalues m−2 and 2(m−1), with multiplicities m−1 and 1. Each singular direction of squared singular value s yields (λ−2)(λ²−λ−2)−2sλ, and ker B yields the stated +2 factor. These blocks exhaust the space. Compact eigenvectors use a double-odd cross mode, differences sharing the odd petal, and an alternating four-cycle in ker B, respectively; the last needs m≥4 and +2 is absent at m=3. The explicit flat blocks have the stated dimensions, not necessarily the total multiplicities after accidental coincidences; the other blocks carry mass 5m/[m(2m+1)], which vanishes for bounded continuous tests.

## originality

PASS

The distinct claim supported by the accessible statements is the complete adjacency spectrum of this two-particle family, with explicit compact states and the adjacency level-counting limit. Neither the token/symmetric-power identification nor the incidence method is new. The closest reported same-object result concerns the combinatorial Laplacian; full text was unavailable and the possible scope of its block calculation is a named risk, not negative evidence.

## value

PASS

This is a full exact invariant across a natural highly connected family for which the hard-core condition prevents reading off the energies from the one-particle modes. The computation identifies an extensive flat-state component, with bounded configuration support witnesses and a precise limiting density, not merely a small spectrum or a reformulation of token adjacency.

The dated certificate retains the supplied scientific assessment, sources and limitations.
