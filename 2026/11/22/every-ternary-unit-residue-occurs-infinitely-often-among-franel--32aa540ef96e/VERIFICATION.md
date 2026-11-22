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

# Reproducibility

Compile `check_franel.cpp` with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic check_franel.cpp -o check_franel` and run `./check_franel`. The checked residue modulus is 729, with exact modular Pascal coefficients, all indices below 6561, all units below moduli 3, 9, 27, 81 and 243, and all valid block shifts within the generated range. The stored output is `CHECKS.txt`.

These finite checks cannot prove arbitrary prime-power modulus or infinitely many witnesses. The universal proof is in `RESULT.md`. No independent mathematical audit was performed.
