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

# Reproducibility and validation limits

Two self-contained source files accompany this result. To run the first, execute `c++ -O3 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive && ./verify_exhaustive`. To run the second, execute `python3 verify_walsh.py`. Neither requires a third-party package.

The C++ implementation enumerates every \(3^{16}=43{,}046{,}721\) spin-one assignment on the folded four-cube, with independent integer energy updates. It checks both off-critical endpoints, the complete critical population and the absence of other critical occupancy sectors. The reported output is `PASS exhaustive_states=43046721 critical=51 occupied_full=10 occupied_half=40 empty=1 strict_below=10 strict_above=1`.

The Python implementation verifies the folded-cube adjacency eigenvalues and critical-state energy and two-point covariance for dimensions \(4,6,8\), with predicted populations \(51,99,163\). For dimensions four and six it additionally searches half-integral affine coefficient tuples independently. Its three cases report `PASS`.

Computational checks are finite and cannot by themselves certify a theorem for all even dimensions. The proof uses the exact adjacency spectral bound, the classification of all ternary affine functions of independent signs, and a closed pair-sign sum for correlations. It assumes uniform positive antiferromagnetic exchange, no external magnetic field and zero temperature. Originality is based on examined sources and remains historically provisional. No independent scientific audit has been performed.
