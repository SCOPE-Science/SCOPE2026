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

# Exact verification and its limits

Run `python3 verify_pellytope_faces.py` using the included standalone Python file. It requires the Python standard library only. The script was executed from the actual packaged file and passed 201 exact assertions. The computations compare independent chord-compatibility enumeration in dimensions 1 through 7 with the derived face formula and check the algebraic recurrence and h-transforms through dimension 50. Finite computations cannot establish infinite dimensional claims; the proof is the fully quantified fan-subdivision and spectral argument in `RESULT.md`.

The cited geometric inputs are the normal fan construction and endpoint links in Bossinger–Telek–Tillmann-Morris (arXiv:2410.08002, Proposition 3.1 and Lemma 3.3). All outputs are integer exact. No external mathematical audit was performed.
