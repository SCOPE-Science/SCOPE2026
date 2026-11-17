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

Run `python3 transfer_check.py` with Python 3.8 or later. This program independently builds the finite transfer graph from the eight-neighbor update condition, finds recurrent components by a two-pass graph traversal, computes integer traces and characteristic polynomials by Newton identities, and checks Perron spectral intervals by exact integer-vector inequalities. It prints the counts through circumference fifteen. It uses no external packages.

Build the second checker with `g++ -O3 -std=c++17 direct_check.cpp -o direct_check` and run `./direct_check`. It enumerates every binary initial configuration of the actual periodic Moore lattice for circumferences three through seven, with neighbor sums constructed directly from bit columns. Its five pairs of counts agree with the transfer results. Exact observed outputs are in `transfer_output.txt` and `direct_output.txt`.

The transfer argument covers every integer \(n\ge3\); the finite direct enumeration alone covers only \(3\le n\le7\). Both checks reproduce the fixed-state census, not the entire dynamical phase portrait. The characteristic polynomials and strict spectral bounds establish the stated asymptotics mathematically, conditional on the fully specified, finite integer calculation. No external mathematical audit is claimed.
