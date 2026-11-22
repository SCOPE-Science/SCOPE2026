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

Three standalone standard-library checks are supplied. Run `python3 verify.py`, `python3 verify_forbidden.py`, and `python3 crosscheck.py` in this directory, without additional dependencies.

`verify.py` reconstructs the one-step and two-step image automata, exact characteristic polynomials, all stated image-word counts, and rational root isolations, including the dominant image-growth root in \( (1.732101,1.732102) \). `verify_forbidden.py` generates and trims the minimal-forbidden-word automaton (29 reachable, 16 productive states), checks every productive transition against its certificate, proves the transfer determinant and all-length rational series by the exact adjugate degree bound, confirms the primitive component, and isolates its dominant real root in \( (1.647072,1.647073) \) by Sturm variations. Thus strict root separation certifies the entropy gap without floating-point inference. `crosscheck.py` enumerates all finite input blocks through output length fourteen and independently verifies distinct outputs, minimal forbidden counts, and the previously known shortest discrepancy.

Expected final markers: `VERIFY_OK`, `FORBIDDEN_VERIFY_OK`, `CROSSCHECK_OK`. These completed successfully. Infinite claims depend on the finite-state proofs and exact algebra, not on extrapolating finite enumeration.

Scientific limitations: the new result concerns only time-two spatial images, minimally forbidden contiguous words, and their entropy gap. The maximal-entropy-measure consequence follows from Wu and Zhang (2026), arXiv:2611.03758v1, rather than from an independent new measure-classification proof. No independent mathematical audit has been performed.
