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

The standalone `verify_alliance.py` program constructs the clique windmill directly and applies the defensive inequality to every selected vertex. For each qualifying set it checks **every nonempty proper subset** to determine global minimality. It compares the resulting complete cardinality coefficient dictionary to the formula, without using the structural classification to generate the purported minimal sets.

Run `python3 verify_alliance.py` from the same directory as this file. The code uses only the Python standard library.

Observed execution:

`VERIFY_OK profiles=495 examined_subsets=1462825 alliances=501626 globally_minimal=11226 local_not_global=127877 all_polynomials=PASS friendship_gaps=PASS`

The 495 checked input profiles have 2–4 labelled petals with each size 1–5 and total petal size at most 12. The code also confirms the exact two-term friendship specialization algebraically for 2–29 petals and independently checks a local-versus-global minimality counterexample. The number of independent candidate vertex subsets checked is 1,462,825. An exhaustive finite experiment is not an exhaustive proof for arbitrary petal sizes; the unrestricted result is proved mathematically in `RESULT.md`.
