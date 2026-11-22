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

# Verification and reproducibility

The proof is in `RESULT.md`. Run `python3 checks.py` in the extracted directory. The checker uses only the Python standard library, constructs the substitution \(0\mapsto0001\), \(1\mapsto0111\), and checks exact counts and finite word-complexity inequalities. The verified finite levels do not certify the theorem over infinite subshifts: the argument uses higher-block recoding, synchronized physical roof sums, uniform continuity of the compact suspension, the bounded-doubling comparison, and the substitution's closed-form eigenvalue count.

At the substitution level, \(|\vartheta^k(0)|=4^k\), and the zero-minus-one count equals \(2^k\). The irrational roof has Birkhoff sums deviating from the only possible constant rate by \((\sqrt2-1)2^{k-1}\) in magnitude; this diverges and forbids continuous cohomology to a constant. Factor-complexity upper and lower bounds are proved, while the checker only tests finitely many lengths.

The source paper's constant-roof theorem does not by itself supply a variable-roof assertion. No independent mathematical audit has been performed. Historical priority comparisons remain incomplete; see `AUDIT.json` for the scope and residual risks.
