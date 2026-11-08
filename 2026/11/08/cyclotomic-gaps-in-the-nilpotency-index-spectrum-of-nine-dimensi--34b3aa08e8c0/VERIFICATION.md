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

# Verification of the nilpotency-index distribution

The proof applies over any finite field; no finite program is claimed to certify its infinite quantifiers. The two self-contained companion programs are supplied with this package.

`verify_symbolic.py` works over the polynomial ring with integral coefficients in the parameters. It constructs multiplication in the nine-dimensional PBW basis, multiplies a completely general radical element, and confirms the formulas for the relevant square coefficients and the complete cube and fourth powers, and that the fifth power vanishes. Execute using `python verify_symbolic.py`; dependency: Python standard library. Actual execution returned `VERIFY_OK_QCI_SYMBOLIC`.

`verify.py` implements finite fields and their multiplication tables independently of the symbolic checker, constructs the monomial multiplication table, and directly multiplies the powers of each enumerated radical element. It exhausts the entire \(q^8\)-element radical for all nonzero parameters over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\) (six cases). It also exhausts the five low-degree coefficients for parameters \((q,\lambda)=(5,2),(5,4),(7,2),(7,3),(7,1)\), accounting for the last three coefficients using the degree filtration proved in `RESULT.md`. The output histograms match the theorem in every case. Execute using `python verify.py`; dependency: Python standard library. Actual execution returned `VERIFY_OK_QCI_NILPOTENCE`.

The direct checker treats \(\mathbb F_4\) as \(\mathbb F_2[T]/(T^2+T+1)\). Checks include the characteristic-three cube-zero and no-index-four cases, the characteristic-two root-of-unity cases, a fourth-power resonance over \(\mathbb F_5\), and a fifth-index regime over \(\mathbb F_7\).

These are algebraic and computational checks of the stated new result, not independent external validation. No independently audited status is asserted.
