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

On simple C_n for n≥5, either set fails domination precisely when the opposite label has three successive occurrences. Two distinct vertices have at most one common neighbor; a repeated nonempty L-signature is therefore a singleton shared by the two zeros on either side of a one. Their two other neighbors must be zeros, exactly 00100, and the converse holds. The marked zero-run argument counts pairs of a labeled word and a distinguished run start: for k runs, the trace counts encodings with the distinguished run at position 0, and there are n positions for that start and k starts per word. This gives n/k even for periodic words. The run weights and exclusion of a single one between two length-two zero-runs give det(I−T)=1−uz²−u²(z³+z⁴+z⁵)−u³z⁶. The trace-log identity gives −z∂z log det(I−T); its terms below degree five are exactly 2uz²+3u²z³+6u²z⁴. After this subtraction the inhomogeneous numerator has degree at most ten, giving the stated recurrence. The displayed n=5–8 coefficients agree. The frozen output is finite corroboration only; inspected but did not run verify.py. The aside about an OEIS index shift is unnecessary under the listed indexing and does not affect the theorem.

## originality

FAIL

A distinct later-indexed record states the identical one-sided language and complete bivariate enumerator on the same labeled graph, with the same integer range and weight. Its larger comparison also counts two-sided partitions. This is demonstrated coverage of the entire frozen scientific claim, not a finding about historical priority. The older existence theorem, two-sided language, and univariate OEIS match alone would not establish this failure.

## value

FAIL

The size distribution is a motivated statistic and would add information beyond existence or the total count. As submitted, however, the record gives no independent exact invariant beyond the already indexed formula for that very statistic; the examples and recurrence are mechanical coefficient consequences. The complete recomputation adds no separate scientific result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
