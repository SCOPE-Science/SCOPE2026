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

The executable `verify.py` is standalone Python 3 with standard-library dependencies only. It constructs the 48 vertices, the 336 graph edges, and the Frobenius actions for residues 1, 3, 5, and 7 modulo eight. It checks the symbolic incidence matrix independently with line-equation ranks over three prime fields, performs exact prime-local Smith reductions of the 47-by-94 integral presentations, and checks three different deleted vertices. The output is captured in `verification_output.txt`; the last line is `FERMAT_48_LINE_FROBENIUS_FIXED_CRITICAL_GROUPS_OK`.

The prime-local moduli are \(512\), \(243\), and \(125\) for primes \(2\), \(3\), and \(5\), respectively. The computation relies on the separately known geometric critical-group exponent 5760, so the local moduli exceed the maximal exponents. Prime support is likewise bounded by that geometric group order. The mathematical justification for the coinvariant presentation and perfect graph pairing is given in `RESULT.md`. The experimental checks over finite fields are not asserted to prove the uniform characteristic statement on their own.

External independent mathematical validation has not been performed. Results for characteristic three, twisted quartics and Néron component groups are not established here.
