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

# Verification and limits

The proof in RESULT.md is all-length and uses the previously established bond theorem, a unique maximal-singleton-run decomposition, a rational generating function, independent Bernoulli cuts and a two-dependent central limit argument. The two packaged programs supply reproducible finite checks, not an external or infinite certification.

Run `python3 verify_direct.py` to enumerate direct standardized single-deletion sets for all layered permutations through length twelve, and `python3 verify_distribution.py` to compare two independent finite distribution algorithms through length thirty. Expected stdout is included in `direct_output.txt` and `distribution_output.txt`.

The exact mean applies for lengths at least three; exact linear variance applies for lengths at least five. The smaller cases are separately explicit. No independent audit has been performed.
