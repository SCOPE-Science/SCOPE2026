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

The induced line graph of a set of retained cube edges is acyclic exactly when those edges form a linear forest: degree three yields an incident-edge triangle, and with degrees at most two a cycle survives as a line-graph cycle. Seven retained edges on eight vertices therefore require a spanning path, and an explicit cube Hamiltonian path proves that keeping seven is possible. In a legal exchange an added edge cannot join two old internal vertices: restoring both degree bounds with one deletion would require deleting the very edge just added. An endpoint-to-interior addition requires deletion of the old cycle edge at the interior vertex and is a slide; an endpoint-to-endpoint addition gives a cycle and the two endpoint-adjacent deletions are slides, with five more unrestricted deletions. Thus line-graph slides are exactly endpoint backbites. An independent exact reproduction regenerated the surviving sets and, separately, the unoriented spanning paths and both moves, obtaining identical graphs in the two representations. Replay with python3 /workspace/branches/848edb27-0ab4-456a-bf08-a40f784a6563/independent_check.py. Its BFS and pair verification (lines 134–173; independent_check_output.json lines 2–42) give 72 states, 144 and 264 edges, every eccentricity six in both graphs, and identical sets of 144 unordered distance-six pairs. The exact distance histograms are (144,408,624,732,504,144) and (264,408,576,684,480,144). The action of coordinate permutations and bit flips gives three orbits of 24; the replay (lines 177–230 and output lines 43–124) agrees with all shell and path signatures, not merely the diameter.

## originality

PASS

The credited assertion is the specific cube/cuboctahedral exchange metric, including the orbit shells and preservation of the diameter-pair set. Neither the backbite move nor the count of Hamiltonian paths is credited as new; the two representations encode one result. Several prior or parallel graph-specific analyses are relevant, but none of the accessible statements supplies this metric.

## value

PASS

The cube is a canonical small three-dimensional lattice cell in backbite sampling, and its line graph is a natural test of how locality constrains optimal decycling sets. The large increase in one-step moves without any change in the full worst-case pair set is not implied by connectivity or by the known path count. Exact orbit shells and distances are useful small-instance benchmarks in both settings. No general cube theorem or mixing-time conclusion is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
