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

Run `python3 checker.py` with Python 3 and SymPy installed. The executed command returned:

`ALTERNATING_JAMILOV_EXCEPTIONAL_POINT_OK symbolic_Jordan_powers=8 rational_trajectories=220`

The checker verifies the symbolic characteristic polynomial, discriminant factorization, a nontrivial nilpotent Jordan component on the sum-zero plane, eight exact Jordan power identities, and 220 exact-rational four-species trajectories and normalized two-season recurrences. It additionally tests the spectral discriminant signs on either side of the critical parameter. The proof in `RESULT.md` supplies the uniform parameter inequalities, exact recurrence for all times, and infinite-time asymptotics; the finite tests are not a certificate of an infinite statement. The literature check examined the primary original full text, a full text of the closest open-access later superposition paper, and general spectral background; at least one similar journal article was accessible only through its abstract. No independent audit is represented.
