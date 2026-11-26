---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Single-symbol counts and homogeneous pairs/triples recover the run and singleton inventories. The 001 and 100 occurrences count the ends of long zero-runs adjacent to ones; 010 counts internal singleton one-runs. Hence the endpoint correction is recovered and, in reverse, determines both mixed bins. Balanced runs give independent one-per-symbol endpoint choices; imbalanced runs require two distinct majority runs, giving the stated feasible number of long endpoints. An all-singleton inventory has one length; otherwise each length from its minimum occurs. Summing the three majority endpoint cases separately and then the geometric series reproduces the rational function. Differentiated geometric series for n, n², n³ and n⁴ plus the residue terms reproduce the fraction exactly, including the exceptional n=1. One representative per class attains the code bound. Private replay: `python /workspace/independent_checks_1_4.py 2` also confirms literal observation counts at n=1..15. Finite checks are corroboration, not the proof.

## originality

FAIL

A distinct indexed record demonstrably covers the entire mathematical finding, including the run-and-endpoint classifier, not just its sequence or growth. This is a present coverage decision, not a finding that the other record preceded this one: the mirror entry is dated 2026-10-26 UTC, later than the frozen record's dated path (2026-10-19 UTC). No separate surviving addition was identified.

## value

PASS

As mathematics this is a motivated exact classification for the length-limited channel in Ye–Elishco: it identifies the first additional run-boundary statistic beyond cutoff two and gives the maximum zero-error codebook at every blocklength, not just an observed growth law. This utility does not supply a rationale for a duplicate as a new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
