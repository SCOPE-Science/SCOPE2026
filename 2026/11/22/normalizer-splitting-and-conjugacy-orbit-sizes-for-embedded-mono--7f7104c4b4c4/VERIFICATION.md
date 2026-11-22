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

# Reproducibility and limits

Run `python3 verify.py` from this directory. It independently enumerates partial injections on zero through five labels, computes their inverse submonoids by genuine closure under composition and inversion, and forms actual simultaneous conjugates under the full symmetric group. Each generating fiber and each orbit length is compared against the stated centralizer-times-inversion-or-totient formula. Successful execution ends in `MONOGENIC_INVERSE_NORMALIZER_PROFILE_VERIFIED`.

The verified triples `(partial_injections, distinct_inverse_submonoids, conjugacy_orbits)` are `(1,1,1)`, `(2,2,2)`, `(7,6,5)`, `(34,24,10)`, `(209,126,20)`, `(1546,838,36)`, in increasing size from zero through five. The finite checks do not verify the infinite theorem independently; that conclusion follows from the elementary proof using component centralizers, generator rigidity and explicit normalizing sections.

No external independent audit has been performed. The possibility of older equivalent treatments of the split normalizer is a publication-priority limitation, not a computational-certification claim.
