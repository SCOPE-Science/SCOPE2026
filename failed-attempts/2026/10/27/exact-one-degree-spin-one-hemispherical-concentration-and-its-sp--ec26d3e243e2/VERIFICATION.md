---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

At fixed ℓ, longitudinal orthogonality diagonalizes the compressed operator. For the stated eth convention the integrand is the square of −U′+mU/sinθ, where U is the real polar factor. Reflection splits the two even terms in half, and the cross term contributes −2πm U(π/2)²/[ℓ(ℓ+1)] for m≠0 because U vanishes at the pole. The equatorial Legendre formula gives the two central binomials. The consecutive same-parity ratios are strictly less than one in the downward direction, hence the extrema are simple and the central multiplicities follow by counting positive orders. The next shift is zero at ℓ=2 and is Dℓ(ℓ−2)/(2ℓ−1) at ℓ≥3. The orthonormal expansion yields the sharp deficit constant and equality sectors. At ℓ=1 the direct integrals of (1±cosθ)² give the complete spectrum (7/8,1/2,1/8); the proof's final sentence in line 76 should say 'second eigenvalue', not 'only other eigenvalue'. The finding and gap are correct. Reversal of the spin convention means reversing helicity, not multiplying eth by an overall minus sign. Replay: RESULT.md lines 46–78; check.py lines 13–86 and frozen verification_output.txt document 120 exact integrals, 868 numerical/trace checks and 1198 finite rational checks (inspected, not rerun).

## originality

FAIL

A distinct, accessible Resultary theorem on the full tangential exact-degree space gives the same equatorial shifts, their order, eigenpolarizations and degree law. The frozen spin-one claim is its invariant helicity restriction, including the unprinted gap by a single ratio. This is verified coverage, without asserting publication priority between same-day records.

## value

FAIL

The sharp concentration question and spectral stability constant are natural and useful in isolation. Here the extra single-helicity formulation and unprinted gap follow mechanically from the exact known full-tangential decomposition and its ordering, so this record does not add an independently valuable exact invariant under the review standard. No genuinely distinct repair is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
