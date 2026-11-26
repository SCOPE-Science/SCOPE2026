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

At an unselected cell the selected-neighbor count is exactly the row occupancy plus the column occupancy. It is one precisely when that cell meets an empty line and a line occupied once. For p,q>=2, the four support cases (neither dimension has a vacancy, column vacancy only, row vacancy only, both have vacancies) therefore require at least q, 2p, 2q and 4 cells respectively. In the last case equality leaves exactly two occupied rows and columns and fills their four intersections. For q<=3 only full support can be minimal; the labeled onto assignments from columns to rows give counts 2, 6, 6. For q>=4 a rectangle attains four. For p=2 any independent pair of choices of two cells per row is valid, with or without column vacancies. A four-cell fort outside that class must occupy all columns, so q=4 and both rows must be occupied; the 1+3 and 3+1 row splits give exactly eight extra. For p>=3 any four-cell fort with vacancies is a rectangle; full support requires q=4 and gives 36 surjections at p=3 and 24 permutations at p=4. For p=1 the graph is K_q and every pair, but no singleton, is a fort when q>=2; the lone vertex at q=1 is a fort. The stated growth rates follow from these exact formulas. The bundled exact checker and recorded output were inspected, not run. They are consistent with the unrestricted support proof.

## originality

FAIL

The equivalent maximum failed zero-forcing classification in indexed record 5cfd0c4c21bc gives the same sizes, counts and every shape on 2<=p<=q. Its later record date does not establish priority in either direction; it does establish equivalent coverage. Moreover, the earlier all-fort polynomial record 10cceec37c9c gives the same row/column support lemma and an exact polynomial covering these counts, explicitly stating the rectangle coefficient in the large-board regime. The generic scalar minimum was proved in the failed zero-forcing literature. For p=1 the frozen statement adds only the complete-graph singleton and pair cases.

## value

FAIL

Minimum fort obstructions and the thin-board change in the enumerating degree are mathematically natural. As a separate contribution, however, the frozen exact invariant is obtained from the earlier occupancy enumerator, and its labeled extremizer census and shape distinction are also explicitly covered by the complementary indexed theorem. The complete-graph one-row cases and asymptotic restatement leave no distinct substantial result in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
