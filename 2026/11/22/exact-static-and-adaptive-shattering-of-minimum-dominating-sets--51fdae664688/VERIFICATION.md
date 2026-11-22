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

# Exact finite verification and scope

The two programs cover all size-at-most-six dominating candidates, then all query supports through five vertices, using complete finite loops. Independent adjacency encodings are the middle two Boolean levels and the generalized Petersen model \(GP(10,3)\). The shipped vertex permutation is verified against all thirty edges by `replay_certificates.py`, and the supplied 64-leaf online decision tree is checked path by path against the reconstructed concepts. The boundary matrices are built from every enumerated face and reduced over \(\mathbb F_2\).

Commands after extraction into one directory:

```sh
python3 verify_middle_levels.py /tmp/desargues-generated-tree.json
c++ -O2 -std=c++17 verify_gp103.cpp -o /tmp/desargues-gp-check
/tmp/desargues-gp-check
python3 replay_certificates.py .
```

The first program regenerates, rather than reads, the shipped tree; the third replays the shipped one and checks vertex-model isomorphism. All expected values are printed or asserted by code.

Limits: These are exact finite proofs for one graph, not statements about all cubic graphs or all generalized Petersen parameters. Homology is only over \(\mathbb F_2\). No external independent mathematical audit is claimed. An undetected independent published equivalent is a historical-priority risk.
