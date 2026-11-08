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

# Verification and scope

The analytical proof covers every finite field of characteristic greater than three and every nonempty retained frequency mask, not only the checked prime fields. The key proof obligations are (i) uniqueness of unordered two-sums with nonzero total on the cubic graph, (ii) the exact zero-fiber correction identity, (iii) the inactive-mask Cauchy--Schwarz equality conditions, and (iv) weighted Cauchy--Schwarz and phase alignment for the active branch. All are given directly in RESULT.md.

The checker `verify_cubic_erasures.py` is standalone and uses only the Python standard library. Execute `python3 verify_cubic_erasures.py`. It enumerates 2,555 masks across prime fields five, seven and eleven, adds 350 sampled masks over thirteen, checks every predicted equality vector via direct pair-sum convolution, and independently checks the exact fiber formula and upper bound on 5,109 complex integer test vectors. The expected terminal line is `CUBIC_ERASURES_VERIFY_PASS masks=2555 random_tests=5109 primes=5,7,11,13`. The finite replay corroborates the proof but does not establish universality or mathematical priority.

No independent audit has been performed. Source-priority comparisons are provisional. The phase transition makes no statement for characteristic two or three, higher moments, or a different frequency normalization.
