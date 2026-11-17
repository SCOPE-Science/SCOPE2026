---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For n>=6, the Johnson three-subset adjacency identity A_1^2=3(n-3)I+(n-2)A_1+4A_2 and the inclusion-filtration spectrum produce all three nontrivial eigenvalues of invariant stochastic kernels. Full permutation averaging cannot worsen SLEM. On the resulting compact two-simplex, the displayed strictly positive dual multipliers certify the minimax branches for n=6..9 and 10..12; the single-mode bound certifies n>=13. Feasible rational weight formulas attain each bound. Averaging nonnegative entries makes suppression of all one-swaps for n>=10 and of diagonal holds for n>=13 valid for every unrestricted optimizer, without claiming unrestricted uniqueness. Independent exact rational checks at all branch transitions and 400 adjacency-square entries at n=6 matched formulas.

## originality

PASS

Best-of-knowledge original exact three-branch optimizer and unrestricted support rigidity. Boyd et al. solve the one-swap Johnson graph, where distance-two jumps are forbidden. DeVille formulates generalized-distance fastest-mixing LPs and discusses Johnson numerics and eventual farthest-move dominance, but does not state the n=10/13 thresholds or all-n J(n,3) rational solution; these substantial antecedents are explicitly credited.

## value

PASS

The optimal mixing value and transition probabilities are a natural finite-state Markov optimization on a standard merged Johnson association scheme. Three exact regimes and unavoidable disappearance of otherwise allowed move types describe meaningful structural phase transitions, not an arbitrary small parameter slice or mere reproduction of a general LP.

The dated certificate retains the supplied scientific assessment, sources and limitations.
