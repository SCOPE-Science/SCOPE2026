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

# Reproduction
Compile and execute `verify.cpp` with `g++ -O2 -std=c++17 verify.cpp -o verify && ./verify`. The final line must be `UNICYCLIC_WALSH_CERTIFICATE_PASS`. The source enumerates graphs by connectivity of exact-edge subsets and independently by unique cycles plus rooted forests. It performs exact integer Walsh transforms and independently checks every five- and six-vertex frequency using direct signed sums and signed net-Laplacian minors.

At five vertices the checker reports `zeros=212`, `rank=812`, and `projection_abs_sum=8104/1024`. At six vertices it reports `zeros=1200`, `rank=31568`, `min_nonzero=4`, `projection_abs_sum=580928/32768` and the weight-zero census `4:420 7:180 8:180 11:420`. Exactly 420 four-edge frequencies have degree pattern `(0,1,1,2,2,2)` and all other four-edge signings are nonzero. The output in `SPECTRA.txt` is a reference transcript of the actual checker execution.

# Limits
The numerical census is exhaustive only for the specified finite groups. The general congruence-class invertibility theorem is proved by the unsigned count and parity argument in `RESULT.md`. No third-party formal or mathematical validation has been performed.
