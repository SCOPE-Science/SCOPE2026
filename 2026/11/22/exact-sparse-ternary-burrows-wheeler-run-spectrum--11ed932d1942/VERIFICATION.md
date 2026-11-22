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

# Reproduction and boundaries

1. Run `python3 proof_mask_gf.py` with `sympy` installed. It generates all 26 strictly increasing active-gap chains, all 111 one-/multiple-level cases, and uses exact rational arithmetic to confirm every displayed generating-function numerator. Its total generating function must be \(z^3/(1-z)^3\).
2. Run `python3 check_direct.py` with Python 3 (standard library only). It enumerates all \(\binom{n-1}{2}\) canonical ternary necklaces for every \(3\le n\le54\), constructs all cyclic rotations, sorts them and checks the run-count distribution against the independent explicit closed formulas. All assertions must pass.
3. The all-length theorem uses the rotation-order lemma and exact finite rational case decomposition, not inference from the finite checks. Symbolic computation is necessary for the displayed 111-case simplification and is fully reproducible from included source.
4. The result only counts ordinary linear runs, not circular runs, and only applies to words with exactly one \(1\) and two \(2\)s over \(0<1<2\). Literature comparison supports qualified originality, not conclusive absence from all prior sources.
