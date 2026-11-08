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

The theorem uses a single monitored channel \(L=\sqrt\gamma |1\rangle\langle1|\), a Hamiltonian \(H=g\sigma_x+(\Delta/2)\sigma_z\), strictly positive \(g,\gamma\), and real \(\Delta\). Count cumulants are ordinary cumulants, with time taken to infinity before changing model parameters.

Run `python3 checker.py` from the directory containing the result. Its Python standard-library exact-rational tests verify the fourth-order formal logarithm and power-series inverse against the four closed cumulant formulas for 100 parameter triples. Independently constructed \(4\times4\) matrices yield 800 determinant matches to the claimed tilted characteristic polynomial, and a direct rational solve yields 200 checks of the no-click waiting Laplace transform. Tests also sample positive and negative fourth-cumulant regimes. These are finite algebraic cross-checks, not substitutes for the proof of analyticity or the infinite family of sign cases.

The analytic proof supplies regeneration after clicks, strict stability of the no-click generator, existence of an analytic dominant eigenvalue, explicit cumulant derivation and uniqueness of every phase-boundary crossing. The result does not establish finite-time cumulant signs, asymptotics uniform as the coherent drive vanishes, nonideal detector performance, an experimentally observed transition, or publication priority. The 2022 resonant full-counting transform and general 2023 full-counting techniques are credited as prior work; independent scientific audit has not been performed.
