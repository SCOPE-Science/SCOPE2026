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

# Verification of the square-polycycle finding

The primary evidence is the exact corner Jacobian computation, positivity of the four stable and four unstable rates under the strict edge chamber, and multiplication of the four hyperbolic saddle passage exponents. The local logarithmic passage argument is proved in `RESULT.md`, independently of finite sampling. The final periodic-orbit existence argument uses compactness, the open attracting collars of the origin and square polycycle, absence of other interior equilibria and the planar Poincaré--Bendixson theorem.

Running `python3 VERIFY.py` from the package directory uses only Python's standard library and checks the strict rational parameter witness \((\varepsilon,h)=(1/100,1/4)\), all corner eigenvalue signs and the exact return product \(32019867/26185967\). It also verifies the algebraic second equilibrium lies outside the square and tests a contrasting rational point with a repelling square. The finite edge mesh is supplemental: all-point edge orientation follows from the rigorous strict coefficient inequalities. Successful local execution returned `SQUARE_HETEROCLINIC_VERIFY_OK`.

No computationally assisted infinite enumeration, unknown external certificate, or independently validated theorem is asserted. The equality \(\rho=1\), existence of additional cycles, and identification of a unique physical periodic orbit remain unresolved by this result.
