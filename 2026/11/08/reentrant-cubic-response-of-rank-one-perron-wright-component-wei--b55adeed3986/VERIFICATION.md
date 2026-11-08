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

# Reproducible checks and their limits

Install the dependency from `requirements.txt`, then run `python verify.py` in the same directory. The checker uses exact symbolic algebra for series inversion and exact rational arithmetic for the two-type sign polynomial and its concrete positive example; it also exhausts weighted labelled trees on two to five vertices using the Prüfer/Cayley identity and checks the exact one-type gauge. The checker prints a count of passing tests and stops with an assertion error on any mismatch.

The proof in `RESULT.md` additionally uses the analyticity and uniform shrinking-neighborhood component-enumeration theorem established by Hu and Sun (arXiv:2610.23003v1, Theorem 3.6, equations (3.12) and (3.13)). That infinite-size theorem is not certified by the accompanying finite checker. The checker does not establish absence of stronger prior results or conduct an independent audit.
