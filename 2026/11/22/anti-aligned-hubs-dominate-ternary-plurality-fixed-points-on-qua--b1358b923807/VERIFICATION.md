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

The exact leaf test is y=u implies x=u and x=v implies y=v. Its five/six allowed page pairs give the displayed coefficient formulas after adding the opposite hub to the count vector; color relabelling gives factors 3 and 6. With hubs (0,1), the first hub's failure differs from A2>A0 only when A1>=A0 (including a tie of the two challengers), with Chernoff rate (2+2 sqrt(3))/6. The hub-swapped event has the same rate of error, and the six bivariate increments give diagonal MGF (2r+r^2+2+r^(-2))/6<rho for simultaneous lower tails. Tilting the single-coordinate walk at log r makes +/-1 symmetric, with variance 2 sqrt(6)/(1+2 sqrt(6)) and a positive atom at zero. Lattice Fourier inversion gives the centered local Gaussian limit at each fixed -j and a uniform O(m^(-1/2)) bound; undoing the tilt gives summable weights r^j for j>=1, yielding the stated c. Inclusion-exclusion and the six ordered distinct hub pairs produce the negative 12c correction. The agreeing sector is bounded by 5^m, and division by 3^(2m+2) gives the already-fixed probability, not any basin probability.

## originality

PASS

The exact count and sharp first correction for labelled square books under the specified tie rule were not found in the inspected comparisons. Same-graph results change the process; same-rule results change the hub/leaf structure and do not specialize to this count. This is a bounded assessment, not a historical-priority guarantee.

## value

PASS

The book graph isolates two interacting hubs with simple repeated pages, a useful comparison problem for finite-state network dynamics under explicit tie retention. Opposite hubs ultimately dominate, and the first loss from the full six-choice page ensemble has a computed exponential rate and lattice prefactor; a count bound or leading growth rate would not identify that rare-event mechanism. The result is meaningful without claims about basins or other plurality rules.

The dated certificate retains the supplied scientific assessment, sources and limitations.
