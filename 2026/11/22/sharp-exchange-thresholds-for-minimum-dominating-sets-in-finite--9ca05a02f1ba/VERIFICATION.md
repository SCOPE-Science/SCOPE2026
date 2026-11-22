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

# Verification
The accompanying standalone programs construct affine planes of orders two, three, and four from field arithmetic, and check every predicted optimum and all pairwise exchange costs. The C++17 checker enumerates **all subsets of size at most the asserted optimum**; the Python checker separately enumerates the mathematically forced point–line split. Both passed. `CHECKS.txt` contains exact outputs. Rerun using `python3 verify_affine.py` and `g++ -O2 -std=c++17 verify_affine.cpp -o verify_affine && ./verify_affine`.

For arbitrary finite affine planes, the proof in RESULT.md is the justification. The finite computation is not a substitute for that proof. The lower-bound, collinearity and pair-intersection steps hold without field assumptions. The original domination number was already established in a 2016 publication, and the present claim is the minimum-set exchange threshold. External independent validation has not been performed.
