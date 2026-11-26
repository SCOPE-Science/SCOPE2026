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

The claim concerns positional occurrences and one-based internal cuts in indexed binary words. The proof tests all proper borders at all starting positions (including overlaps), then rules out closed one-letter extensions only on available sides. For a zero-based interval [i,j] the crossed one-based cuts are i+1 through j inclusive, so the difference marks at i+1 and j+1 count exactly the desired occurrences. A freshly written exact enumeration independently exhausts all words at lengths 2 through 14 and gives (1,1,2,2,3,3,4,4,5,5,6,7,8). The only pairs at eight crossings at length 14 are 00101110100011@8, 00111010001011@6, 11000101110100@6 and 11010001011100@8; reversal with g mapped to 14-g and complementation give the four distinct pairs from the first. The maximum at length 13 equals, rather than exceeds, its ceiling-half benchmark. This proves the finite first threshold and rigidity, not an asymptotic statement.

## originality

PASS

The exact unrestricted finite maxima, the exclusion of earlier ceiling-half excesses, and the exhaustive classification at 14 survive the closest comparisons. The same-day persistent-density record already supplies F₂(14)≥8 and one representative of the very same orbit (hence all four witnesses by symmetry); no independent originality or chronological priority is credited for that construction. The construction does not show maximality, uniqueness, or absence of earlier excesses.

## value

PASS

The binary cut-extremal function is the same local-density observable as in the published bounds. The stronger rounded half benchmark asks exactly when a cut first supports more than ceiling-half many occurrences. The first excess and the unique extremizer orbit distinguish an exact finite boundary from merely producing high-density examples, and supply a useful benchmark for future structural bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
