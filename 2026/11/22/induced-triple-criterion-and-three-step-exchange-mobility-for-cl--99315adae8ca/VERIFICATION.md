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

The executable checks are the complete standalone `verify_python.py` and `verify_cpp.cpp` source files included alongside this document. Run:

```sh
python3 verify_python.py
c++ -std=c++17 -O2 verify_cpp.cpp -o verify_cpp
./verify_cpp
```

The two programs build the sixteen-vertex Cayley graph from XOR differences `1,2,4,8,15`. Python tracks observed vertex sets explicitly; C++17 uses a separate bit-mask closure. Both enumerate all 65536 possible initial sensor sets, check exactly 320 successful minimum triples and exactly sixty failed four-sets, confirm unique extension of all 240 failed triples, and reconstruct all 320 vertices and 3360 edges of the optimal three-set exchange graph. Their independent all-root breadth-first searches establish distance profile `(1,21,126,172)` for each root. All successful placements complete observation in at most one forcing wave after neighborhood observation.

Expected final lines begin `PYTHON_VERIFY_OK` and `CPP_VERIFY_OK`, respectively. No probabilistic computation, time-limited search or external database is used as a correctness certificate. The checks establish a finite theorem on the stated labelled graph only. No independent external validation has been performed.
