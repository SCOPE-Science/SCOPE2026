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

The feedback parametrization is bijective: the two five-bit windows with a common four-bit suffix must append different bits, and the resulting permutation yields a cycle exactly when its zero orbit visits all states. Starting with the unique zero window identifies rotations only. Neither reversal nor complementation is quotiented. Independently enumerated Euler tours in the directed order-four de Bruijn graph, by enumerating last-exit trees with the all-zero edge prescribed first. Each complete tour gives a tree: along a nonroot last exit to another nonroot, the next last exit must be later. Conversely the local outgoing-edge orders determined by a tree give an Euler tour. The greedy walk can stop only at the root; if an edge were unused, unused last exits would lead from an unexhausted vertex to the exhausted root, contradicting balance of unused in- and out-degrees after the closed walk. For each generated word, counted ordered pairs of one-positions with difference t, giving the exact correlation 4*overlap(t)-32 by balance. Replayed via /tmp/opencode/frozen_review_3.py using Python 3. It matched the complete table (20 occupied cells, 2,048 distinct rooted words), the digest e8b5746482780303fec542789b123a2d51a892f460137bb9f8a96c85fec30421, the p=0 count of four at m=-8, and both absolute bounds (12 and 784). These are nonzero shifts, not nonzero correlation values. This is exhaustive only for order five; the frozen verifier was read, not executed.

## originality

FAIL

A distinct earlier indexed record supplies the complete same-universe, per-cycle periodic autocorrelation data. Taking the two extrema and counting pairs is a direct reduction of those data, so the frozen table is covered even though no checked paper printed it. The verdict is about coverage, not priority or mathematical validity.

## value

FAIL

Signed sidelobe extrema measure a natural feature not encoded in the absolute peak alone, but the entire claimed result is a direct aggregation of a complete existing autocorrelation dataset. A different correct census is a corroboration, not an unknown finite invariant. No non-covered result remains for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
