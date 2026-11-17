---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The fixed elliptic cubic E:y²z=x³−xz² is smooth and supersingular in characteristic19. The double cover defined by w²=xy+tz² has six simple branches exactly for t ≠0 and t⁴ ≠12; Riemann–Hurwitz gives genus4. Independently expanded the complete-intersection defining forms to exponent18 over F19 and extracted all sixteen Hasse–Witt coefficient-polynomials using the e_i exponents; matrix matches displayed two-row four-column support. Its sole potential 2x2 block has determinant −8t^6(t⁴−6)(t⁴−7). On the smooth locus rank is 2 outside eight simple roots and 1 at them, so a-numbers 2 and 3. At prime-field roots t=9,7, rank-one blocks have nonzero trace 1,4, hence stable Frobenius rank1; t↦−it fourth-root symmetry transfers to all eight geometric roots. Else block invertible and stable rank2. The universal geometric classification uses symbolic polynomials/isomorphism, not finite F19 sample extrapolation.

## originality

PASS

Ogasawara et al arXiv:2403.08139 provide complete-intersection Hasse-Witt formula and characteristic19 superspecial enumeration, not rank-one non-superspecial locus for this specified conic pencil. Chang et al arXiv:2502.09540 prove broad p-rank stratum dimensions and existence but do not calculate polynomial (t⁴−6)(t⁴−7) or a-numbers in the specified fixed-supersingular E pencil. Resultary prior searches for this equation/characteristic and equivalent Hasse-Witt degeneracy found no covering earlier record. Best-knowledge PASS with residual risk from hidden coordinate-equivalent old pencil.

## value

PASS

For a fixed supersingular j=1728 elliptic quotient, the conics xy+tz² define a natural equivariant genus-four family. Exact eight reduced coefficient parameters where geometric p-rank drops 2→1 and a-number rises 2→3, against a full smooth-parameter classification, give a motivated exact rank-stratification test case for bielliptic/Prym studies. This is a substantive family invariant, not arbitrary single-computation data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
