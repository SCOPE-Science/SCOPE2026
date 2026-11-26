---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For any super dominating set, a private leaf and its core cannot both be omitted. Every omitted core in A is witnessed by its selected leaf; every omitted leaf at a core in B needs that core as witness, so it cannot have any adjacent omitted core. Thus the allowed omitted sets are precisely nonconflicting choices. They are downward closed and inclusion-minimality of the selected set is maximality of the omissions. An empty pair at v can add an omitted core iff v has no B-neighbor, and can add an omitted leaf iff it has no A-neighbor. This establishes both directions of the classification, including isolates and disconnected bases. On a cycle the E's are isolated, and every E flips the occupied type across it. Therefore their number is even, say 2j, and the 2j remaining positive runs alternate, requiring 4j<=n. Marking one separator gives n labelled choices, two choices of first type, and binom(n-2j-1,2j-1) ordered run compositions, divided by 2j possible marks. The zero-separator case gives the two constant words; it includes n=3, with no positive j. The resulting support, maximum size and all four residue formulas follow by substitution. A bounded replay from the witness definition agrees, including the C_8 counts 2,40,4 at sizes 8,10,12.

## originality

FAIL

An older pendant-corona result already gives the exact allowable omissions on every base; the new-looking two-neighbor condition is saturation of those omissions. More importantly, the entire cycle size distribution reduces exactly to earlier enumerations in other formulations: the odd sunlet rows are the reflected independent-domination polynomial of odd-rung Möbius ladders; the even rows are a change of parameter of the established mixing-number distribution for integrated cycle colorings. This also covers the upper cardinality and every claimed optimizer multiplicity. The obstruction is mathematical prior coverage, not an inaccessible source or a flaw in the formulas.

## value

FAIL

A size-refined classification for this natural family would intrinsically be useful, but all of the claimed new census and extremal information is already accessible through exact earlier results. The remaining all-base local test is an immediate maximality reformulation of the known allowed omissions; it does not add a nonroutine structural or enumerative consequence. A credit correction alone would not leave a distinct valuable theorem to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
