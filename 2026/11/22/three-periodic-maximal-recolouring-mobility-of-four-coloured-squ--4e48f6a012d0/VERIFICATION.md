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

Each consecutive triple has three distinct letters. The next letter either returns to the oldest or switches to the fourth, giving exactly the stated tuple operations. An indexed bit word closes iff its position permutation is the identity; then there are 24 possible initial tuples. At a vertex only the fourth alternative to the two neighbor colors and current color can work, and the four neighbors use just two colors iff the two relevant moves were both returns. Closed walks with the previous bit in state therefore implement the degree count exactly, with no factor for rotation. A mixed word with k switches and r positive zero gaps has degree n−k−r. S is odd and R is even, so identity forces k even. Positive gaps may be reduced to 1,2,3 preserving closure, residue and r; independent finite multiplication reproduced the relevant 2-, 4- and 6-switch cases and the displayed table. The residue-1 optimum uses a run of four switches; the residue-2 optima use four isolated switches or two runs of three with every positive gap 1 modulo 3. Marking a switch in the former family, or a run in the latter, gives n·binomial(h+1,3)/4 and n(h−1)/2 distinct control words. The extra all-switch word maximizes only at n=8, and the all-return word uniquely maximizes when 3 divides n. This covers the boundary orders n=6,7,8 and all three residues.

## originality

PASS

The strongest match on the same graph is a frozen-coloring transfer which is exactly the zero-degree specialization in different state coordinates. Its three-class result also implies the residue-zero extremum by the elementary mobility criterion, and its eight-site fall count overlaps this audit's degenerate n=8 subcase. The distinct result is the sharp maximum and multiplicity beyond the known periodic/frozen cases, and the complete weighting beyond degree zero, not the state construction itself.

## value

PASS

The number of movable vertices is a natural local measure in a recoloring state space. The period-three obstruction and its two inequivalent defect patterns reveal how near-perfect mobility first becomes possible and how many indexed colorings realize it. The exact weighted enumerator also makes the rest of the degree spectrum accessible beyond prior frozen-state counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
