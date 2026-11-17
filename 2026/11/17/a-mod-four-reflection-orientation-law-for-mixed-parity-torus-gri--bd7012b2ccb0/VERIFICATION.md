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

The standalone `check_dihedral.py` uses Python 3 standard library only. It checks all forbidden graph edges directly from the product metric, identifies all antipodal column components, and computes exact signed simplicial Lefschetz traces for the four dihedral generators using exhaustive, memoized invariant face-orbit enumeration. The seven reported cases test the first two nontrivial residue classes of the odd side and both mod-four outcomes of the half-even width. The enumeration is exact for the tested finite instances. It does not certify every parameter by enumeration: the all-parameter recurrence and orientation argument are in `RESULT.md`. No external or independent mathematical audit has been performed.
