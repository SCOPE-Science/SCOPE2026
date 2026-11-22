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

# Reproducible finite verification

Run `python3 verify.py` with Python 3 and no third-party libraries. The program computes charge probabilities by enumerating orders of distinct factors, independently of the proof's weighted periodicity calculation. It examines every legal context for all \(1\le k\le13\) at five exact rational transition parameters, comprising 6,752 source contexts before multiplying by parameter choices. It then generates all exceptional contexts from forced periodic overlaps and compares their rational-weight corrections to the formula for every \(2\le k\le80\), at the same five rational parameters. Finally, it checks the golden-mean three-residue simplification to 70 decimal digits through \(k=80\).

The all-length result is established by the structural proof and exact symbolic Markov weights, not by testing finitely many block lengths. No external mathematical evaluation has been performed.
