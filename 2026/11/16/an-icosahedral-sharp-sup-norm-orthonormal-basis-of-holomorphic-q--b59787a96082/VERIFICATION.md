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

On the probability-normalized complex unit sphere of C³, the fourth-moment identity gives ||zᵀMz||²_2=tr(MM*)/6 for symmetric M. Takagi factorization gives ||zᵀMz||∞=||M||op; for unit L² this is at least sqrt(tr(MM*)/3)=sqrt2, with equality exactly for M=sqrt2 times symmetric unitary. The six real unit axes from antipodal vertices of an icosahedron have exact pairwise squared overlap 1/5. With ξ=(-7+i√15)/8, |ξ|=1 and Re ξ=-7/8, U_v=I+(ξ-1)vvᵀ are symmetric unitaries and tr(U_v U_w*)=0 for v!=w since 3+2(Re ξ-1)+(2-2Re ξ)/5=0; diagonal Gram trace 3. Their six quadratic forms form a complete orthonormal basis and every member attains sqrt2. An independent exact symbolic golden-ratio overlap check and the package finite numerical checker corroborate the explicit matrices; the universal lower bound is analytic.

## originality

PASS

General Rudin-problem bounded ONB constructions neither assert the minimax √2 for the fixed six-dimensional quadratic space nor supply six icosahedral symmetric-unitary orthogonal matrices. The algebraically natural ETF reflection construction yields the exact sharp answer, with older matrix-frame equivalence as priority risk.

## value

PASS

An intrinsic, sharp finite-dimensional instance of the uniform bounded homogeneous basis question: exact minimax for the six-dimensional quadratic component and explicit simultaneous attainment. The equality geometry of symmetric unitaries and icosahedral equiangular axes is substantive, not just a low-cost numerical constant or a renaming of a general asymptotic existence bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
