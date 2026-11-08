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

The full theorem follows from an explicit bijection between period-two configurations and closed walks of a size-16 transfer graph, plus three fixed-size exact determinant identities. These matrices are constructed directly from the local majority constraints; the asserted identities are checked in `code/transfer_certificate.py` using integer Newton identities, without using numerical eigenvalue approximations. Closed-walk counting does not quotient by spatial rotation.

For an independent finite check, the C++ program `code/direct_census.cpp` implements the actual graph update with bit operations. It examines all \(4^n\) global states for every \(3\le n\le11\), checking both iterates, fixed states and all-vertex-flipping two-cycle states.

Reproduce from the package root with:

```
g++ -O3 -std=c++17 -Wall -Wextra -pedantic code/direct_census.cpp -o /tmp/sunlet_majority_census
/tmp/sunlet_majority_census
python3 code/transfer_certificate.py
```

The expected exact standard outputs are stored in `results/direct_census.stdout` and `results/transfer_certificate.stdout`. The former covers \(4,194,304\) global states at \(n=11\); the latter independently checks characteristic factors and trace formulas for \(3\le n\le30\).

The range-limited state enumeration cannot prove a formula for all \(n\). The all-size proof rests on the transfer encoding and algebraic factorization; no basin or transient-time enumeration is claimed. Scientific priority is qualified by the possibility of earlier unindexed work. No independent external audit or certification has been undertaken.
