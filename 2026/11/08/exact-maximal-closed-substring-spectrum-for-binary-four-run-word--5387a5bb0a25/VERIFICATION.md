---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For every positive a,b,c,d the word 0^a1^b0^c1^d has at most three transitions in a factor. Zero-transition maximal closed occurrences are precisely four whole runs; one-transition factors are not closed; two-transition closed words require balanced outer unary runs, with exactly one deletion at the crossing extension when c≤a or b≤d; three-transition closed words have border 0^x1^y for x≤c and y≤b and a unique maximal occurrence at x=min(a,c), y=min(b,d). These disjoint exhaustive cases give K=5+min(a,c)+min(b,d)−I(c≤a)−I(b≤d). Compositional floor inequalities, explicit upper/lower witnesses, and a continuous intermediate family prove the complete fixed-n interval {5,...,floor(n/2)+4} for n≥5 and {5} for n=4. Independent direct factor-and-overlap border enumeration reproduced every endpoint for all 1296 tuples with a,b,c,d≤6 and all attainable spectra n=4..19; this is supplemental to the all-length proof.

## originality

PASS

General run-length encoded MCS enumeration and valid-pair/unary-border structure preexist (Umezaki et al. 2026), as do general output-sensitive MCS algorithms. Those sources are algorithmic and do not visibly state a direct four-run endpoint list, the corrected min formula, or the fixed-length gapless extremal output spectrum. The latter involves an additional integer composition optimization beyond running a generic enumerator. Because the highly relevant 2026 run-length paper full text could not be retrieved and some of its structural lemmas may imply the count routinely, this is a specifically identified material originality/value risk; best-of-knowledge acceptance is limited to the all-n explicit classification and attainable spectrum, not the general MCS mechanism.

## value

PASS

Four alternating runs are the first natural binary run class simultaneously exhibiting two-transition unary-border and three-transition mixed-border maximal-closed occurrences. The exact endpoint structure and gap-free sharp range of output counts at fixed length give a small but genuinely useful analytic benchmark for compressed/output-sensitive substring enumeration, not a known table, incidental fixed tiny instance, or alphabet renaming. Extending general procedures to a sharp symbolic family and all attainability values is mathematically motivated even without a downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
