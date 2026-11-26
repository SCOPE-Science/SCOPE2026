---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The 120-line graph has A1=63·1 and A²=27I−6A+36J; on the complement of constants this gives roots 3 and −9, and trace and dimension give multiplicities 84 and 35. The stated projectors follow, including subtraction of (63+9)P0 in P3. Even degree gives a representative-independent kernel with three entry types; writing it in I,A,J gives precisely the three spectral levels. The raw probability-normalized Gram is h_l K_l, not K_l. Its adjoint kernel and inverse scaling cancel in the minimum-norm interpolant, leaving the reciprocal h_l in the squared-norm formula. The Gegenbauer coefficients follow by extracting terms from (1+z²)^(-3) and (1+z)^3/(1+z³)^3; the mod-three cases bound |b| by (2k+6)(2k+3)/6. The identity at k>=6 is exact: its two sides expand to 4k^5+30k^4+85k^3−920k²−3869k−3450. This certifies strict positivity and O(k^(-3)) closeness to the identity. Exact recurrence at l=0,2,4,6,8,10 gives ranks 1,35,84,119,120,119, with the sole missing constant sector at 6 and 10.

## originality

FAIL

Two distinct indexed findings explicitly cover the central reentrant rank classification and exact three-sector spectrum; the stronger one handles all exact degrees, including odd degrees on the 240 roots. The closest line record also proves strict diagonal dominance using the very same polynomial bound. Once the known spectral sectors and eigenvalues are given, the projector inverse and minimum-norm norm identity are standard pseudoinverse consequences and do not constitute a distinct surviving finding. These catalogue records have later recorded dates; equivalent coverage is demonstrated, but no historical priority or independent derivation is inferred. Earlier published work also explicitly gives the degree-ten mean obstruction, though not the full rank statement in the passages inspected.

## value

PASS

Single-degree harmonic interpolation on a canonical root configuration is a natural spectral question. The reentrant loss followed by permanent recovery and the explicit stable cutoff describe nonmonotone sampling behavior that is not captured by classical design strength alone. These mathematical merits are separate from whether an already covered statement adds a distinct result now.

The dated certificate retains the supplied scientific assessment, sources and limitations.
