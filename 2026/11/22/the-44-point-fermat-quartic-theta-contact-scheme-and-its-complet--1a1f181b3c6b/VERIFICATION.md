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

The independently executable `fermat_contact_verifier.py` uses integer arithmetic to construct \(\mathbb F_{p^2}\) for 23 primes \(p\ge5\). It enumerates the 12 hyperflex and 32 ordinary contact coordinates from the displayed root parameters; verifies all coordinates satisfy the Fermat equation; verifies tangent lines and nonduplication; applies Frobenius to recover the predicted fixed points and two-cycles; then performs a separate full projective-point enumeration over \(\mathbb F_p\) for the degree-12 and degree-32 complete intersections. The output ends with `FERMAT_CONTACT_SPLITTING_VERIFIED_OK`.

All 8 residue classes modulo 24 are tested. The proof's infinite-prime-power range rests on exact polynomial identities, multiplicity arguments and root-of-unity Frobenius, **not** on the finite enumeration. The code does not check historical novelty, and no independent mathematical audit is asserted.
