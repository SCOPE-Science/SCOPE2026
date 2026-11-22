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

# Reproducible verification

With standard Python 3, execute `python3 verify.py` from this directory. The script computes the axial polynomials \(Q_m\) for integers \(0\le m\le9\), where \(m=0\) is an algebraic base case (the ordinary disk), not an empty cylinder intersection. It checks coefficient identities against the infinite generating-series formula at 16 positions per polynomial, verifies all polynomial degrees and strict alternating signs, constructs each Cayley transform with integer coefficients, and verifies imaginary-axis root exclusion by exact rational polynomial Euclidean algorithms.

An exact-fraction Routh–Hurwitz count then obtains the interior-zero vector \((0,0,0,0,0,0,0,0,2)\) for \(m=1,\ldots,9\). The final sign string is `+++++++-++`. No numerical tolerance controls these decisions. Root approximations supplied for orientation in `RESULT.md` are not proof objects.

Every count uses the classical Routh–Hurwitz root-count theorem; the finite exact certificate does **not** establish any statement for \(m\ge10\), and it does not search for nonaxial zeros. The required monomial-basis and beta-integration arguments are written in `RESULT.md`. Independent audit has not been carried out.
