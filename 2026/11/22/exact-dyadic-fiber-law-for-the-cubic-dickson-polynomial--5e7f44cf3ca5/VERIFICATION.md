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

# Reproducible mathematical checks

The exact claim, domain, branch normalizations, and square-root formula are in `RESULT.md`. The standalone `verify.py` uses only the Python 3 standard library.

Run `python3 verify.py` in this directory. It enumerates all inputs and all targets modulo \(2^k\) independently for every integer \(1\le k\le16\), verifies the complete fiber law, ensures exactly \(2^{k-1}\) even images, and compares the observed maximal fiber and maximizing-target count with the closed theorems. Total evaluations and target comparisons: **131,070 each**. It additionally enumerates all squares modulo \(2^m\) for every \(1\le m\le12\) and checks the separate closed root count formula.

The executed checker completed without assertion errors, reporting a maximal fiber of \(257\) at exponent \(16\), attained by eight targets. At exponent \(15\) its maximal fiber was \(257\), attained by two targets. The initial levels verify the small-exponent exceptional table and the exponent-eight tie.

These are finite independent computations; no argument of the form “verified up to a bound, therefore all exponents” is used. The proof's unbounded part is the exact four-branch decomposition and 2-adic coordinate lemma. An independent audit has not been performed.
