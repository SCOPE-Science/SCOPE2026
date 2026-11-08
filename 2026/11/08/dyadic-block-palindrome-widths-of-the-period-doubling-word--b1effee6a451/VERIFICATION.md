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

# Reproducibility and limits

The proof in `RESULT.md` establishes the theorem for every dyadic exponent from the valuation identity and the shortest-border characterization. No external formal proof assistant or independent audit is claimed.

Run the standalone verifier with `python3 verify.py` (standard Python 3 only). It checks all dyadic exponents from zero through thirteen, the exact predicted border lengths for the even cases, the doubling of shortest-border lists under the morphism for the odd cases, full maximization by a separate exhaustive border-choice dynamic program for exponents through eight, and all nonempty binary words through length ten.

Actual checker output begins with:

`VERIFY_OK dyadic_levels=14 max_prefix=8192 full_optimum_levels=9 all_binary_words=2046 border_steps=8172`

These are finite reproducibility checks. They do not establish a universal theorem without the independent mathematical argument already provided in `RESULT.md`.
