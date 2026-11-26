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

For a single-one factor, a border exists exactly when both sides have nonzero zero runs. For a two-one factor, equal endpoint symbols give a one-letter border; when only the leading zero run is present, the only possible proper prefix ending in 1 is the run followed by the first 1, which is a suffix exactly when the run is at most the central gap. Reversal deals with a trailing run. This proves the occurrence counts, including the singletons of 11, with no deduplication by factor string. The disjoint gap classes sum to the stated series; [z^n]B counts (n-2)/3 < m <= (n-2)/2. Uniform gaps converge by simplex Riemann sums, and ties lie on area-zero lines. On Q=2 the inner gap is the simplex maximum, giving one third of its inclusion-exclusion CDF. On Q=1, requiring both outer gaps at least 1-t gives (2t-1)_+^2, with one third of the translated simplex with all gaps at least 1-t excluded. Integrals give conditional means 29/36 and 11/18 and the stated marginal mean. The independent raw substring prefix/suffix checker and separate expansion of the rational series agreed on all 3654 words of lengths 2–28; replay: /workspace/branches/4fc04731-0aed-42bc-94c7-65db87324ec8/independent_check.py. The source scripts and saved outputs were inspected but not executed; the bounded replay supplements the all-length proof.

## originality

PASS

The known longest-border spectrum implies the maximum-length marginal, as the finding already credits. Neither that spectrum nor the inspected all-occurrences algorithm gives the closed occurrence-interval classification, multiplicity census or joint limit. Those are the distinct claim; priority beyond the checked evidence is not certified.

## value

PASS

In the first sparse binary family with interacting marker gaps, the number of optimal positions is genuine information beyond the already known optimal length and is the output size for all-occurrences reporting. The classification exposes the exceptional ties, gives their exact frequencies, and shows how optimum length differs between the two positive-probability multiplicity classes. This is a complete natural fixed-content refinement rather than a repeat of the marginal spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
