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

Each cyclic rotation of a permutation word is distinct and a nontrivial rotation is a crossed factor of ww. Hence at most one representative per rotation class and the optimum size is at most six; all six words starting with 0 attain it. For the census I independently enumerated all binomial(24,6) sets, first factoring each illicit middle word into an incoming suffix and an outgoing prefix to precompute the forbidden masks, including repeated endpoints. This gave 348 distinct forbidden masks and 2872 accepted sets. Relabeling commutes with crossing and reversal interchanges the roles of the two ends and complementary shifts, so the group action preserves these sets. Independent orbit expansion and Burnside fixed-point summation gave 73 orbits with respective size/multiplicity pairs (8,4),(16,2),(24,17),(48,50), Burnside sum 3504, and exact agreement with all TSV rows. The stronger count is 32 both by direct prefix/suffix tests and analytically. The first-letter and last-letter sets must be disjoint. A singleton first or last forces all six words with that specified endpoint, giving eight codes. Otherwise the endpoints partition the alphabet into ordered sets F,L of size two. Four words have pattern FFLL and four FLFL. Length-two matches occur exactly in two complementary pairs among the alternating words, so an optimum takes all four FFLL words and one from each pair. A length-three match would need a prefix and suffix of FFLL words with patterns FFL and FLL respectively, impossible. Thus the six ordered partitions contribute 24 more codes. Replay: python3 -I /workspace/branches/independent-checks/record1.py; record1.log in that directory. Frozen scripts were inspected, not executed.

## originality

PASS

The distinct result is the complete optimum census and symmetry partition on the fixed permutation layer, and the 32-code stronger refinement there. The rotation bound and elementary common-first-letter construction are not novel. Neither the inspected unrestricted maxima nor the separate nominally matching count 32 in related composition/closure problems verifies the claimed census.

## value

PASS

The permutation layer is the natural four-symbol fixed composition with every symbol present once. Optimal synchronization dictionaries on that layer are reusable mathematical objects, and the exact group partition plus reconstructible representative list is useful beyond the elementary capacity six. The non-overlap refinement quantifies the difference between two widely used restrictions, on precisely the same optimum family. Value is in the complete equality classification, not a claim of broad asymptotic impact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
