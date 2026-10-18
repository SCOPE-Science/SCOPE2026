---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The matrix-rank-zero/one/two Fourier sums 1,u=-1/(q^m-1),v=1/((q^m-1)(q^(m-1)-1)) determine every coordinate Gram entry. The q-1 character labels split into local contrast eigenvalue beta, while the m-by-m rook-cell space splits into row/column differences alpha, doubly centered interactions gamma, and a two-dimensional coupled block H with eigenvalues ell±. Multiplicities sum to 1+m²(q-1). The determinant comparison gives a strict maximum mode crossover at m=2q and ell- always least. Exact independent rational/symbolic eigenvalue tests for (q,m)=(2,2),(2,3),(2,4),(3,2),(3,6),(3,7),(5,2),(5,10) match; the finite tests are corroborative, while the explicit algebra supplies the general statement.

## originality

FAIL

FAIL: a demonstrably earlier published package, "Exact coordinate Fourier frames on invertible finite-field matrices" (Git import 2026-10-11 12:57:55 UTC), proves the same *full* single-entry GL_m Fourier Gram spectrum and sharp m=2q Riesz crossover for m>=3, including all equality eigenspaces and asymptotic conditioning. This assigned result was imported 2026-10-11 12:58:01 UTC. Under a=-u, b=v, earlier C=beta, R=alpha, D=gamma, B=h, L±=ell±. The only new parameter m=2 follows mechanically by applying the same rank-one/two and rook decomposition; it is not a distinct independent spectral theorem. This is a substantive source-implication comparison, not a title match.

## value

FAIL

FAIL: the mathematically valuable all-dimensional sharp spectrum, character eigenspaces, transition and asymptotic were already established six seconds earlier. Adding the trivial base dimension m=2, an equivalent formula rearrangement and slightly different O_q error notation does not independently motivate or establish a separate new valuable spectral classification. The correctness of rederivation and finite reproducibility do not alter this coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
