---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For an unfilled graph the lower link is a cone exactly at one lower neighbor. The acyclic orientations of the ten edges are precisely those induced by vertex orders, so enumerating their induced matching sets and all subsets reconstructs the full complex. Independent exact replay enumerated 240 acyclic orientations, got face vector (20,55,20), validated the twenty successive unique-proper-coface pairs from the frozen JSON as data, and verified connectedness of the residual (20,35) graph. Its integral cycle rank is 16. Signed simplicial traces were (20,55,20), (0,0,0), and (2,-3,0) for identity, nonidentity rotations, and reflections, respectively. Lefschetz with connected H0 gives H1 traces (16,1,-4), the rational character of 4 epsilon plus 3 V, with zero invariants. This proves an ordinary collapse onto a graph and a rational representation statement, not an equivariant collapse or an integral module decomposition.

## originality

FAIL

A separate configured published record states the entire finding for the same full strong complex of the unfilled K1*C5, including the twenty-step collapse, residual graph sizes, all rational H1 traces and the module decomposition. There is no distinct supported remainder in the frozen finding. This is demonstrable coverage in the checked catalogue, not a finding about who first proved it; the later path date neither supplies priority nor removes the overlap.

## value

PASS

The mathematical result has a motivated input and useful structural content: this elementary non-cycle example separates full strong from ordinary graph Morse topology, and the collapse certificate and rational action give more than a Betti count. This assesses the value of the mathematics itself, not a second incremental contribution from re-reporting a covered finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
