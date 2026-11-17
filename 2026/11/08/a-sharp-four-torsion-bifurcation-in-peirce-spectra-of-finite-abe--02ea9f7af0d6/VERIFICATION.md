---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Fourier transform of e_x e_y=e_(2y−x) gives (vu)^∧(ψ)=v^(ψ^(−1))u^(ψ²). For idempotents cψ=cψ⁻¹ cψ², inversion-paired nonzero Fourier coefficients form 2x2 matrices [[0,cψ²],[cψ⁻²,0]] whose offdiagonal entries vanish together or are both nonzero; hence each is diagonalizable, including self-inverse scalar blocks. If no order-4 element exists, squaring on odd-character subgroup permutes finite cycles; idempotency forces products cηcη⁻¹∈{0,1} and all eigenvalues in {0,±1}. Explicit basis and uniform idempotents attain {0,±1} when odd order exists; exponent-2 core has trivial quandle and only eigenvalue1. Order-four character χ gives idempotent uλ=|G|⁻¹Σ(1+λχ²(g))e_g with spectrum containing ±λ for arbitrary complex λ. Independent exact arithmetic checked cyclic examples Z2,3,4,5,6,8 and complex λ values; this is finite corroboration, not an all-groups proof.

## originality

PASS

Zhang 2026 establishes odd-order three-point Peirce spectrum and Fourier product; Kaur–Singh 2023 handles representation decomposition for even abelian Takasaki quandles but its irreducible module decomposition is not itself the union over every complex idempotent spectrum. This theorem adds elementary two-primary mixtures and complete four-torsion threshold with whole complex spectrum and uniform diagonalizability. Two plausible same-family 2026 Fourier/idempotent manuscripts remain inaccessible in full and may contain the classification. Best of knowledge O PASS qualified; no inference of full-document noncoverage from abstracts.

## value

PASS

A simple group-theoretic four-torsion condition exactly determines whether the Peirce spectrum jumps from finite three-point set to all complex eigenvalues, while every operator remains diagonalizable. This is a natural complete classification of a Peirce invariant across finite abelian core quandles and clarifies the role of non-Latin even cores and the distinction between different torsion types.

The dated certificate retains the supplied scientific assessment, sources and limitations.
