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

Two self-contained Python 3 scripts reproduce the finite checks using only the Python standard library. Run `python3 verify_bruteforce.py` and `python3 verify_decomposition.py` from their containing directory.

The direct program checks every allowed binary string of every length from \(1\) to \(21\), examining all positive proper border lengths and comparing its Hamming-weight spectrum to the proposed recurrence. The alternative implementation counts shortest-border sandwiches by polynomial convolution and compares with independently written recurrence coefficients through length \(150\). The latter computes certified intervals for the limiting density at truncations \(K=10,20,40,60,100\), using a proved tail estimate \(\varphi^{2-K}\) and decimal arithmetic with 60-digit precision. These finite checks passed.

The all-length proof is in RESULT.md, including the disjoint shortest-border argument, exact middle-language generating series and the Binet limit. No finite experiment is presented as an infinite proof; no independent mathematical review has been conducted.
