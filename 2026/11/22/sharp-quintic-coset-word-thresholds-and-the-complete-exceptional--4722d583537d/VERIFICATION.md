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

# Verification record
The self-contained source `verify_quintic.cpp` was compiled with C++17 and executed. It enumerates 836 eligible primes at most 31126, reconstructs their fifth-power colors both by discrete-log enumeration and independent coset construction, compares all 125 histogram counts, and verifies the 48 all-word and 43 mixed-word exceptional primes. The boundary prime 2311 misses the all-zero word and a mixed word; 2411, 2731, and 3331 miss only the all-zero word; 2341 and 3361 exhibit all words. The inequality \(125N_{\mathbf c}(p)\ge p-176\sqrt p-75\) is mathematical proof for the untested infinite prime tail, not a numerical extrapolation. The classical Weil character-sum theorem is invoked, not independently certified. No independent audit has been performed.

Run: `g++ -std=c++17 -O2 -Wall -Wextra verify_quintic.cpp -o verify_quintic && ./verify_quintic`
