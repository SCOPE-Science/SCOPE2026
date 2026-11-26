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

Reconstructed the labeled graph and independently generated all 52 perfect matchings by joining disjoint edge subsets of two halves with complementary covered-vertex sets. Direct sign-parity sums using a different spanning tree reproduce all ten absolute histogram entries, rank 11,583,488 and nullity 5,193,728. The tree restriction bijects the cut space onto all tree sign choices, giving 8192 representatives and 2048 full frequencies per class. A switch at one vertex multiplies every signed matching weight by -1. Thus it is the magnitude that is constant on a class; the phrasing at RESULT line 70 should be read in that absolute-spectrum context, not as claiming that the signed value is constant. Direct evaluation gives no singleton zeros and exactly the 48 incident mixed 12/14 pairs, no disjoint zeros. Separable direct summation of the support transform gives absolute coefficient sum 162144 and norm 5067/256 after division by 8192; cut invariance makes the kernel zero outside the orthogonal cycle space. The norm is attained by convolution at both endpoints (absolute column or row sum). Averaging any projection onto the invariant range over translation conjugates preserves its identity action on the range and contracts its norm; the only commuting projection onto that range is the stated Fourier projection. This verifies the unrestricted optimum, not just sharpness within convolutions.

## originality

PASS

The clearly overlapping proof method and several same-day graph-specific Fourier results are prior or parallel context, not novelty credit for switching, Walsh analysis or projection averaging. The supported distinct evaluation is the specific Chvátal spectrum, its low-weight zero structure and the sharp numerical endpoint norm. No matched evaluated theorem/table for those quantities was found in the inspected material.

## value

PASS

The explicitly checked connected triangle-free 4-regular graph is a standard small 4-chromatic benchmark; a direct independent-set check gives independence number four, no partition into three independent sets, and a valid four-coloring. Its two edge incidence counts make for a meaningful structural test: the first zero characters are exactly the incident mixed pairs, unlike on the cubic McGee benchmark. The full cancellation and amplification figures are useful exact recovery data beyond unsigned matching counts or general Fourier formulas, with no claim of novelty for those formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
