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

# Verification information

The standalone `verify_genus4_spin.py` implements two independent determinations of the action of every permutation partition of ten on the geometric odd and even theta-class sets: direct cycle traversal and a closed fixed-point formula for all powers through the permutation order. The checked class numbers are 42 branch types, 40 joint spectra, 40 odd spectra and 37 even spectra, with two explicit joint collision pairs. Signatures of rational points through extensions 1–5 have exactly 22, 33, 39, 39 and 40 distinct values. Direct exact finite-field polynomial gcd checks establish irreducibility of the seven listed degree 2/4/5/8/10 examples over the field with three elements.

Run `python3 verify_genus4_spin.py` with the program in a writable directory. It regenerates the complete tab-delimited `spin_spectra_42.tsv`, emits the success marker `GENUS4_HYPERELLIPTIC_SPIN_42_TYPES_40_JOINT_SPECTRA_VERIFIED`, and has no third-party dependencies. Compare the regenerated TSV against the package's bundled table. The algebraic theta-subset correspondence is a separately stated mathematical premise; code cannot certify it on infinitely many curves. Equivalence to a presently unidentified older cycle-index theorem is a residual originality risk.

No external independent validation has been performed.
