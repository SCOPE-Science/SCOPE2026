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

This is an exact finite computation, not an external proof certification.

Run `c++ -O2 -std=c++17 even_cycle_verify.cpp -o verify && ./verify` and separately `python3 even_cycle_verify.py`, with `witnesses.json` in the same directory as the Python file. Both run without external packages or network access. Each implementation builds the 15 matchings and 105 differences, determines all shattered supports, verifies the face and facet counts, and computes mod-two reduced boundary ranks `1,14,91,284`. The Python implementation additionally checks 64 explicit representative traces, identifies the four facet types, and checks that a support is shattered exactly when it is a subset of a four- or six-cycle with at most four edges.

Expected independent outputs include the f-vector `1,15,105,375,675`, 675 four-edge facets, and sole nonzero reduced Betti number `391` in dimension three. No assertions are made about larger complete graphs or integral homology.
