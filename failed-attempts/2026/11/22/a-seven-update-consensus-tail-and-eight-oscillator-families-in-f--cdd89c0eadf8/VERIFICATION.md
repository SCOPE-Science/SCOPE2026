---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The incidence graph has 20 degree-four vertices and 40 edges. Tie retention is equivalent to majority of the four neighbors and the vertex's own bit. Independently constructing the transition on all 2^20 states, then testing the first F^(t+2)(x)=F^t(x) through t=7, reproduces all twelve nonzero first-entry/period cells and leaves no unclassified state. Testing F^(t+1)(x)=F^t(x) at entry separates fixed and primitive period-two states, yielding 4,036 fixed states, 702 period-two states (351 temporal orbits), and basin totals of 959,624 and 88,952. The time-seven row has 960 members, split 480/480 between the two unanimous equilibria. A separate pullback of the all-zero state using update masks for the two bipartition classes gives exactly 960 first hits at time six and 480 at time seven; global complementation proves identical counts for all-one. These exhaust the two late fixed-basin rows. The five doubled pairs are precisely the non-singleton identical-open-neighborhood classes. Each permutation of those pairs forces the edge-vertex permutation, and arbitrary internal twin swaps are allowed. Thus the nine natural generators give the full group of order 3840. Its orbit traversal, including a temporal phase swap only among period-two states, yields the exact 44/8 class counts and both stated size histograms.

## originality

FAIL

A distinct published Resultary record on exactly this 20-vertex graph and update already gives the core sharp clock, complete entry/period table, basin totals, and 44/8 symmetry classification, as well as a larger individual-attractor basin census. The additional printed late-consensus splits and symmetry-class size histograms in this frozen record are direct readouts of that comparator's existing per-state terminal and per-orbit member computations, not an independently new classification. This is an exact coverage finding; relative same-day provenance or temporal priority is not determined.

## value

FAIL

The smallest semisymmetric graph and distinction between short oscillatory tails and long consensus tails are well motivated. As a standalone finding, however, almost the entire classification is already present in the exact public comparator, which also goes further on individual basin sizes. The added late terminal-color counts and group-orbit size multiplicities are mechanical tallies of that complete computation, not a surviving independent invariant requiring new analysis. Revalidating the package is useful as a check, but does not give the frozen claim independent scientific value under the review standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
