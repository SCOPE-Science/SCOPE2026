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

# Verification and reproducibility

Run `python3 verify_exhaustive.py` and `python3 verify_phase_enumeration.py` with the Python 3 standard library. The captured outputs are `verify_exhaustive.out` and `verify_phase_enumeration.out`. All of these files are embedded in the same research package.

The first checker applies the actual synchronous chip transfer and checks the full distribution of period-three states against the claimed polynomial in the finite confined boxes for \(3\le n\le6\), covering exactly \(1,034,128\) candidate initial configurations. The second checker constructs independent inequality intersections for all \(3^n\) labelled phase assignments at each order \(3\le n\le9\), comparing entire polynomials and verifying integer support and endpoint counts.

The proof for all \(n\ge3\) is given in `RESULT.md` and depends on the exact update law, period-three firing-count balance, phase-specific necessary-and-sufficient intervals, and chip complementation. Computational enumeration does not establish the general theorem. Neither checker evaluates transient basin populations or periods other than three.
