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

The direct exact Walsh test is wt(f+u·x) ∈ {6,10} for each u, since W=16−2wt. An independent enumeration obtains 896 functions, 448 of each support size, and confirms by binary Möbius inversion and polar-radical tests that each is a nonsingular affine quadratic. For every support, the exact trace set is {S ∩ supp(f)}; its cardinality reaches 2^|S| precisely on the proper ten-block subfaces. Independent checks validate all 512 witness entries, the entire f-vector, the seven-/eight-point exclusions, and the affine orbits of sizes 4480 for the nine-faces and 30, 840, 1920 for the unshattered eights. Both dimensions equal nine: the nine-face supplies a fixed-order tree, and any depth-ten complete tree needs 1024 distinct concepts, one per leaf.

## originality

PASS

The supported distinction is the classification of surjective coordinate projections of the full bent-function class, not the 896-concept census or the eight-point geometric orbit partition in isolation. The prior spectral classification shares the geometry and counts, but no inspected source establishes that the partition classifies traces of bent functions or supplies the nine-facet complex and its complete shattering counts.

## value

PASS

Four variables are a natural small setting for full-rank quadratic bent functions. The classification replaces all Boolean trace tests by an affine-block containment criterion, distinguishes two different small obstruction mechanisms, and explains why all maximal supports have one orbit even though many seven- and eight-supports fail. That is independently useful for studying projections of this canonical nonlinear code, beyond publishing a known concept count or a dimension bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
