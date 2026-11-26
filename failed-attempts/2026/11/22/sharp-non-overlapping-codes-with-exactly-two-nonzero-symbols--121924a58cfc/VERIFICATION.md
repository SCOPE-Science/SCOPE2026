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

A split w=uv makes its proper prefix u a suffix of the rotation vu. Thus no two rotations can appear; any word with a nontrivial rotational stabilizer is self-bordered. Unequal cyclic intermarker gaps select a unique orientation of the shorter gap and hence m² primitive necklaces per shorter distance. For n=2d, the equal-valued antipodal case is periodic. An antipodal word with distinct markers must put a marker at one end to avoid a zero-to-zero length-one border. The two resulting endpoint orientations cannot mix, and length-d comparisons separate the two marker alphabets, giving at most floor(m²/4). In the proposed construction a prefix must contain exactly one marker, so k≤t (the second-marker index of the prefix word), and a suffix needs k≥n−s (s the suffix word's second-marker index). Because s,t≤n/2, only an antipodal half-length comparison is possible, and disjoint alphabets forbid it. This covers all proper lengths and self-overlaps, even when m=1. The claimed deficit is the difference between choose(m,2) and floor(m²/4). Independent replay with literal prefix/suffix union subset search matched all 14 small cases (python3 /workspace/replay/checks.py 3); this is finite corroboration, not the proof.

## originality

FAIL

A distinct indexed finding, 467052fb9d47, explicitly states the same exact parity formula for the same non-overlap problem and exactly two nonzero positions, on the larger domain n≥2. It also states odd primitive-necklace saturation and the even bipartition obstruction. Thus the claimed extremum is already covered in the available published statement; the explicit deficit is a mechanical subtraction once the extremum and elementary primitive-necklace count are known. The conclusion concerns substantive coverage, not who obtained it first. No historical order can be inferred from the common calendar date. The scientific failure is the matching statement, not a mirror retrieval failure.

## value

PASS

As a mathematical problem the natural fixed-weight synchronization layer has a substantive, explicit all-parameter extremum. The antipodal cut explains why primitive-necklace counting can fail at even lengths. This valuation of the underlying theorem does not credit the frozen record with a new contribution: the catalog already covers that theorem and obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
