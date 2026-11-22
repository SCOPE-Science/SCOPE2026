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

# Verification of the sharp two-collision Fourier moment theorem

The inequality holds for every compact abelian group and finite character spectrum satisfying the two distinct, off-diagonal product collision and one-character-overlap hypotheses. It is proved analytically by Parseval, AM-GM, a one-dimensional split maximum comparison, and an exact positive sum-of-squares identity. The proof's strict balanced-branch inequality is an infinite-domain analytic fact, not a numerical observation.

Run `python3 verify_cubic_two_collisions.py` (requires Python 3 and SymPy). The self-contained script enumerates all unordered pair sums of positive integer cubes for every prefix length 1–23, checks the next collision at 24, directly verifies 700 seeded exact Gaussian-integer fourth-moment identities, tests two rational equality witnesses, and expands the exact sum-of-squares identity. Verified output:

```text
VERIFY_OK finite_prefixes=23 unordered_pairs=2300 exact_moment_checks=700 equality_witnesses=2 sos_identity=1
```

The finite arithmetic enumeration establishes the claimed collision pattern only through 23, not a general classification of taxicab numbers. Moment tests are additional consistency checks and are not a proof of the sharp bound on arbitrary compact groups. The hypothesis cannot be dropped at the next resonance, and no claim is made about higher moments or arbitrary cubic spectra. Independent mathematical audit has not been performed.
