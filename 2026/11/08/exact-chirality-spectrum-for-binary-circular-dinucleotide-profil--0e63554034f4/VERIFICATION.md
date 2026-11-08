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

# Verification and scope

The proof applies for all integers \(b\ge1\), \(A,D\ge b\), with constant words excluded. Its central steps are the paired positive-composition encoding, the offset reversal action, reflection fixed-point generating functions, and dihedral Burnside's orbit formula. These steps are symbolic and cover arbitrary parameters and periodic representatives.

Run `python verify.py` in the same directory as the other files. The program independently enumerates literal binary rotation classes for lengths \(2\) through \(17\), calculates circular `00`/`01`/`10`/`11` counts, tests literal rotation equivalence to reversal, and compares all observed profiles to both the total and the symmetry formulas. The expected terminal line is `VERIFY_OK lengths=2..17 profiles=444`.

Finite checks do not certify every parameter; the non-experimental proof in `RESULT.md` supplies the universal argument. The program uses only the Python standard library. No external independent audit has been performed.
