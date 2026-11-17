---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

PASS: For a marker-start word 1 0^a 1 0^b 1 0^c, every proper border must start at one of the two later markers; checking both yields unbordered iff a<c. Reversal gives zero-run start iff a>c. Interior same-symbol cuts have a one-letter border. Counting ordered three-gap compositions and dividing by marked-marker multiplicity yields M0,M2,M3 and moments. Independently enumerated 3,876 fixed-three-marker words for n=3..18 by direct prefix/suffix checks, matching cut predictions and count classes. The all-length algebra is the proof.

## originality

FAIL

FAIL: Both October 18 and October 26 published theorems are decisive: October 26 proves identical *positionwise* marker/zero-run gap tests and complete necklace distributions, while October 18 already proves identical all-n linear-word count formulas. The new expectation and variance are elementary moments of those existing exact histograms.

## value

FAIL

FAIL: Fixed-content border correlation is a meaningful combinatorics problem, but the complete classification has already been solved and published. Algebraic restatement and elementary variance derivation from the known full distribution create no independent valuable claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
