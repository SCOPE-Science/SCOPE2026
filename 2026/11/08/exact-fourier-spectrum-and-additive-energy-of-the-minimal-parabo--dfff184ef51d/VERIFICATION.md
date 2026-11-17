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

PASS: The x≠0 vertical fibers of K={(x,x²−s):s a square} plus the complete fiber at x=0 have size (q+1)/2 and q, respectively; tangent lines y=2tx−t² furnish every nonvertical direction. The indicator Fourier transform separates a quadratic Gauss sum over x and square-residue sum over s; subtracting the incomplete x=0 contribution and adding the full fiber yields the stated v≠0 coefficient, and v=0,u≠0 yields (q−1)/2. The Gauss identities G²=eta(-1)q and a_v sum z=q imply the claimed v≠0 fourth-moment sum, split by q modulo 4 and eta(2), with orthogonality sum |hat1_K|⁴=q²E(K). The two explicit polynomials follow; their q^-1 uniform bias upper bound comes from |G|=sqrt(q) and the exact set size. Independently constructed K and exact ordered pair-sum energy over q=3,5,7,11,13,17: all six matched the claimed integer polynomials; the all-prime-power theorem relies on the algebraic proof.

## originality

PASS

PASS for the full all-odd-prime-power spectral/energy theorem, with explicit prior-coverage subtraction. Blokhuis–Mazzocca already establish minimal cardinality and geometric model; Fraser proves some Fourier-decaying measure exists on any Kakeya set, not the transform of its uniform measure. The November 8 published four-level spectrum of the same quadratic-tangent Kakeya set, after x-coordinate scaling, covers all q=3^m with m odd >=3: this covers a NONTRIVIAL subfamily and is not credited anew. Its theorem does not address fields q≡1 mod4, q≡3 mod4 outside characteristic three, or the all-q piecewise eta(2)-sensitive energy polynomial. The surviving exact arithmetic fourth moment for every odd prime power is a distinct natural invariant, although a disguised old Gaussian-period identity may exist.

## value

PASS

PASS: The exact additive energy (ordered quadruple count) is a natural additive-combinatorial invariant of the extremal minimum-size planar Kakeya configuration, with uniform-measure Fourier decay and a full complex transform rather than merely existence of a favorable weighting. The dichotomy by q mod 4 and eta(2) measures arithmetic changes in fourth moments beyond known cardinality and some-measure Salem bounds, across an unrestricted infinite family. It is a self-contained motivated exact calculation, not a single arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
