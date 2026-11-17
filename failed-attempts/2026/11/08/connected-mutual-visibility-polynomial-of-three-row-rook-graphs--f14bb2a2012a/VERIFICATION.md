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

Each selected 2x2 subrectangle obstructs both geodesics between opposite corners, and a selected set is induced-connected exactly when the line graph of its row-column incidence edges is connected. With three row vertices, at most three distinct two-row column supports are possible, or one three-row column, yielding the displayed five-family polynomial. Independently enumerated all subsets for n=1..5, including claimed C_3 coefficients and top-degree n+3. The unrestricted combinatorial case split is sound.

## originality

FAIL

The already published exact ordinary visibility and facet-polynomial theorem for K3 □ Kn gives the SAME complete row-column support classification: 0,1,2,3 distinct pair columns or one triple column, with labelled placements and singleton freedom. Applying the standard induced-line-graph connectivity condition immediately retains the connected row-support types and removes the disconnected singletons. Hence the current polynomial and top-degree counts are mechanical restrictions of that earlier all-set classification, despite a different invariant title. It is rejected for prior mathematical implication, not incorrectness.

## value

FAIL

The polynomial is a correct enumeration of a natural newly named invariant, but it requires only a standard connectedness filter on a fully classified prior family and adds no structurally motivated new phenomenon or difficult counting step. The top coefficient is already the earlier ordinary visibility maximum-facet multiplicity. Therefore its claimed independent scientific value does not pass the required non-mechanical bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
