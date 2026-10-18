---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

From pinned RESULT.md, start empty word and apply five shortest E,E,E,R,E pseudopalindromic closures to directive digits 1,0,1,1,1; result is the length-44 binary word 10011010011011001011001100101100100110100110. Recomputed closures, fixed-suffix lengths 0,0,2,3,4 and output lengths 2,6,12,23,44. Attractor Gamma={9,16,23,33,39} intersects an occurrence of every distinct nonempty factor: verified all factor sets through length 9; every longer factor crosses a mark because max unmarked run is 9. Lower certificate: first four factor-support sets for 1010,11011,00100,110011 are pairwise disjoint; forced fourth point at 18 to hit factor 0101 contradicts required point 20..23 for factor 001100. Independent exact suffix/factor occurrence enumeration validates the six support sets and both bounds; this is an exact finite word proof, not a claim about all directives.

## originality

FAIL

A direct earlier, already published length-36 pseudopalindromic prefix has the identical gamma=5 counterexample property and strictly smaller length. The 44-word is a distinct correct witness, but main purported conjecture refutation is covered and there is no motivated new extremum.

## value

FAIL

The main reason this 44-symbol instance was presented was to refute the universal four-point attractor conjecture. An earlier published October 4 result already supplies an even shorter 36-symbol generalized pseudostandard pseudopalindromic prefix with gamma=5 and a full finite certificate. The new word is different, and its exact gamma value is true, but without a proved extremality, a new bound, a classification, or a reason to require precisely this longer directive, its standalone contribution is an unmotivated second witness. Repackaging the already disproved existential conjecture as another example is insufficient distinct mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
