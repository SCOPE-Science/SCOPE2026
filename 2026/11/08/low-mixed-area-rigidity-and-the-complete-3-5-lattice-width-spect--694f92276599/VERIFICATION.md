---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

After a unimodular change of direction, every pair of lattice extreme-height chord vectors has determinant divisible by d, and its absolute determinant is at most V(P,Q). For V<d all such chords are parallel. Their integer multiples of a common primitive vector are at and bt, with t a positive integer by coprimality. An off-line lattice vertex of P would give perpendicular integer width at least one, hence V>=bt>=b. Thus P is a segment; positive V forces Q to be two-dimensional and V=at times an integer width. The determinant comparison covers every pair of extreme vertices and thus every extreme-height chord, including endpoints drawn from entire support faces. Parallel segments realize zero and the supplied triangles realize every permitted positive multiple of a. For the 3:5 section, in coordinates (x,y-dx) the semigroup base polygons have mixed area 3r1+5r2 by the lattice edge support formula (also valid in the segment cases by the segment formula). The same shear makes the four-edge P witness for 7 have support contributions 0,5,2,0 from Q. Lattice edge support also ensures integral mixed area. The small 1, 2, and 4 witnesses and the strict low-area exclusion cover all missing semigroup values, including both sides of d=5. Frozen verification reports 22,198 finite checks, not the 22,200 asserted in RESULT.md; this is a nonmaterial reporting discrepancy. The uploaded checker was inspected, not executed, and the proof does not depend on its count.

## originality

PASS

The strongest comparison establishes exact prior coverage at d=10, prior semigroup realizations, and direct derivability of the all-d value-7 witness. It does not establish the generalized strict-window divisibility and rigidity, or the full parameter-dependent spectrum and sharp onset of the hole at 4. Those are the distinct contributions supported here.

## value

PASS

The strict-window result gives geometry, not just a list of values: it forces dimensional collapse of the smaller-width polygon and explains the divisibility obstruction for arbitrary coprime width ratios. The 3:5 section resolves a natural family extending a published exact case and identifies where the persistent hole at 4 begins, without requiring a catalogue of all area-four pairs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
