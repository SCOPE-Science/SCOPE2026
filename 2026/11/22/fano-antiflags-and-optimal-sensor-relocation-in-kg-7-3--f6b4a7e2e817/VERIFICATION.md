---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification details

The exact finite graph has 35 vertices, each a three-subset of a fixed seven-element ground set; adjacency is disjointness. The power-domination closure starts with the selected vertices and all their neighbors and repeatedly marks unique unseen neighbors. No graph libraries, downloaded datasets, or external dependencies are needed.

Run these commands from the directory containing the attached package files:

```sh
python3 verify_full.py
python3 verify_symmetry.py
python3 verify_fano.py
```

`verify_full.py` independently enumerates all sets of sizes one, two, three, and four, checks every quadruple against the pencil criterion, builds both optimal-state graphs, and computes every all-pairs jump distance. It checks 840 optima, 5,460 jump edges, 420 slide edges, radius and diameter six for jumps, and the exact all-pairs distance histogram.

`verify_symmetry.py` uses set-valued graph neighborhoods and all 5,040 point permutations to construct 10 orbits of three-subsets of graph vertices and 38 orbits of four-subsets of graph vertices; their sizes add to the complete binomial totals. Exactly one four-set orbit is successful, and its representative's closure is the full graph after 20 initial observations and two additional forcing rounds. The script regenerates `orbit_census.csv` and independently computes the vertex-transitive jump distance profile \((1,13,39,87,204,320,176)\).

`verify_fano.py` independently enumerates all 30 labelled Steiner triple systems on seven points by relabelling one explicit Fano plane, constructs all 840 distinct nonincident point-line pairs, and checks uniqueness of their pencil-plus-line configurations and complement-transversal partners.

The `orbit_census.csv` includes representative triples, orbit cardinalities, initial observation counts, closure counts and propagation-round counts. `CERTIFICATE.json` collects the exact finite assertions. All three programs have been executed successfully as packaged. A search over a single finite 35-vertex graph does not prove corresponding statements for larger graphs; no independent external audit is claimed.
