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

Run `python3 verify.py` with Python 3.9 or later; no external libraries are required. This standalone program checks the three exact generator identities, the proposed finite Apéry index set and its distinct residues, and compares every residue minimum with independently computed shortest paths. It then independently reconstructs the pseudo-Frobenius set, Frobenius number, and genus. It checks 52 odd parameters, from 7 through 99 and five larger cases through 251.

Expected first output line: `APERY_PF_FROBENIUS_GENUS_EXACT_OK 52 n_min 7 n_max 251`. The finite experiment is supporting evidence; the proof in `RESULT.md` is the infinite-domain argument. No independent mathematical audit has been carried out.
