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

# Exact verification and limits

The result has four proof components: an analytic all-horizon invariant for at most three machines, an explicit adaptive five-chore obstruction on four machines, a finite exhaustive certificate that four-machine streams of at most four chores admit online exact PROP1, and an all-population two/three-arrival adversarial threshold for at least five machines.

Execute `python verify.py` with Python 3.10 or later. The run checks 91 feasible lattice discrepancy triples (364 min-discrepancy transitions), 16,105 non-singleton eligibility streams of length at most four, exact minimax reachability at horizons four and five, and 108 branches of the explicit adaptive adversary. The expected observed checks include `three invariant (91, 364)`, `four greedy prefixes 16105`, and `adversary (108, [0, 0, 0, 12, 0, 96])`.

Also execute `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_independent.cpp -o verify_cpp && ./verify_cpp`. It enumerates all 54,241 eligibility-set sequences of lengths zero through four, including singletons, calculates allocations directly from current loads and proportional shares, and verifies exact PROP1 at each step. Expected output: `Direct all-eligibility 4-job prefixes checked: 54241; allocation transitions: 54240`.

Integer arithmetic with denominator 12 handles all eligible-set sizes on four machines; denominator 6 handles all sizes on three machines. The proof is complete because the finite enumeration covers every possible eligibility sequence of the claimed finite horizon, including adaptive realizations. No finite check is offered as an infinite-horizon theorem. Separate analytic arguments establish the unlimited-horizon three-machine guarantee, the five-chore obstruction at four machines, and the three-chore obstruction and two-chore feasibility bound at all larger populations. No external independent review or certification has been performed.
