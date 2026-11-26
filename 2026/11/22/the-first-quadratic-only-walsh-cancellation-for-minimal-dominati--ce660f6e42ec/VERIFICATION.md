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

A closed-neighborhood dominating mask is minimal iff removing any one selected vertex breaks domination, by monotonicity; this is equivalent to the stated private-neighbor condition. The independently written python3 /workspace/branches/independent_finite.py paths (NumPy integer arithmetic) uses shifted-mask domination, actual deletions and direct signed character sums, rather than the supplied enumeration and forward transform. It matches the full table at all orders 1–17 and the published 268-mask digest. At 17 it matches all fifteen pairs and the complete zero-degree histogram: 19,516 zeros, no constant or singleton zeros, higher-degree zeros as well, rank 111,556, least nonzero modulus 2 and maximum modulus 268. No smaller positive order has both a zero and no singleton zeros. The condition number is 134 on the nonzero singular spectrum with the stated convolution normalization. A separate recursive inverse transform of the nonzero-mode indicator gives integer absolute sum 3,341,768 before division by 2^17. The resulting kernel gives both endpoint norms by absolute column or row sums. Translation conjugation preserves the range, the property of acting identically on it, and the norm; averaging any projection over translations therefore gives another projection with no larger norm. Scalar action on the distinct Walsh characters forces the averaged map to have multiplier one on surviving modes and zero elsewhere, over either real or complex scalars. Thus the ratio 417721/16384 is the sharp minimum over all endpoint projections. The title's quadratic-only shorthand describes the first support size witnessing cancellation, not an absence of higher-degree cancellations.

## originality

PASS

The supported distinction is the sharp labelled-path support-degree boundary and associated exact spectral and projection data for the inclusion-minimal closed-neighborhood family. General enumeration tools, the private-neighbor lemma and the averaging mechanism are not claimed to be novel. The inspected exact Walsh comparisons concern different admissible masks or graphs; same-day listings do not establish priority.

## value

PASS

The finite cutoff is motivated by the mismatch between singleton tests and invertibility: this is the first path for which every individual coordinate test survives but exact recovery still fails on pair modes. The explicit pairs, nullity and sharp endpoint projection norm quantify the discrepancy and provide a reproducible test case for recovery and parity-enumeration methods. No asymptotic or all-order classification is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
