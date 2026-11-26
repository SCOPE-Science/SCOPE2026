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

In a nonempty configuration the integer product is positive somewhere, and every positive normalized value is at least 1/(9HW), strictly beyond the closed selection window. Thus the first image is the union of the full rows and full columns selected by the respective zero masks. Two nonempty masks give a full row and column, so every blurred count is positive in the image and the second image is empty. One nonempty mask gives a stripe with positive occupancy across all orthogonal coordinates. The induced stripe NOR map T obeys T²=ED and T³=T by the erosion–dilation adjunction. If a nonempty stripe maps to empty, the original map's absorbing convention takes over; otherwise its next stripe is on a 2-cycle. The singleton initial state has both masks nonempty for H,W>=4, and reaches the empty fixed point only on the second update. The nonconstant T²-fixed cyclic words are exactly those with no zero-run of length 1 or 2; every longer gap is preserved by ED. Such words have T(A) nonempty and disjoint from A. The stated transfer matrix counts labelled cyclic words uniquely, including both constant words, and has characteristic polynomial (lambda²-lambda-1)(lambda²-lambda+1). Subtracting the constants gives C_n. The two stripe orientations share no nonempty recurrent state, and each primitive orbit accounts for exactly two states. Independent 4x4 and lengths 4–13 enumeration corroborated the argument.

## originality

PASS

Radius-one NOR (elementary cellular automaton Rule 1), closing idempotence, and transfer matrices are existing machinery. Even a prior solution of the NOR stripe sector would not supply the all-state reduction in the normalized two-dimensional model. The inspected same-model work treats numerical regimes or different threshold sectors; it does not account for the zero-edge two-update sharp bound and all-torus recurrent census obtained from both zero masks and the absorbing empty convention.

## value

PASS

For a natural extreme of the originally numerical model, the result classifies every attractor, gives the exact orbit count without an exponential global-state search, and establishes a sharp transient bound valid across a nonzero parameter interval. It distinguishes mixed-mask extinction from genuine persistent stripe oscillations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
