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

All-positive labels require a matching, and a full matching fails a single-edge flip. Fixing any positive submatching multiplies the crossing sign of a completion by a constant: for each fixed chord, its crossings with free chords have parity equal to the number of free endpoints on one arc. Thus the local four-endpoint signs are +,−,+ even in the presence of fixed edges. For the six-endpoint avoidance lemma the two class sizes are 8 and 7 (their signed sum is 1 by the all-ones-upper-triangle Pfaffian). Inclusion–exclusion leaves at least 10 avoiders for one or two forbidden edges (15 for zero), and 8 for three; in the last case at least one positive matching is excluded because each forbidden chord extends to a positive matching on six endpoints. Fixing an allowed edge then inducts to more endpoints. This handles every labeling leaving at least six endpoints; with four and no forbiddens both signs occur. For size n−1 supports, all-positive forces the completion and each single-label flip reduces to the four-point switch: there is a sign-preserving alternative exactly when the omitted edge does not cross the flipped edge. The omitted edge is uniquely determined and must divide the remaining endpoints into even arcs. For each such chord the unsigned count is the product of the two double factorials and the signed count is 1 (the arc Pfaffian expansion alternates to 1 on each arc). Summing over odd endpoint differences gives the stated L_n and n² difference. A polygon side can be omitted in a matching of either sign for n≥3, while the only negative matching at n=2 has no shattered singleton. The resulting dimensions and the example coefficients agree.

## originality

PASS

The parity-constrained trace problem is distinct from noncrossing matching shattering, ordinary crossing-count enumeration, and shattering on a host with deleted edges. The full two-class criterion and its top-coefficient difference survive those comparisons. Neither the Pfaffian sign nor the positive-class lower bound supplied by the noncrossing subclass is new.

## value

PASS

This gives a complete trace classification for two natural sign classes, not only a common dimension. It locates the obstruction exactly at one missing pair and measures the imbalance at that degree, while showing that parity cannot distinguish their lower-dimensional face counts. The exact signed count is useful for comparing the two classes and is not determined by their unrestricted class sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
