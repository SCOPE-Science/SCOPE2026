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

# Reproducibility and verification

The exact reproducibility script is `verify_dihedral_cycle.py`, requiring Python 3.10 or newer and `sympy==1.14.0` (see `requirements.txt`). Run `python verify_dihedral_cycle.py` with no arguments in a directory containing the script. It reads no external files and makes no network requests. The corresponding complete output is in `verification_output.txt`.

The script enumerates all nonempty independent sets of each cycle \(C_n\) for \(3\le n\le13\), forms every strictly nested nonempty-face chain, and computes its full dihedral orbit. Distinct ranks prevent inversions and fix the quotient-cell orientations. It then performs deterministic elementary collapses using the unique-coface test in descending dimension, constructs the remaining exact integer chain complexes, checks consecutive boundary products are zero, and computes each integer Smith normal form. It also independently computes the Euler characteristic through signed fixed-face enumeration and Burnside averaging, checking agreement with the quotient-cell alternated count.

Every positive Smith invariant factor is one. For the two cases that do not collapse entirely, the residual cell counts are \((9,35,52,26)\) at \(n=11\) and \((14,64,100,50)\) at \(n=13\). The respective nonzero boundary ranks are \((8,27,25)\) and \((13,51,49)\), proving the claimed integral homology. Fundamental-group triviality follows from a separate theoretical fixed-point argument and Armstrong's theorem, not from the numerical output alone.

The verification is exhaustive over the specified finite range, but it does not certify any larger size, a PL homeomorphism, an independent review or uniqueness in the mathematical literature.
