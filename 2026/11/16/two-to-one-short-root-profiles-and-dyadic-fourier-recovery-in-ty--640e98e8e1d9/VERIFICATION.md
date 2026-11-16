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

# Exact verification

Running `python3 short_root_fourier_check.py` rebuilds the type-C root order using integer simple-root coordinates, constructs ideals by independent breadth-first and antichain down-closure methods, verifies two-to-one short-root profile fibres through rank eight, and computes all Walsh multipliers in ranks two through five using integer Walsh-Hadamard transforms. The checked pairs (rank, zero count, convolution rank) are (2,0,4), (3,18,46), (4,0,4096), (5,126056,922520). The rank-six signed character with frequency mask 524545 divides the 924 full ideals into 462 and 462. The expected completion marker is `SHORT_ROOT_C2_C8_FOURIER_PASS`.

Running `c++ -O3 -std=c++17 short_root_direct_check.cpp -o verify` and then `./verify` performs independent direct exact character sums over all frequencies in ranks two through five; its completion marker is `SHORT_ROOT_DIRECT_CHARACTER_PASS`. Both programs were executed successfully with no numerical tolerance. The twelve rank-four marginal counts are recorded in `C4_MARGINALS.tsv`, and the compact census is in `SPECTRUM_SUMMARY.tsv`.

Finite checks do not prove the infinite result, which instead follows from the long-short spine and the two-to-one lift proof in `RESULT.md`. No full rank-six Fourier transform, converse in arbitrary ranks, or independent mathematical audit is claimed.
