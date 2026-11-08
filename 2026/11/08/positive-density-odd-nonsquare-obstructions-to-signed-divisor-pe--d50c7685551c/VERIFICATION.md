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

## Reproducibility
Run `python3 verify.py` in the directory containing this file. The program calculates exact divisor sums, checks the factorization and abundance of the odd square core, and validates the strict subset-sum obstruction for four concrete odd nonsquare cofactors. The observed output is included in `verification_output.txt`.

## Infinite checks and boundaries
The proof of positive lower density is symbolic and uses a fixed finite primorial, inclusion-exclusion for integers coprime to that primorial, an absolutely convergent divisor-square series, and Markov's inequality. None of the finite examples can establish this density claim. The script tests neither all cofactors nor a density threshold; no independent mathematical audit has been performed.
