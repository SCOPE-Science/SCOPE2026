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

The result is a finite exact theorem about the explicitly defined 24-vertex McGee graph. Complete enumeration checks all 1,961,256 ten-vertex and 2,496,144 eleven-vertex candidate codes, then all one-vertex replacement possibilities for the 384 optimal states.

Run `g++ -O3 -std=c++17 verify_cpp.cpp -o verify_mcgee`, then `./verify_mcgee`, then `python3 verify_python.py`. Both programs must print `VERIFY_OK`. The C++ checker independently forms and compares 24 closed-neighborhood signatures, while Python uses all 300 nonempty hitting constraints. Each reconstructs the jump/slide graphs from the masks. Python also checks the component's two glued four-cliques and pendant-leaf placement exactly.

The enumeration assumes the displayed labelled LCF graph; it does not assert a theorem for graphs of larger order, larger codes or multi-detector failures. The absence of 10-vertex codes combined with the proved analytic lower bound and 384 size-11 codes establishes the optimum. Component counts and isomorphism shape are determined by complete finite graph traversal, not experiments from partial data.

Publicly available prior work already established the minimum and the 384-mask census. No independent scholarly audit of the new exchange classification has been performed.
