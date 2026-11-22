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

# Verification instructions

Run `python3 checks/verify.py` from the extracted directory using Python 3 and its standard library only.

The program constructs exactly 16,257 distinct state codes, evaluates the two prescribed bfloat16 finite dynamical systems entirely in `fractions.Fraction`, independently checks nearest-even rounding by neighboring-value search and by exponent-quantum integer quantization, and decomposes each graph both by forward-path discovery and indegree peeling. It asserts all six recurrent components' periods/basin sizes/maximal preperiods, verifies 1,371 distinct edges, and prints their exact code lists.

The expected leading line is `CHECK_OK,states=16257,disagreements=1371`. The proof is a complete enumeration of a finite set using exact arithmetic and two independent graph decompositions, not a claim of a machine-checked theorem over the real numbers. Reproduction has no dependency on hardware bfloat16 support. Prior literature comparisons are necessarily incomplete and independent mathematical audit has not been performed.
