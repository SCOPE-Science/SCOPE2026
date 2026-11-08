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
# Reproduction and scope

Run the included `verify.py` with standard Python 3 (no third-party packages):

```sh
python verify.py
```

The standalone checker (executed from the actual bundled source) reported:

```
PASS: exact outcome enumerations, marginal-law identities, all-liked formula, symmetry, small-horizon identities
Checks: 106
Examples:
p1=1/2, p2=1/2, m=5, success=4047/4096
p1=1/3, p2=2/3, m=6, success=524998/531441
p1=1, p2=1, m=5, success=5/8
```

It explicitly enumerates valuation and recipient histories, rather than merely replaying the trinomial formula, for six exact-rational parameter pairs and each horizon from one to six. It checks the all-approved coin-toss formula at horizons through 34. The analytic theorem covers all nonnegative integer horizons specified in the result and the infinite-horizon limits; the finite checks do not constitute proofs of those infinite statements. The proofs of the sharp prefactors use standard aperiodic lattice local central limit estimates after exponential tilting, and the boundary-window proof uses the bounded triangular-array central limit theorem. Independent audit has not been performed.
