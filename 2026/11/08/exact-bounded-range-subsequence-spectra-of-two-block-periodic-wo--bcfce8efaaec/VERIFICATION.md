---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The proof in RESULT.md is an infinite-parameter mathematical argument. Independent finite checks were executed using the accompanying dependency-free script, then the script was replayed from the packaged files.

Command: `python3 periodic_span_verify.py`

Expected output:

`PASS: 36792 exact reference-span comparisons; 324 sharp-threshold comparisons; 667 coefficient comparisons; all polynomial coefficient mass totals equal 2^k.`

The reference routine scans each possible phase of the host period and greedily embeds the pattern; it does not call the asserted run formula. For the generating function, independent finite truncated polynomial products compute coefficients and compare them to the direct reference distributions. Tested parameters: \(1\le a,b\le6\) and \(1\le k\le9\) for pattern spans and threshold, and \(1\le a,b\le4\), \(1\le k\le7\) for rational-series coefficients. These checks do not substitute for the proof for unbounded parameters. Independent literature or mathematical audit has not been performed.
