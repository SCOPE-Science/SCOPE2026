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

# Reproducibility and evidence scope

Run `python3 verify_exhaustive.py` and `python3 verify_runs.py` in the directory containing these files. Both programs require only Python 3's standard library; deterministic outputs are stored as `exhaustive_output.txt` and `runs_output.txt`.

The first program constructs the labelled graph for each cycle length 5–16 and every nonredundant chord distance, performs synchronous open-neighbor majority with tie retention, tests the literal conditions \(M^2x=x\) and \(Mx\ne x\), and checks both chord endpoints change state. It examines 48 graphs and 830,112 configurations. The four-vertex base case was also separately checked by direct enumeration and has six period-two states. The second program independently enumerates stationary arc words with the exact boundary conditions for all lengths 1–17 and checks the stated Fibonacci and residue coefficient recurrences through length 100.

The complete proof of the general theorem is in `RESULT.md`: phase propagation; classification of stationary versus flipping arcs; generating functions for admissible stationary words; endpoint compatibility; and asymptotic estimates. The finite experiments do not certify the infinite domain. No independent audit or external validation has been performed.
