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

# Verification record

The theorem is symbolic for all prime-power fields and all \(r\ge1\), \(n\ge2\). Its decisive steps are the Smith-normal-form nullity criterion, the nonzero determinant derivative, the cyclic-lift argument, and the polynomial-centralizer orbit-size computation. The exact finite-field count of nilpotent residue matrices is the classical Fine–Herstein theorem.

`python verify_power.py` exhaustively enumerates all \(r\times r\) matrices over the indicated truncated rings and computes **successive powers**, without using the characterization being tested. The five cases are \((q,r,n)=(2,2,1),(2,2,2),(2,2,3),(3,2,2),(2,3,2)\); counts of nilpotent and maximal-index elements agree with the proof. The case \(n=1\) explicitly checks the boundary outside the theorem.

`python verify_orbits.py` directly enumerates invertible \(2\times2\) ring matrices and exhausts their conjugation actions on companion representatives. For \((q,n)=(2,2),(2,3),(3,2)\), it confirms respectively \((2,8,6)\) classes, of respective sizes \((12,48,72)\). It independently checks disjointness and full coverage of regular nilpotent matrices using determinant/trace fibers.

Both scripts produce `VERIFY_OK`. The scripts require only Python's standard library, and their checks are over prime fields; the mathematical proof independently covers all prime powers. A finite exhaustion of these examples is **not** claimed to be a proof for unrestricted \(q,r,n\). Independent mathematical audit: not performed.
