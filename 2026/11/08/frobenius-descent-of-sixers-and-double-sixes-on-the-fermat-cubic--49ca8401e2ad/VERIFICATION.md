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

# Reproducibility and scope
The accompanying `verify.py` uses Python's standard library only. It enumerates exactly 351 line pairs, 296010 six-subsets, all resulting 72 sixers and 36 double-sixes. All determinant computations are performed in \(\mathbb Z[\omega]\), with \(\omega^2+\omega+1=0\); norms of all nonzero determinants are 3 or 9, eliminating any untested positive characteristic except the excluded 3. The complementary sixer pairing is verified including bijective omissions.

Running `python3 verify.py` yields `VERIFY_FERMAT_DOUBLE_SIX_OK sixers=72 double_sixes=36 fixed_sixers=2 fixed_double_sixes=4`. Running `python3 verify_fields.py` separately yields `VERIFY_DOUBLE_SIX_FIELD_OK`; its elementary row-reduction algorithm verifies the arithmetic fixed-set counts over characteristics 2 and 7. These small-field checks are not a substitute for the integral argument.

The proof of the contraction count also uses the standard facts that six disjoint exceptional curves on a smooth cubic surface can be contracted and that the Brauer group of any finite field vanishes. Proofs/certificates do not address characteristic 3, for which the Fermat cubic is singular. No external independent audit has been performed.
