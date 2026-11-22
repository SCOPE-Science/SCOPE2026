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

Run `python3 verify_py.py` and `c++ -std=c++17 -O2 verify_cpp.cpp -o verify_cpp && ./verify_cpp` after extracting all files into the same directory. Both independently generate every seven-cell subset of the five-by-five rook board, verify all closed-neighborhood signatures, build the full one-replacement graph on the optimum codes, and run breadth-first search from a canonical optimum. Both programs completed successfully with the following exact output invariants:

- \(480700\) seven-cell candidates; \(7200\) feasible optimum codes
- degree \(14\) for each code; \(50400\) undirected exchange edges
- one connected component; radius and diameter \(9\)
- shell sizes \((1,14,81,208,504,1024,1696,2184,1352,136)\)

The stand-alone proofs for the all-odd-order statements are the structural component and local-move arguments in RESULT.md, not these finite checks. The pre-existing static optimum theorem is explicitly credited. No external/independent scholarly audit has been completed.
