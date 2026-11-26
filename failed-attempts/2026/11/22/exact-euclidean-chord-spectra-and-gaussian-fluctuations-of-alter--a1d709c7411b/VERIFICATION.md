---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For a fully alternating arc in unscaled ambient coordinates, the primary vertex construction gives distinct alternating selections. Translating negative coordinates by 1 also makes these zero–one points, each extreme among the listed points. The one-match open/closed block matrix is [[2,1],[1,1]], giving F_(2r+1). For a pair, the squared chord counts exactly the differing bits. It is even since each support has even size. The start and end are both 00, and quotienting the two exchanged states gives the claimed cubic characteristic polynomial and recurrence; the initial terms and generating-function numerator agree. The second shell is genuinely off-diagonal only for r>=2. Its recurrence gives 72 ordered pairs in rank 3 and r^2*2^r for all r>=2, while the leading term is 2^r. Support follows by comparing consecutive-interval matchings to the empty matching. At q=1 the positive transfer has a simple analytic dominant root, a spectral gap and a nonzero start/end eigenprojection; implicit differentiation verifies the two log-root derivatives and strictly positive variance. Taylor expansion proves the normalized CLT, and discarding the diagonal of mass 1/F_(2r+1) leaves the limit unchanged. An independent exact enumeration of 435664 ordered pairs and symbolic cubic/log-derivative checks are reproducible with record1() in /workspace/branches/frozen_metric_replay.py. The discrete tests do not prove the infinite result; the frozen script was read, not run.

## originality

FAIL

The earlier linked type-C transfer already covers the ordered rank-r enumerator by a direct boundary specialization, not a new rank-marking or an inversion of its mixed-rank output polynomial. In its published state encoding, y_1=|A|-|S|, so restricting both endpoints to rank r just replaces the initial row of ones by e_11^T. For the alternating profile, this produces the identical alternating two-matrix product after relabeling the binary suffix states; the cubic, shell coefficients and explicit Gaussian constants follow by ordinary algebra and standard Perron asymptotics. The older run-length theorem also separately covers the diameter and the linked theorem explicitly supplies the top multiplicity. No scientifically distinct claimed remainder was established.

## value

PASS

The rank-specific chord distribution and separation of extremal from typical chords are meaningful metric descriptors for a natural infinite family. Their explicit statement is useful even though this record does not clear the distinct-contribution requirement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
