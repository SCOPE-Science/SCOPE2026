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

The cube-edge incidence construction gives twelve sites of degree four. The independent exhaustive replay evaluated both synchronous successors on every one of the 531,441 ternary states, treating GHM states 1 and 2 as unconditional transitions. Functional-graph classification assigns every state its unique eventual cycle, its least period, and its distance to that cycle. The only joint classes were (1,1):512505, (3,3):24, (6,1):48, (8,1):15984 and (12,1):2880, giving 18,912 unequal-period states and the stated 789-fold oscillation probability ratio. The CCA basin spectrum, writing size×multiplicity, was period one: 116×18, 1300×36, 4989×24, 114627×3; three: 3×8; six: 6×8; eight: 416×18 and 472×18; twelve: 360×8. GHM has one fixed basin of 531417 and eight period-three basins of size three. Sharp depths eight and six each occur 72 times, with verified witnesses 31727 and 16188, respectively. The lcm of the CCA periods is 24, and that of GHM is three, which proves the two map identities after the sharp entry times. Acting on temporal-orbit identifiers by the 48 cube maps and three CCA color shifts gives (period,class size) pairs (1,3),(1,18),(1,24),(1,36),(3,2),(3,6),(6,8),(8,18),(8,18),(12,8); the two period-eight classes have respective basin sizes 416 and 472.

## originality

PASS

Credit the exact same-graph GHM marginal, including its sharp entry time, to the overlapping catalogue finding. The supported distinct claim is the threshold-two CCA census and its genuine common-initial-state comparison with GHM, including CCA geometric classes. The strongest inspected statements either cover the GHM restriction or change the dynamics or graph.

## value

PASS

The cuboctahedron is a natural four-regular comparison graph with overlapping triangles and squares. Running the two standard three-color rules at their same two-contact threshold exposes a sharp contrast not captured by naming their periods: the short CCA cycles have no transients, the long CCA cycles have large basins, and almost all oscillatory CCA starts are fixed-point-bound under GHM. The common-state census and geometric classes supply concrete benchmark data for comparisons of threshold dynamics and separate two distinct types of attracting eight-cycles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
