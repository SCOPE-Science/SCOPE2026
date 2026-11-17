---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For each fixed integer j>=0 the geometric-sum factorization gives |K_nj|-|D_n| as the quotient of two fast-phase absolute values by |1-e^{it}|. Away from t=0, trigonometric approximation plus the Riemann-Lebesgue lemma yields the circular phase mean h(|1-z+z^{j+1}|)-h(1); near the singularity the reverse-triangle bound | |K|-|D| | <=1 uniformly in n and |H_j(z)-1|<=j|z-1| control the limit. The exact j=0 identity H0=1 gives C0=0. For j=1, h is 1-Lipschitz and nondecreasing; Jensen h(s)>=s yields a positive lower part P>0.83778 against negative N1<0.53590 and N2<0.23550; independent recomputation gives (P-N1-N2)/pi =0.02113360943>0. This proves C1>0 independent of numerical quadrature. No claim for j growing with n.

## originality

PASS

The moving one-frequency deletion k=n-j produces an edge transition C0=0<C1, unlike the fully classical Dirichlet constants and the published strictly positive fixed-index deletion limit. The distinct quantification in n is decisive, not a title/number mismatch.

## value

PASS

The single missing Fourier coefficient is the minimal nontrivial perturbation of a sharp Fourier projection norm. The exactly characterized moving-edge penalty and discontinuity between removing the highest and next-to-highest modes explain a meaningful sharp boundary phenomenon invisible to the full-band logarithmic asymptotic. This is not a renamed fixed-frequency constant or an arbitrary small numeric calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
