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

The enumeration may restrict to antichains since a containment would violate the triple condition for any family of size at least three. Independently enumerating target sizes 8 and 7 with pair-compatibility bitsets gives zero and 31, respectively. Each step selects the least remaining mask or advances past it, and, for each previously selected A and new B, removes any future C contained in A∪B or containing either A∖B or B∖A. These are precisely the three violations; pruning for insufficient remaining masks is safe. Exhaustion at size 8 excludes all larger families. The replay checked the seven singletons, 30 Fano systems, exactly one occurrence of each point pair in the triple systems, and the full permutation orbit and stabilizers. There is also a direct proof: for an antichain with at least three members satisfying the condition, the projections of the other columns outside any fixed column A form a nonempty antichain of distinct sets, since containment of two traces is exactly containment in the union with A. With at least seven columns on seven points, a column of weight at least four would leave at most three points and therefore at most three other columns, a contradiction. For 3≤v≤6 and m≥v the same argument excludes weights ≥3: the maximum sizes of the projected antichains are at most 1,1,2,3 for v=3,4,5,6, below m−1. A block of size at most two must have a private point; otherwise two other blocks cover it. Deleting a private point and its block gives induction for v≤6, starting with antichains on at most two points, and forces equality to consist of all singletons (an extra point in the deleted block would contain one of the retained singleton columns). The same reduction handles seven-point families with a private point. Without a private point all blocks have size three, and any repeated pair together with a block containing the remaining point would cover a triple. Thus m≤7, with a Steiner system at equality. At a fixed point its three incident triples determine one of 15 matchings of the other six points. The other four triples select one point from each pair and have bijective projections to each two of the pairs, giving exactly two parity choices. Relabeling acts transitively on the matchings and interchanges the parity choices, giving the stated orbits and stabilizers.

## originality

FAIL

The exact unrestricted equality classification was already recorded. OEIS A286874 gives the same extremal set-family problem and a(7)=7. Its cross-reference A303977 explicitly lists exactly two inequivalent maxima on seven bits, the singleton family and a Fano plane. The May 2018 revision already contains both types. The current entry's hexadecimal Fano representative even decodes to exactly the frozen seven blocks. The 31 labeled families and the stabilizers are mechanical consequences of these two known orbits, not independent unknown invariants. This is verified database coverage, not a failure based on inaccessible papers.

## value

FAIL

Classifying the first projective-plane optimum can be a worthwhile coding question, but the frozen claim recomputes the exact known unrestricted table entry and applies the routine Fano orbit size. The digest confirms the census; it is not an additional mathematically useful invariant beyond the established equality types.

The dated certificate retains the supplied scientific assessment, sources and limitations.
