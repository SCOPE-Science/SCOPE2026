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

The independently constructed projectors in `verify.py` reproduce the two expected two-step quadratic forms exactly; off-diagonal terms vanish in the bisector basis. The crossover value and all four rational example factors follow by exact symbolic substitution. The script tests exact optimality inequalities at 19 rational overlaps, 39 rational relaxations and 51 rational coupling values, with additional endpoint and crossover tests. Executing `python verify.py` using `requirements.txt` produces the output stored in `verify_output.txt`.

The proof in `RESULT.md` proves the statements for every real parameter in the stated open domain. Exhaustive symbolic identities support the algebra; a finite parameter grid is not an infinite-domain proof. No randomized numerical verification is presented as an exact certificate. The result concerns only two-step, fixed-relaxation Kaczmarz with the specified uniform-marginal couplings and worst-initial-direction expectation. Independent audit has not been performed.
