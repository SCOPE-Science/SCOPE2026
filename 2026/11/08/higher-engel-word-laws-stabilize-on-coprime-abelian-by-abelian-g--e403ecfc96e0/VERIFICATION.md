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

The standalone `verify.py` runs without third-party packages under Python 3. It builds the semidirect group products directly and evaluates Engel words as literal nested group commutators, rather than invoking the formula being tested. `verification_output.txt` is the recorded exact output from executing `python verify.py` in the artifact directory.

Ten coprime cases, including noncyclic complements, noncyclic kernels, non-Frobenius actions, a nonfaithful action, non-elementary kernels, and a non-diagonal irreducible action, were exhaustively checked for \(k=2,3,4\), yielding 464790 individual word evaluations. For every triple consisting of a complement coordinate of the left element and a fixed complete right element, all kernel coordinates of the left element were enumerated to check conditional support and exact fiber multiplicities; this gives 3884 conditional-fiber checks. Every predicted right Engelizer size was checked; subgroup closure was tested on small examples or a distinguished right element for larger examples. The predicted Fourier transform was compared directly with the enumerated word distribution at each additive character, using a complex numerical tolerance of \(10^{-10}\); the remainder uses exact integer/rational arithmetic. The dihedral group \(C_8\rtimes C_2\) provides a fully enumerated failure of stabilization without coprimality.

A successful execution prints `VERIFY_OK cases=10 direct_word_evaluations=464790 conditional_fibers=3884` as its last line. The original execution output is included verbatim. The symbolic proof in RESULT.md, and not these finite computations, proves the universally quantified statements. No independent mathematical audit is asserted.
