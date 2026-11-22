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

# Reproducibility checks

Run `python verify.py` from the directory containing this file and `verify.py`. Python 3 and SymPy are required for the first symbolic rational identity check. All later tests use the Python standard library and exact `Fraction` arithmetic. A successful run ends with `VERIFY_OK`.

The program independently simplifies the three-parameter rational Lyness conservation law to zero; checks \(H\circ F=H\) at 6,241 rational pairs; checks the vertex inequalities, polygon perimeter and area, and primitive orbit periods at 321 different reduced rational energy levels; enumerates the complete lattice boundaries at energy \(m\) for all integers \(1\le m\le100\) and checks every lattice point belongs to the unique orbit on its shell (25,550 tested points); and checks the zero-energy reflection and the two 18-period resonance levels. The checker was actually executed successfully from its final code path. These computations verify finite instances and underlying algebra; the all-real/all-integer theorem is the analytic proof in `RESULT.md`, not an inference from these tests. No independent audit or external certification is claimed.
