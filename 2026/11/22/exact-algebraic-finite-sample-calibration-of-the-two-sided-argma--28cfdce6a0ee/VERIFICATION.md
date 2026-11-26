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

The probability integral transform and the density n! on the ordering simplex give the correct normalization for a fully specified continuous simple null. Pairwise ties between the signed affine deviations have measure zero. The winning sign fixes a half-interval on which its deviation is positive; at a fixed winning coordinate u, the other rank constraints are exactly the two-sided affine bands in the record. The split volumes multiply, with no conditional-density factor beyond n!. Squaring the threshold inequality on that sign domain yields the stated quadratic interval. A chamber cut at every line crossing keeps bin eligibility fixed. Ordered bin counts partition the admissible region up to null sets and contribute products of width powers divided by factorials, so integrating polynomial pieces at rational or quadratic endpoints proves finite piecewise algebraicity. Each point-level event fixes the winning coordinate to finitely many roots, so the CDF is continuous; t=0 and the n=1 support edge are consistent. An independent direct slice calculation using d_i=1/(2n)+|U_(i)−(2i−1)/(2n)| recovered both radical values. The exact differences H_3(t)−19/20 lie between −3854/10^9 and −3853/10^9 at t=2.2981, and between 2265/10^9 and 2266/10^9 at t=2.2982, giving the strict enclosure.

## originality

PASS

The strongest matching primary and indexed statements address the identical statistic only asymptotically or in its far tail, or give an exact one-sided finite-sample law. They do not establish the exact full finite-sample two-sided calibration. This is a bounded assessment, not a historical priority certification.

## value

PASS

The statistic and its finite-sample calibration problem were independently posed in primary literature. The formula certifies critical-value bounds under the simple null without relying on simulation or the limiting distribution. The all-n construction, exact small-sample examples and rigorous finite threshold bracket address the specific missing law, not merely its tail or a numerical recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
