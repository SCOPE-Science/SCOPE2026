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

# Verification instructions and limits

Run `python3 verify_vectorized.py` with Python 3 and NumPy installed. Independently run `g++ -O3 -std=c++17 -Wall -Wextra -pedantic verify_direct.cpp -o verify_direct`, then run `./verify_direct`. Both programs are standalone and construct the finite graph internally. The two attached outputs, `verification_output.txt` and `verification_direct.txt`, were obtained by running the packaged sources.

The vectorized method enumerates every base-three input, directly constructs each transition, performs exact indegree peeling, classifies cycles and entrance depths, and computes basin populations. It also computes the 48 cube isometries, the compatible three-color shifts for CCA only, and the exact joint eventual periods. The direct C++ method enumerates all initial states by following paths and detecting trail repeats; no NumPy, prior result file, external database, or approximate experiment is needed. Both algorithms reproduce the same orbit/basin/depth histograms and maximal transient bounds.

The exhaustive classification verifies a **finite** mathematical claim, not an infinite-dimensional or arbitrary-graph theorem. The computations and source texts have received self-review; independent audit has not occurred. No historical-priority certification is asserted.
