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

Both admissibility conditions are hereditary under prefixes; for each newly appended symbol an overlap must be a suffix of period p and length 2p+1, checked by comparing p+1 consecutive positions shifted by p. An overlap-free source is cube-free, so the next curling digit is 2 exactly when an equal-block square is a suffix. I exhaustively enumerated labeled prefixes through depth 85 using an independent bit-plane depth-first traversal: shifted XOR masks test suffix periods in both alphabets, without quotienting source labels. At 84 the two printed length-84 outputs occurred with frequencies 4032 and 2016, respectively, with common prefix length 83; at 85 no admissible prefix survived. This independently corroborates the canonical enumeration and the full search in the frozen evidence. The sixfold size of each canonical orbit at 84 follows from using all three symbols, which both the frozen canonical check and known extremal characterization support.

## originality

FAIL

An earlier distinct indexed record directly states the two terminal images with the same common length-83 prefix and the exact labeled split 4032/2016. It also gives a stronger description of all length-83 continuations and a condition on the final two source symbols, and supplies tabulated source/transform pairs. The later same-day match provides additional overlapping coverage but its date does not determine priority. The arXiv primary paper's known maximum and total alone do not imply the image partition.

## value

FAIL

The extremal image constraint and its unequal fibers are a natural exact invariant, but this submission reproduces an already stated and tabulated classification. It does not supply a new explanation, additional invariant, or independent useful remainder; another correct exhaustive reproduction does not rescue it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
