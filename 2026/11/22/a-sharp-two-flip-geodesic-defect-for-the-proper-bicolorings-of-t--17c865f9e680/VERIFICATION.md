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

# Exact finite verification

Execute in the directory containing the accompanying programs:

```
python3 check_projective.py
c++ -O2 -std=c++17 check_singer.cpp -o check_singer
./check_singer
```

`check_projective.out` and `check_singer.out` contain the independently reproduced 468-state, 702-edge, diameter-13 classification. The field-coordinate implementation checks the projective `2-(13,4,1)` incidence structure, enumerates all 8192 color assignments, builds the one-bit-flip adjacency, and runs breadth-first search from every valid state. The C++ implementation generates the line system from the cyclic Singer difference set `{0,1,3,9}` and independently checks the same incidence structure, including a specific isomorphism to the field-coordinate labeling. The two programs independently compute all 109278 unordered-pair distances. Both checks executed successfully in this package's preparation environment.

The exact all-pairs computation proves only this finite instance. The public priority comparison does not constitute independent scholarly validation. No expert or formal certificate is claimed.
