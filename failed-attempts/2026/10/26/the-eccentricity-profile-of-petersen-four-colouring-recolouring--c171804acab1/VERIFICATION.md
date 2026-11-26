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

The independent checker /workspace/branches/2770281c-d43d-403f-9e5c-bbf03d83ee90/reproduce_petersen.py, with output reproduce_petersen.out in the same directory, backtracks on the stated outer/inner convention, admitting each palette name except those already at adjacent assigned vertices. It enumerates each proper named colouring once, including those with an unused colour. It tests each alternative name at each vertex against the three neighbours, so exactly the legal edges are obtained. Automorphisms are generated directly from adjacency, and colour and graph permutations preserve every edge. Orbit reduction applies only to the choice of roots; each BFS reaches every named state in the full graph. The calculation gives 12960 vertices, 53280 edges, one component, radius and diameter 13 and 14, all degree counts and eccentricity multiplicities, and exactly the eleven listed size/eccentricity pairs. It agrees with both frozen outputs. Frozen programs were inspected, not executed. The calculation is exact for one graph and is not a general recolouring theorem.

## originality

FAIL

There is a distinct current indexed result for the identical named-colour single-vertex graph, with all main metrics and all eleven orbit size/eccentricity pairs stated explicitly, together with a stronger distance spectrum. The frozen degree histogram, not printed in that finding, follows immediately by counting legal changes on its eleven published representative words and weighting by their stated orbit sizes; this yields exactly the frozen vector. Thus there is no distinct remainder relative to verified current coverage. The comparison does not assert that the differently dated indexed record was published earlier or has historical priority.

## value

FAIL

A sharp metric at the first connected palette of the Petersen graph is intrinsically well motivated; if unknown, the exact eccentricity and orbit data would be useful benchmarks. Here the same metric profile is already available in the current catalogue, and the degree histogram is a direct readout of that profile's listed representative words. The independent replay is useful validation but does not leave a distinct scientific invariant of adequate value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
