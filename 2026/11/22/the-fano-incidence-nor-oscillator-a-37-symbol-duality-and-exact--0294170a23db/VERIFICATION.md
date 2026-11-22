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

# Finite verification

Run `c++ -O2 -std=c++17 heawood_nor.cpp -o heawood_nor && ./heawood_nor` and `python3 verify_duality.py`. Both commands completed successfully using the packaged source files. The C++ program tests all 16,384 Boolean initial configurations; the Python program independently computes all 128 possible subsets on each shore and uses the closure-fiber formula for the complete attractor basin table. Exact outputs are transcribed to `census.txt`.

The analytic proof, not the programs alone, establishes completeness and the one-update bound for this precise finite network. In particular the exact total basin mass is 16,384 and the 703 attractor basin-size multiset has the counts claimed. This does not validate perturbed graphs, different update conventions, or historical novelty. Independent external mathematical audit has not been performed.
