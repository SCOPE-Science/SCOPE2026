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

# Reproduction and limits

With Python 3, NumPy and SymPy available, execute `python check_frontier.py` beside this file. In the verified run it produced `PASS: 48253 independent analytic/numeric assertions`.

The executable checks five exact SymPy identities; it checks the normalized explicit saturation families at eight concurrence values and four depolarizing noise strengths; and it calculates the conditional battery state directly from the full eight-dimensional noisy W density matrix for the witnesses and 12,000 seeded complex auxiliary rays. Its asserted inequalities, numerical energy comparisons and weighted probabilities agree with the theorem. This finite sample does **not** replace the proof for all complex four-component rays, which is the triangle/Cauchy–Schwarz argument in `RESULT.md`.

The code has no network calls, private inputs, outside papers or unbundled data. Independent auditing of mathematical priority and correctness has not been performed.
