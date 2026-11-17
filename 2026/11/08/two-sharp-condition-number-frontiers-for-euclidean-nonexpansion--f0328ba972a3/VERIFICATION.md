---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The explicit 3x3 sweep B from three coordinate minimizations has vanishing first column. Gram nonzero 2x2 block obeys tr G=rho² S(rho), det G=rho^4(1+2rho²), det(I-G)=(rho-1)P(rho), S=2rho^4-6rho^3+7rho²-2rho+3, P=6rho^4+2rho²-rho-1. Independently checked exact coefficient polynomials against original verifier and SymPy. Psecond=72rho²+4>0, with endpoint signs yields exactly two real roots in SPD range. On P<=0, |rho|<2/3 gives detG<=272/729<1, ruling out both singular eigenvalues above one; on P>0 det(I-G)<0 gives one >1. At kappa=6, rho=5/8 gives ||B||~1.01807839 and rho=-5/13 gives ~0.85371231. Equalities at roots, all six update orders permutation-conjugate. The spectral eigenvalue modulus rho^(3/2) for positive rho is older and not the norm result.

## originality

PASS

The published October 2026 three-block momentum result already gives identical B and its eigenvalues, and is explicitly excluded from originality credit. A different published two-dimensional best-order Euclidean Gauss–Seidel minimax is not a 3-dimensional equicorrelation Gram classification. The sharp quartic singular-norm frontiers and sign-dependent kappa pair are not shown to be implied by either, nor by standard SPD energy descent. Historical specialized numerical iteration literature is a residual risk.

## value

PASS

Ordinary objective descent does not control Euclidean error amplification of nonnormal sweeps. Two matrices with identical condition number but opposite one-sweep Euclidean behavior are a mathematically meaningful sharp boundary example; exact all-rho classification gives useful non-asymptotic norm information beyond classical spectral convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
