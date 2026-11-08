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

# Verification notes

The finite support reduction has exactly \(9\times7\times7=441\) signatures. Each signature stores two distinguished colors and one tracked representative of each initially occupied ordinary color. The reduction is lossless for temporal entry times and periods because each color class shares the same ordinary-neighbor set. `support_checker.py` performs the full deterministic transition enumeration, verifies the nine by-support coefficient rows and the explicit three-step witness, and tests the resulting weighted expressions for \(2\le m,n\le11\).

An independent `direct_check.cpp` evolves each labelled vertex using its actual graph neighbors (it does not use the support quotient), enumerating all \(3^{m+n}\) configurations for each \(2\le m,n\le6\). It checks first-entry times, least periods and exact class populations. In total, it directly checked 1,185,921 labelled colorings on 25 graphs. Captured outputs are supplied as `support_check_output.txt` and `direct_check_output.txt`.

Replay with `python3 support_checker.py`, then `g++ -O2 -std=c++17 direct_check.cpp -o direct_check` and `./direct_check`. These commands require Python 3's standard library and a C++17 compiler.

The unlimited-parameter proof depends on the exact 441-case finite-state reduction and surjection weights; the independently checked finite graph sizes are corroborating tests only. This result has had self-review but no independent audit.
