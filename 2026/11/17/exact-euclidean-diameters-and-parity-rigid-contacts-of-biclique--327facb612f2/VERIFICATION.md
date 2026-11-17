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

# Verification and limits

The executable `check_biclique_cycle_diameter.py` requires only Python 3 standard-library modules. Run `python3 check_biclique_cycle_diameter.py` from the same directory as the scientific files. The checker enumerates all sign matrices for thirteen small biclique sizes, compares their exact rational projection energies against the proposed sharp values, and checks that the equality criterion identifies exactly the maximizing sign matrices. Separately, for each of 2,401 pairs with both dimensions from 2 through 50, it constructs an explicit sign matrix attaining the proposed rational value. The expected success line starts `BICLIQUE_CYCLE_DIAMETER_PASS`.

These are finite tests. The proof for every possible size uses two exact orthogonal-variance identities, sign parity and explicit cyclic/paired witnesses, followed by strict convexity. The checker does not establish an infinite quantifier, does not certify bibliographic priority, and is not an independent mathematical audit.
