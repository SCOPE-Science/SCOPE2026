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

# Reproducibility and limits

The file `finite_certificate.py` enumerates all \(4(2^{10}-1)=4092\) hub/occupied-type supports. Its state update is a direct rewrite of the stated local excitation rule. It checks that every support first reaches all-rest in at most seven iterations; the necessary-and-sufficient condition for first reach at update seven; and all eight signed coefficients of \(E_t(k)\) derived by exhaustive type-support inclusion–exclusion. Run `python3 finite_certificate.py`. The actual captured stdout is embedded in `finite_certificate_output.txt` and ends with `finite_certificate: PASS`.

Independently, `full_state_census.cpp` updates vertices on the complete adjacency pattern directly and tests every one of the \(4^{2k+1}\) labelled configurations for each integer \(1\le k\le5\), totaling \(4,473,920\) starting states. It compares every first-extinction population with its mathematical formula. Run `g++ -std=c++17 -O3 full_state_census.cpp -o full_state_census && ./full_state_census`. Its captured stdout, embedded as `full_state_census_output.txt`, ends with `full_state_census: PASS`.

The all-size proof is the hub/support quotient plus exhaustive evaluation of its finite 4092-case domain; finite small-graph simulation alone would not imply the theorem. The scripts are ordinary source-code proofs/checks with no third-party dependency or external mathematical certification. No independent mathematical audit has been performed. See `RESULT.md` for assumptions, source comparisons and unproved extensions.
