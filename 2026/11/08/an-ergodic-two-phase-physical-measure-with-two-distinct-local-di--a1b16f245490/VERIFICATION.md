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

Reproduce with `python3 verify_markov.py` using Python 3 and no third-party dependencies. The program compares all binary words through length 10 with both the renewal Markov formula and the original minimum-inverse-length formula, checks normalization exactly, exhaustively enumerates all 15-bit uniform inputs against output lengths 1–4 with exact unresolved-mass bounds, and checks strict entropy inequalities. It completed with `PASS 2090 exact arithmetic and finite-input checks` and printed local dimension `0.9182958340544897`.

Analytically, Step 1 of RESULT.md proves the one-step image law by geometric waiting times; Steps 2–3 combine published preservation and mixing for the second iterate with ergodic theorems; Step 4 proves the exact two-valued Euclidean local dimension using Markov transition frequencies, Bernoulli frequencies, and Borel–Cantelli terminal-run control. Tests of finite words do not establish mixing of the square or the infinite pointwise limits; these are attributed and proved as appropriate. The principal limitation is a short combination of strong existing theorems, so the novelty assessment remains subject to independent literature verification.
