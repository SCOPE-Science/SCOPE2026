---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

A character is multiplied by the signed kernel sum under counting convolution. Conditioning on the middle row length b gives the product of the independent numbers of top and bottom lengths subject to b; expanding the product of selected factors (1−2·incidence) gives the stated formula. For independent replay run python3 /workspace/reviews/replay-4.py; it encodes shapes using three separator positions and sums parity directly over the complete shape list, rather than invoking the packaged checker. Widths 2,6,10,14 give zero-count tuples (0,2),(0,3),(0,0,30),(0,2). All 4525 tested supports at width 10 were covered, with the exact published row-pair minimum magnitudes 4,2,4,10,2,4. The computed zero triples equal the actual 15 listed supports and their disjoint set of half-turns; the width-2/6 pair witnesses and both width-14 pairs also agree. Complement followed by rotation induces W(ρS)=(−1)^|S| W(S); ρ has no fixed cells at width 10, so an odd support cannot be fixed. At odd widths the central cell is toggled under the diagram bijection, proving a singleton zero, and 4|n makes the shape count binomial(n+3,3) odd by Lucas, ruling out all zeros. This leaves only widths 2 and 6 to check before 10. The proof does not claim full nullity or a general law for larger widths. The phrase 'first three singular widths' in the supporting self-review should be read as referring to the 2 mod 4 subsequence; odd widths already have singleton zeros in the actual theorem.

## originality

PASS

Qualified best-of-knowledge credit for the first cubic-only width and exact support census, not for the general Boolean Fourier identity, rank parity, complement duality, or inclusion–exclusion method.

## value

PASS

Minimum support is the first order at which the Young-diagram incidence kernel annihilates a Boolean interaction. At width 10 the complete quadratic test misses real cubic blind characters; the return to a pair zero at width 14 disproves monotone growth across the first four widths in this congruence class. Locating the first such width and identifying every offending interaction is a useful exact benchmark on a standard shape family, even without a general-width spectrum or full nullity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
