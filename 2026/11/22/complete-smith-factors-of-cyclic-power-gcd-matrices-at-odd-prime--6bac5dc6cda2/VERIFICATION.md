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

# Verification of cyclic power-GCD Smith factors

The mathematical proof in `RESULT.md` gives the universal statement. Its pivotal nonstandard steps are: the exact three-level block decomposition; integral splitting away from \(p\); a unit-pivot Schur complement at \(p\); and the cross-prime comparison identifying a globally ordered Smith diagonal. They do not rely on numerical diagonalization to determine integral invariant factors.

The standalone `check.py` uses only Python 3's standard library. It builds each original gcd-difference matrix for the seven test pairs \((p,a)=(3,1),(3,2),(3,3),(3,4),(5,1),(5,2),(7,1)\), checks every entry against the proposed block matrix, checks divisibility and the determinant, and computes local Smith valuation lists independently using modular unimodular elimination over suitable powers of every prime dividing the predicted final factor. There were 4,499 assertions, all successful. Finite testing is a check on the formulas and not a replacement for their proof.

The theorem is not claimed at \(p=2\), for prime-power modulus \(p^k\) with \(k\ge3\), or for incomplete residue index sets. No independent mathematical validation has been performed.
