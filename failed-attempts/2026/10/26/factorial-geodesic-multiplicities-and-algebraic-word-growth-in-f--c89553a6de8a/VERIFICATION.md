---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Deleting an edge gives a cut crossed at least once for a trunk edge and at least twice otherwise, by coverage and parity. The bound is attained by completing every attached subtree during its sole out-and-back excursion and moving once along the trunk. Equality forces precisely this form. At each vertex the independent choice is the order of its children after excluding the trunk directions or parent edge; the first changed order changes the word because outgoing Cayley labels are distinct. This proves the factorial product and includes the single-vertex tree. For R and L the maximum available distance is the rooted eccentricity (inversion reverses the order and inverts the letters); for D it is the diameter. Ordered diametral pairs label different normalized elements since a left translation preserving a finite nonempty free-group vertex set would have finite order and thus be the identity. Summing disjoint word sets gives the class formulas. For the series, q possible first trunk steps, p choices per further step, p endpoint side directions and p-1 internal side directions give the displayed geometric series; each off-trunk edge contributes u². Formal recursion fixes coefficients from earlier degrees and proves algebraicity, with no ambiguity at r=1 where p-1=0. I independently enumerated rank-two words through length eight by updating the freely reduced prefix and testing n=2(number of visited vertices-1)-endpoint distance; this gave (1,4,16,60,228,840,3132,11496,42528). This bounded replay is corroboration, not the proof. The frozen script was inspected, not executed.

## originality

FAIL

The earlier Bodart–Carvalho–Monteiro arXiv v1, Theorem 6.1, provides an exact grammar for the same set of word strings, with recursion on the allowed first directions of ordered idempotent branches and a separate reduced-path state. This is stronger than a mere assertion of context-freeness. Its direct weighted translation, after deleting one redundant empty production, is precisely Theorem B. Restricting those same productions to a fixed Munn tree gives the individual factorials in Theorem A, and the known class minima then give the class sums. The exact formulas need not be printed in the prior paper for the mechanical implication to apply.

## value

FAIL

The two expressions are clear enumeration aids and correctly distinguish words from elements. As submitted, the quantitative statements are the immediate fixed-tree and length-weighted translations of the previously available excursion/path grammar, plus sums at independently known class minima. There is no additional unknown extremum, asymptotic, or other distinct exact invariant that could survive as a valuable repaired claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
