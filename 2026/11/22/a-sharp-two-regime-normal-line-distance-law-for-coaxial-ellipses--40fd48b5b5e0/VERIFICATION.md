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

# Reproducibility and proof boundaries

The proof of the four-parameter formula appears in `RESULT.md` and is analytical. Its decisive steps are: identification of normal-line offsets with angular derivatives of support functions; reduction by quadrant symmetry to a one-variable total variation; and the affine-polynomial derivative sign and unique root. The formula includes all nondegenerate centered coaxial ellipses and concentric disks, with the transition equality in the non-switching branch.

Run `python3 checker.py` from any directory. The script uses only Python's standard library. It verifies the sample \(u_*=11/30\) and \(z_*^2=14/15\) using exact rational fractions, then performs direct angular quadrature for 252 deterministic and seeded ellipse pairs including 40 switching cases. Its absolute tolerances account for numerical integration, not uncertainty in the exact theorem. The script prints `PASS` on successful completion and fails by assertion otherwise.

Finite quadrature is a regression check, not a proof for infinitely many semiaxes. No machine-verified formal proof or external independent assessment is asserted. Any historical priority concern remains for independent audit.
