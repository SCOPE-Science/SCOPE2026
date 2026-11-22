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

# Computational verification

Python 3 standard library suffices. Run the forward exhaustive trajectory classifier and the independent reverse-indegree functional graph classifier, and compare their output to the recorded full `census.json`. Run the graph identity and nonisomorphism checker against `graph_catalog.json`.

```sh
python3 verify_forward.py > forward_recomputed.json
python3 verify_reverse.py > reverse_recomputed.json
python3 verify_catalog.py > graph_checks_recomputed.txt
python3 -c 'import json; a=json.load(open("forward_recomputed.json")); b=json.load(open("reverse_recomputed.json")); c=json.load(open("census.json")); assert a==b==c; assert all(v["map_power_identity"] for v in c.values()); print("FULL_CENSUS_OK")'
```

The classifiers were executed successfully and yielded equal dictionaries for all five graphs, not merely agreement of aggregate statistics. Each independently enumerates 4096 states for each of five explicitly labelled graphs. The catalog check yields one automorphism per graph and zero cross-isomorphisms for all ten graph pairs. The G5 sharp time-eight witnesses are 486 and 3609; corresponding full time-eight counts are exactly two, while G1–G4 have time-seven populations and zero time-eight population. The global power identity is checked for every state. No sampled experiment is used as a substitute for an exhaustive finite proof.

The result does not independently enumerate the historical catalogue of all cubic identity graphs or prove any assertion on cubic graphs of other orders. Independent external mathematical review remains unperformed.
