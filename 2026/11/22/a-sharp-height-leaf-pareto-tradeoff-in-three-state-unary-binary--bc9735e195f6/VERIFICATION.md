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

# Reproduction and scope

The two C++17 programs enumerate all 531441 labeled unary and binary transition tables on three states. Run `g++ -O2 -std=c++17 verify_height_leaves.cpp -o v1 && ./v1` and `g++ -O2 -std=c++17 verify_pareto.cpp -o v2 && ./v2`. Their terminating exhaustive recurrences independently reproduce the joint minimum-height/minimum-leaf histogram and all Pareto frontiers. They make no inference beyond the specified three-state unary–binary domain. Publication priority and independent mathematical review have not been independently certified.
