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

# Reproducibility

Run `python verify_schur_half_lattice.py` with Python 3 and the dependency in `requirements.txt`. The checker reads only its internal transcription of the published thirty-two incidence triples and the displayed integer certificates. It constructs the \(24\times24\) Gram matrix over \(\mathbb Z\) and verifies all adjacency multiplicities, rank, characteristic polynomial, Smith normal form, twelve-line divisor indicator and modular nonmembership obstruction. It also checks column Hermite normal form membership for \(H\) and \(3H\).

The run on the included files succeeded with all five expected success messages. The source incidence data are proved in Naskręcki–Pokora, Proposition 3.5 and Appendix B; they are not being re-established by this arithmetic checker. No full Néron–Severi basis, primitive-closure computation or independent mathematical audit is claimed.
