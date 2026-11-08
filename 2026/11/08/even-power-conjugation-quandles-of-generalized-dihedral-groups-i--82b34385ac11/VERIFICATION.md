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

# Reproducibility and mathematical limits

Execute `python3 check.py` in a directory containing `check.py`. The script builds finite generalized dihedral groups from the given additive invariant factors, then constructs the power-conjugation operation directly from the multiplication and inversion laws. For nine cases it checks the derived multiplication law, computed image group \(H=(2m)A\), the predicted exact size of the automorphism group, and group-induced automorphisms. Six nontrivial small cases are checked by exhaustive permutation search of the two intrinsically distinguished layers; three additional trivial cases use their proved full symmetric group, without factorial enumeration. Larger cases check multiplication and induced automorphisms but not the entire automorphism group by brute force. The recorded standard output appears in `output.txt`.

The theorem is proved by a general fiber/torsor argument and does not extrapolate from computations. The calculation neither establishes the novelty of the formula nor provides an external independent audit. The result excludes odd exponents, nonabelian rotation subgroups, and infinite groups.
