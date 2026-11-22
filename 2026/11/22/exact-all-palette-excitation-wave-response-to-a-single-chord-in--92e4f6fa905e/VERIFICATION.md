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

# Reproduction and scope

Execute `python3 verify_bruteforce.py` and `python3 verify_transfer.py` from the directory containing these scripts. Both use only the Python standard library. They check the exact formula in RESULT.md for every qualifying chord position in their stated finite ranges.

`verify_bruteforce.py` directly constructs the graph and evolves each \(k\)-state configuration for \(k\) steps, separately excluding fixed states. It checked 30 graph/palette cases and 1,301,418 complete initial-state trajectories. `verify_transfer.py` independently computes phase-support assignments by tracking endpoint support flags in a path transfer; it checked 10,266 parameter cases over palettes \(3\) through \(8\) and circumference up to \(61\). The reported outputs are included verbatim in the corresponding `.out` files.

The independent transfer is an exact finite combinatorial computation, not a universal machine proof. The all-length conclusion follows from the proof of the successor-cycle and path-word lemmas in RESULT.md, which should be reviewed separately. No external audit, certification or claim of historical priority is implied by these checks.
