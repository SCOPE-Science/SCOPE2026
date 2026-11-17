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

# Reproducibility and checks

Run `python check_multipartite_ball.py` using Python 3 with NumPy and SciPy installed for the unrestricted numerical comparisons. The exact rational checks use only the Python standard library.

The tested program reconstructs all \(N\) original graph Laplacian columns from part sizes, checks zero sums and the center formula, the threshold equation, every squared-distance clearance, positive contact weights, and the weighted mean and variance identities. It checks 646 exact profiles (three through six nonempty parts, plus selected larger examples), including zero-weight boundary contacts. It independently optimizes unrestricted ambient-dimensional center coordinates for 23 cases, without prescribing symmetry. The observed successful final marker is `MULTIPARTITE_LAPLACIAN_BALL_PASS`.

The program's finite coverage does **not** prove the theorem for arbitrary part sizes or graph orders; those quantifiers follow from the explicit algebra in the proof. Independent audit: not performed.
