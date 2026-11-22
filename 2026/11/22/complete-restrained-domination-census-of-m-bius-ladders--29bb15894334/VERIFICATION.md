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

# Verification

The graph uses the explicit vertex set \(\mathbb Z/(2n)\mathbb Z\), with edges along the cycle and antipodal chords. Two self-contained checks have different mathematical paths:

- `python verify_direct.py` enumerates every vertex subset from the original adjacency definition for all integers \(3\le n\le10\) and independently tests both clauses of restrained domination.
- `python verify_transfer.py` builds a sixteen-state local-rule automaton, checks the row-swap symmetry, derives and verifies both finite characteristic determinants with SymPy, checks the formal leading-coefficient identities, and enumerates the transfer distributions for all integers \(3\le n\le40\).

The direct test covers \(\sum_{n=3}^{10}2^{2n}\) subsets, with no random sampling. These exhaust only the stated finite orders. The infinite proof consists instead of the exact transfer bijection, finite determinant identities, and algebraic coefficient extraction in RESULT.md. No unexplained numerical extrapolation is used.

Use Python 3 and SymPy (verified with SymPy 1.14.0). Both commands completed with final `PASSED` messages as recorded in `verification_output.txt`. The recorded output is corroborating evidence, not a replacement for rerunning the source code. No external independent audit has been performed.
