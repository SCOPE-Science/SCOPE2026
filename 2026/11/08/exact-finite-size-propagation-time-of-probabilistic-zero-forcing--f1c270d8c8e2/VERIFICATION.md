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

Execute `python3 verify_sun.py` from this directory with Python 3 and its standard library. The checker:

- calculates exact boundary-state expectations through index \(110\) using integer-rational arithmetic;
- independently derives both starting-state expectations from the recurrence and checks the closed form through sunlet order \(109\);
- solves the original complete \(2n\)-vertex blue-set Markov chain, without frontier compression, for \(n=5\) and \(n=6\), including leaf starts;
- compares the obtained exact values with the source's displayed finite-size decimals.

The actual replay returned **653 exact equality checks and six decimal-table comparisons, all passing**. The full-graph values were \(1225469/256500\) and \(251448607/46170000\) from cycle starts at sizes five and six, respectively. The complete algebraic argument, especially the rational generating-function identities, is in `RESULT.md`; no finite test substitutes for the all-size proof. No external or independent audit has been performed.
