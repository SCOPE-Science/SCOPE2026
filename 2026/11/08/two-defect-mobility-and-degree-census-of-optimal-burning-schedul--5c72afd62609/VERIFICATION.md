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
# Reproducibility and mathematical limits

The finding concerns simple labeled cycles \(C_{k^2-2}\), for integers \(k\ge3\), with strict time-labelled optimum ignition schedules. The proof covers every such \(k\) and does not rely on extrapolation from finite tests.

Two standalone implementations are included. Run `python3 construct_check.py` to check generated gap encodings against direct graph-distance balls and ignition-order constraints, including complete direct tuple comparison at \(k=3,4\) and structured testing through \(k=7\). The recorded output is `construct_check.out` and ends with `CONSTRUCT_CHECK_OK`.

Compile `g++ -std=c++17 -O3 direct_exhaustive.cpp -o direct_exhaustive` and run `./direct_exhaustive`. This program generates schedules independently from the graph metric and performs exhaustive source-slide adjacency and component searches at \(k=3,4,5\). The recorded output is `direct_exhaustive.out` and ends with `DIRECT_EXHAUSTIVE_OK`. In these tests, graph sizes are 56, 672 and 7,176 schedules, split into 2, 6 and 24 components respectively. The two finite methods agree with the proven formulas.

These checks do not establish previously unknown historical priority or independent scholarly certification. Proof details, scope and scientific limits are in `RESULT.md`.
