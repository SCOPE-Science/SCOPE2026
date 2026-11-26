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

For linear binary words the multiset of bigrams and the initial letter determine total letter multiplicities: the bigram heads count all positions except the initial one. Conversely the letter and head counts determine that initial letter. The equal-length-four classes give 16 literal forbidden windows and four extras, 00100100, 01000010, 10111101 and 11011011. In the seven-bit suffix graph, each legal word of length n>=7 is exactly one labelled walk of n-7 steps with arbitrary endpoints. The independent replay at review-evidence/record1_arithmetic_check.py (output beside it as record1_arithmetic_check.txt) rebuilt all 128 states and 236 edges directly from letter and pair counts, checked all coordinates of the row-vector identity at lag 33, reproduced the numerator and initial counts, and verified strong connectivity, period one and both Perron enclosures by exact integer comparisons. For n>=40, the polynomial convolution vanishes by right multiplication of that vector identity; convolution for n<40 uses the verified initial values, including the empty word. Thus the finite certificate gives an all-n rational series. Primitivity gives the simple Perron rate and positive leading constant; the strict comparison uses strict entrywise containment somewhere in irreducible graphs. Independently, in the literal-only case the first four letters and the subsequent lag-four XOR bits are bijective coordinates, and a forbidden literal square is exactly four consecutive zero XORs. The tetranacci equation for that avoidance rate agrees with the literal enclosure. The literal graph has 240 surviving edges of 256 possible; the awkward wording in the proof does not change the edge set or calculation. Uploaded support was inspected, not executed.

## originality

PASS

The exact fixed-half-length-four enumerator and its Perron rate are distinct from previously stated equivalence characterizations, global or long-repetition avoidance results, and literal-square counts. No inspected statement or published table was found that covers this exact numerical invariant. This is a bounded conclusion, not a priority guarantee.

## value

PASS

Half-length four is the first possible length of a genuinely nonliteral binary 2-Abelian equivalence class: length two is determined by its sole bigram, and for length three the two bigrams with their fixed initial letter cannot be traversed in two distinct orders producing different words. Thus this slice is selected by a combinatorial threshold, not by an arbitrary enumeration cutoff. Its exact recurrent counts and rate quantify an exponential cost from only four new exclusions and provide a reusable benchmark for fixed-period avoidance, beyond the generic fact of rationality or the qualitative rate inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
