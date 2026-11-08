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

# Reproducibility and evidential limits

The embedded files `verify_prime_exponent.py` and `verify_pebble_bisimulation.py` use only Python 3 standard-library modules. Run the two programs together in one directory, without external input files or network access. Their outputs are embedded as `check_profiles.txt` and `check_bisimulation.txt`.

The first program enumerates complete atomic relations for all three-place multiplication atoms using two variable names and the identity, on eleven representative finite groups. It tests identity, exponent, uniformity of profiles for nonidentity anchors, the six sets of relative profiles, four explicit class-separating sentence invariants, and noncommutativity of the three unitriangular examples. The second independently enumerates ordered pairs and every replacement for either pebble in all eleven groups, checking that each shared atomic type has the same set of replacement types, including for groups of differing orders and nonabelian groups. Both are exhaustive over their finite test instances.

These are not exhaustive tests over all groups or all quantifier depths. The unrestricted theorem is established by the algebraic classification of the relative profiles and the permanent two-pebble strategy in `RESULT.md`. The verification programs are reproducible corroboration, not a substitute for that proof. No independent mathematical audit was performed.
