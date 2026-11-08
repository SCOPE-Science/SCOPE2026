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

# Reproducibility and boundaries

Run `python3 check.py` in the directory containing the extracted files. Python 3's standard library is sufficient. The observed output was `PASS: 20483 exact rational assertions`.

The checker exhaustively sums independent edge-state patterns and uniformly chosen sources on paths of three through nine vertices at three rational edge probabilities; all marginals and joint events are compared to the exact formulas. It verifies the polynomial-CDF positivity certificate for all path lengths three through one hundred, cross-checks the conditional one-edge coefficient for all distinct pairs through thirty vertices, and checks endpoint strict negativity for a further finite rational grid. The script is not an independent proof of the universal statements; the proof in `RESULT.md` establishes the arbitrary-length claim, including the root existence and large-length expansion.

No empirical outbreak data, formal theorem prover, external independent assessment, or field validity are claimed. The primary scientific limitations are independent undirected bonds, one uniform seed, finite paths, and eventual rather than contemporaneous infection.
