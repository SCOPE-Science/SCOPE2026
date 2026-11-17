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

# Verification and limitations
The claimed identities follow from the exhaustive connected-tight-edge classification, the explicit centered-normal squared-norm calculation, exact integer resonance solutions, and contact-normal spanning arguments in `RESULT.md`. All assertions quantify over even \(m\ge2\) and real \(1<t<2\); the attached exact checker samples finitely many rational cases as a consistency test, not a proof by enumeration of an infinite parameter family.

Run `python verify_biclique_resonance.py` after installing Python 3, NumPy and SciPy. Its first suite uses exact fractions for every strong-part sign pattern, verifies the maximum squared norm and contact counts, and applies rational Gaussian elimination to all contacting normals. A separate SciPy halfspace-intersection calculation starts directly from the metric inequalities for selected smaller cases. Expected final line: `BALANCED_BICLIQUE_RESONANT_INCENTERS_ALL_CHECKS_PASS`.

The quadratic center-width limit is justified analytically in the proof; it is not directly certified by the finite checker. No independent validation or external expert assessment has been performed. Possible earlier equivalent expressions through Lipschitz variance and transportation geometry remain a scientific literature risk.
