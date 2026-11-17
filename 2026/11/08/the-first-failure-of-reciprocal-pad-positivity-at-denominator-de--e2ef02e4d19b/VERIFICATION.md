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

The degree-five integer polynomial P_k has 5 simple roots isolated by 330 disjoint exact rational radius-10^-6 Rouche disks. For each k 0..65 the strictly smallest-modulus root is real positive with positive residue, and strict root/residue bounds guarantee its dominance for all n>=300. Independently recomputed 330 root centers using high-precision numerical candidates then checked all root-disk, simple-pole and tail inequalities using only exact rational bounds; the largest competing-pole/positive-residue ratio at n=300 was 0.3376494235153464<17/50. Separately evaluated 19,734 exact positive finite coefficients (n=1..299) and negative c_38(66,5). Thus the all-n statement uses a proven tail bound, not extrapolation of a finite run. The certificate script and data at exact pinned paths were inspected.

## originality

PASS

Fresh best-of-knowledge comparison for Reciprocal Padé positivity first fails at numerator order 66 for m=5: no checked stronger or equivalent prior statement implies the full scoped final claim. The source inspections are scoped to material actually read. Unindexed or inaccessible history remains explicitly a risk.

## value

PASS

Sharp first-failure order for a natural fixed-denominator instance of the Fasi-Higham reciprocal-positivity conjecture after its refutation is useful for locating the precise safe k-range. Ruling out any negative coefficient for 66 different rational denominators is stronger than searching finitely many n. The result does not claim a new negative witness, all denominator orders or matrix algorithm breakdown.

The dated certificate retains the supplied scientific assessment, sources and limitations.
