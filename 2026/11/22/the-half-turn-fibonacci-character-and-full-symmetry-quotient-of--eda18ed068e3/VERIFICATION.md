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

Chandrakar et al., arXiv:2611.18058v1 §3 and Thm. 3.5, independently checked in the primary PDF, give exactly the required Cartesian grid, perfect-matching facets, and homology rank F_(n-1) in degree n-1 for n>=2. In the augmented Lefschetz sum the sign of the permutation of a fixed face and its degree sign combine to minus (-1)^(number of edge orbits), including the empty face. The strip state records the selected incoming edges and the set of all feasible incoming masks of disjoint complementary matchings; one column exhausts the possible residual vertical choices and forces the outgoing complement. Keeping a set, rather than counting completing matchings, ensures each eligible face is counted once. At the central cut the existence of a common completion containing the chosen central subset is exactly the gluing condition: intersect Q with its row reversal for the half-turn and use Q itself for the column reflection. For row reversal both vertical edges would intersect if selected as an orbit; only rows {1} and {0,2} give horizontal selections. An independently written integer replay (`python3 /workspace/checks/grid.py`) recovered 24 states and 112 weighted transitions on the half strip, 8 and 16 on the row transfer, and zero recurrence errors at all 24 and 8 required starting indices. Cayley–Hamilton extends these checks to all widths. Initial values fix the displayed solutions, including F_(-1)=1 at n=2. Separate enumeration of fixed subfaces gave (row,column,half) = (-1,1,-1), (-1,-1,1), (0,0,2) for n=2,3,4. The four character averages follow from the sign projectors. On barycentric subdivision, a stabilizer of a simplex fixes it pointwise and preserves its dimension-ordered orientation. Quotient cellular chains identify with coinvariant chains, which over Q are exact and equivalent to invariants. Thus the quotient is the actual geometric quotient and the first nonzero reduced rank is one at n=4. No assertion of integral quotient homology or homotopy type is needed.

## originality

PASS

The supported distinct contribution is the all-width half-turn trace on the perfect-matching-extendible subcomplex and the consequent joint rational character and geometric quotient homology. The row and column traces, nonequivariant rank and width-four boundary value are credited. No inspected statement determines the new all-width trace; unavailable sources leave a bounded priority risk.

## value

PASS

Two natural axial traces miss the joint action even in a very small member of this canonical strip family. The missing trace grows without bound, and knowing it determines both the whole rational symmetry module and the homology of the simultaneous geometric quotient at all widths. The main contribution is the trace calculation, not the standard projection rule.

The dated certificate retains the supplied scientific assessment, sources and limitations.
