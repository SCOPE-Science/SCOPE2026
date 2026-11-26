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

The parity label in the paired lift is δ_j≡j−π_j mod 2, so A=Σδ_j is even. The inversion degree at j is π_j−j+2L_j; counting the endpoints of differently labeled inversion edges shows B≡Σδ_j(π_j−j)≡A≡0 mod 2. For pairs internal to the two halves equal labels double the base inversion status and unlike labels contribute once, giving 2(I_q−B)+A(q−A). For cross-half pairs, two labels 1 contribute A² and unlike labels contribute exactly once per unordered pair, for another A(q−A), hence Aq. The combined correction −2B+A(2q−A) vanishes mod 4. The odd-modulus sign character, the bijection of unit groups and character orthogonality then give the stated square/nonsquare sums, residue counts and cyclotomic conclusions for any odd q≥3.

## originality

FAIL

The exact pointwise congruence is an elementary specialization of the known inversion reciprocity and Jacobi-sign formulas; this is stronger evidence than the previously conjectured root criterion. The frozen counting proof differs, but the Finding's mathematical conclusions are already covered by those formulas.

## value

FAIL

The cyclotomic question is motivated, and the paired-lift proof is correct. Nevertheless the stated narrow exact invariant and its distribution are mechanically deduced by the two reciprocity substitutions and the standard supplementary law. No further independently motivated structural theorem on parity-preserving lifts is stated or established as a separate valuable contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
