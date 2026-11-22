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

# Verification and scope

The proof has four nontrivial ingredients: the four clopen substitution phases; an explicit invariant of normalized even-prefix triples; a parity-residue recurrence proving infinite periodicity of the two return maps; and the minimal-component conclusion from actual recurrent reference-fibre orbits plus the established almost-periodicity theorem for permutative lifts.

## Reproduce the finite checks

Use Python 3 and the standard library only:

```sh
python3 check_lag_six.py
```

The checker independently concatenates both substitution words and compares their residue parity counts at all levels through ten. It checks the state recurrence from level two through 25, calculates both 64-state return permutations, confirms that their four orbits have sizes 8, 8, 24 and 24, and compares their orbits with the closed-form even-triple invariant. It also searches substitution words at levels five through eight within a level-sixteen word, checking that all encountered return permutations preserve and traverse exactly these four classes. The corresponding direct occurrence totals are 2730, 1365, 682, 341.

The finite computations are sanity checks, not proofs that the orbit structure persists at every substitution level or for every bilateral base point. Infinite persistence follows from the exact four-periodic parity recurrence, and global minimality requires the cited almost-periodicity theorem. The proof does not establish classifications for larger offsets, alphabet moduli, or other substitutions.
