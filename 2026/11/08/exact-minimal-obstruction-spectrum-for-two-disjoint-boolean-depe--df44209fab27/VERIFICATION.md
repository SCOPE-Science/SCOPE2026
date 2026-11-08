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

# Reproducible verification

The scripts `verify_profiles.py`, `verify_2sat.py`, and `verify_orbit_certificate.py` use Python 3 standard library only; they were executed successfully on the included source bytes. The first enumerates the sixteen 12-row maximal satisfying envelopes and every one of the 65,536 Boolean teams, finding 32,377 satisfying teams and 132 minimal falsifiers. The second independently reduces every team to a 2-SAT implication graph and reproduces the same totals and size distribution. The third expands the nine listed orbit representatives under the full 32-element natural symmetry group, verifies all 132 resulting masks are minimal falsifiers, and checks that every other nonsatisfying mask contains one. Thus completeness is checked explicitly, not inferred from sampling.

Execute `python3 verify_profiles.py`, `python3 verify_2sat.py`, and `python3 verify_orbit_certificate.py` in the same directory as those files. They terminate with `VERIFIED` only after all assertions pass. The exact finite checks supplement, rather than replace, the mathematical envelope/transversal proof. The checks do not establish claims for universes larger than two values, nor do they constitute independent verification or external certification.
