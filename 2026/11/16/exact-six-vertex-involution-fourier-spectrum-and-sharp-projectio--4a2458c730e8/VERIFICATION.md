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

Exact verification relies on a 15-bit signed-matching representation, not on direct construction of a \(2^{36}\)-entry operator. The reduction from the original additive matrix characters is proved in `RESULT.md`.

Two genuinely different algorithms were executed:

* `check_spectrum.cpp`: enumerate all 76 matching incidence masks and apply the exact integer Walsh-Hadamard transform; separately compute all relabeling orbits and the exact projection kernel mass.
* `check_spectrum.py`: for each one of the 32768 signed graphs, recursively sum over remaining fixed and paired vertices; then apply an independent exact integer Walsh-Hadamard transform to the nonzero mask.

The two ordered signed-multiplier vectors agree byte-for-byte in little-endian signed 32-bit form. Their SHA-256 is `622bf9900d5a6d9a43e681e8e32a8d28c8c111e85ced8c12fdbefbae7093b134`.

Both methods check zero count \(6825\), nonzero count \(25943\), least positive absolute multiplier \(4\), the 19 exact signed levels, the negative-edge-count distribution \(480,2880,2280,1185\) at sizes \(5,7,9,11\), and exact Parseval identities. The C++ code checks 26 relabeling orbits and their size histogram; its `orbit_table.csv` output matches the included certificate. Both methods compute the integer sum of absolute inverse-mask Fourier coefficients \(1\,524\,338\), giving sharp endpoint norm \(762169/16384\).

Success markers: `INVO_FOURIER_CPP_PASS` and `INVO_FOURIER_PYTHON_PASS`.

Compiler: `g++ -O2 -std=c++17 -Wall -Wextra -pedantic check_spectrum.cpp -o check_cpp`. Execute `./check_cpp spectrum.bin orbits.csv`, then `python3 check_spectrum.py`. No third-party packages or data downloads are required.

Limits: the computation exhausts precisely fifteen signed graph edges; it is not an infinite-order spectrum calculation. The mathematical independence of an external auditor is not claimed.
