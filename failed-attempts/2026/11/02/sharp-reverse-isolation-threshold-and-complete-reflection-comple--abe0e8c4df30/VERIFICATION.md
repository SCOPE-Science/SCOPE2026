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

The independent reconstruction from h(0)=01, h(1)=21, h(2)=0 gave the stated 37-letter sixth iterate, 17 length-eight factors, and 119 substitution-image windows with no closure failure. Non-erasing images ensure an eight-letter output window intersects at most eight consecutive input images; extending this input block to eight letters proves inductive exhaustiveness for the entire fixed point. Reversal disjointness at length eight excludes every longer reflected factor. Taking short subwords of the certified set (every shorter factor extends to the right) reproduces Q1–Q7, including 1012101 at length seven. Subtracting one class per nonpalindromic pair gives the stated small values; the empty word gives the length-zero value and Currie et al., Theorem 1, gives the 2n+1 tail. The finite check was reconstructed independently; the frozen script was inspected, not executed.

## originality

FAIL

A distinct indexed result states the same complete reflection spectrum for the exact same morphism. Its different finite proof does not distinguish the boxed scientific finding. This is demonstrated statement-level coverage, not a claim about who obtained it first.

## value

FAIL

The sharp barrier and exceptional pairs are naturally motivated, but the complete invariant is already supplied for this word. A short alternative check of the identical finite table is sound and reproducible, but the record establishes neither a distinct useful result nor a substantive methodological gain warranting a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
