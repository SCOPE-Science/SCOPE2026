---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

On the normalized monomial basis the shift has weight sqrt((k+1)/(k+2)) and commutator diagonal 1/((k+1)(k+2)); integrating the derivative of u^(k+1)(1-u) against the flat symbol gives precisely the stated positive moment difference. Finite-support diagonal congruence followed by a diagonal phase change gives I-|c|J_a; density and parity give the full non-strict threshold. The t~sqrt(a/k) saddle and Bessel upper bound give -log w_k~2sqrt(ak); concentration at t=0 gives consecutive bond ratio one. For the lower counting bound, compression cannot increase any singular value. Cutting O(R/L_R) bonds in that compression costs O(R/L_R) in the count; scaled blocks differ in norm by o(1) from the length-L_R unit-bond path, whose cosine grid puts o(L_R) eigenvalues in an o(1) neighborhood of zero. At the lower cut the ratio of threshold to bond tends uniformly to zero. Beyond the upper cut the entire tail norm is o(lambda), giving coefficient 1/(4a) by the rank bound. Parity splits this exactly in half by sign, and inversion and summability follow. For x=a(k+1), the rescaled bond is bounded above by sqrt(6) times 2x^2 K0(2sqrt(x)) for all k, controlling both tails; on compact x-intervals the t=av substitution gives the claimed Bessel profile by an integrable majorant. The row norm bound and a diverging test block of width o(1/a) then match. The Bessel stationary ratio has positive derivative y[(K1/K0)^2-1], with limits zero and infinity. Strong convergence follows by dominated convergence and uniform contraction bounds; the two limiting regimes are not interchanged. Independently evaluating K_nu(y) by quadrature of exp(-y cosh(t)) cosh(nu*t) on [0,1,3,6] in 45-digit arithmetic and solving yK1-4K0=0 from (3,4) gave y=3.528270552033763, C=0.7353491542186070, 1/C=1.359898211976071. The omitted tail is negligible at these digits. The supplied checker was inspected, not executed; its compression tests are not needed for the asymptotic proof.

## originality

PASS

Best-of-knowledge pass for the specialized normalized flat-symbol counting law and sharp Bessel coupling collapse, not for the general Jacobi reduction or qualitative compactness.

## value

PASS

This is the operator governing exact positivity for a natural shift-plus-radial Bergman family. The count resolves the spectral scale beyond every Schatten membership statement; the norm asymptotic quantifies failure of a seemingly small strongly convergent perturbation to preserve hyponormality, with the obstruction forced to degrees of order 1/a. These are distinct, useful asymptotics rather than a restatement of the abstract norm criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
