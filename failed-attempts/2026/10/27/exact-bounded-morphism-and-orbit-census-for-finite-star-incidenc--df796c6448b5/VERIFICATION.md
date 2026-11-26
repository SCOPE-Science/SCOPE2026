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

Back forces each source maximum to map to a target maximum. A leaf's principal filter has two worlds, too few to lift the target center's filter when s≥2, so surjectivity forces center to center. Forth then permits exactly the matched leaf or the matched maximum at each source leaf. Each target leaf must be hit, and lifting there forces its target maximum to be hit by the corresponding source edge; hence the center's entire filter is lifted. This supplies both directions of the word bijection and the missing-letter inclusion–exclusion. The center is the unique minimum with multiple strict successors, so the automorphisms are exactly arm permutations. After source permutations only the tagged multiplicities at each index matter; target permutations make these pairs unordered. There are n types of total size n, as required by the product. In independent Python enumeration I tested equality of principal-filter images for all onto functions and counted orbits by explicit multiplication by arm permutations. For (r,s)=(2,2),(2,3),(3,2),(3,3),(4,2), the pairs (maps,orbits) were (2,1),(0,0),(18,2),(6,1),(110,6). The frozen replay paths are artifacts/verify_star.py and artifacts/verification_output.txt. The uploaded sweep at lines 78–81 actually samples only s≤r, so those sweep assertions alone do not test nonexistence. Universal correctness follows from the proof, not these finite checks.

## originality

FAIL

The prior Resultary branch-use theorem e5029a66a849 already gives the same normal form as a specialization, up to an equivariant identification of map sets. The frame orders are not isomorphic, but the labelled count, existence criterion and two-sided orbit census all follow from that same prior word model. This is demonstrated coverage, not an inference from a coincident product, a date or the absence of other papers.

## value

FAIL

Star incidence is a natural modal test case, but here the change of order leaves the known tagged map sets and their arm actions unchanged. The resulting existence, labelled count and orbit count are routine transfers; the orbit product uses only the immediate multiset quotient, not a new classification beyond the earlier word structure. No separate surviving substantial claim is established by the frozen package.

The dated certificate retains the supplied scientific assessment, sources and limitations.
