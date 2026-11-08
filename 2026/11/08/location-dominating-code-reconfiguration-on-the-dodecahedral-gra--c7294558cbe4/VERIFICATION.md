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

# Reproducibility

Execute `python3 checks/verify_ld_python.py` and `c++ -std=c++17 -O2 checks/verify_ld_cpp.cpp -o /tmp/verify_ld && /tmp/verify_ld` from this document's enclosing directory. The Python source constructs the dodecahedral edges as 30 unordered pairs and enumerates all combinations up to size seven; C++ scans all 1,048,576 masks and evaluates the same mathematical criterion by a separate implementation. For every size-seven optimum, each tests all 7×13 possible deleted/inserted vertex pairs, and all-pairs BFS verifies distances.

Successful Python output:

```
PYTHON_LD_PASS gamma_LD=7 optimal_states=220 legal_edges=570
PYTHON_LD_PASS TJ_equals_TS=yes degree_profile=4:120,6:40,7:60 connected=yes radius=8 diameter=9
```

Successful C++ output:

```
CPP_LD_PASS min=7 count=220 edges=570 degree_profile=4:120,6:40,7:60
CPP_LD_PASS all_valid_jumps_are_slides=yes connected=yes radius=8 diameter=9
```

The exact same sources are part of this package, so the finite certificate does not depend on externally hosted code, a saved log, or a selected sample. Exhaustive enumeration proves this individual finite instance, not an infinite family; the runtime output itself is not proof in isolation. Historical-priority assessment is separate and may require further literature review.
