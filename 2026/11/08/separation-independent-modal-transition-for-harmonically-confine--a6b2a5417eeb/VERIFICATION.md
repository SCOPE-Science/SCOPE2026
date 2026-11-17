---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The OU renewal law p(x)=r∫e^{-rt}∫P_t(x|y)mu(dy)dt is positive, even for symmetric mu, and twice smooth inside (-a,a). Its source-free equation Dp′′+kappa x p′+(kappa-r)p=0 and p′(0)=0 give (exp(kappa x²/(2D))p′)′=((r-kappa)/D)exp(...)p, fixing derivative sign throughout gap, critical flatness included. For two atoms ±a, Gaussian means lie in [-a,a], hence each Gaussian derivative strictly decreases for x>a; the cusp jump at a and symmetry yield complete global modes. At r=kappa the displayed erfc-tail plateau is normalized by integration by parts. Independently checked derivative signs for a gapped four-atom mixture and source formula normalization. Boundary r=kappa, r>0, kappa,D,a>0 and arbitrary unbounded symmetric mu are respected. Independent finite quadrature cannot establish generality.

## originality

PASS

PASS for the quantified universal source-free-gap monotonicity for every symmetric reset law supported outside (-a,a), even with continuous/unbounded tails. Exact two-atom global shape, threshold, plateau and normalized density are NOT novel: same-day previously published Resultary proof covers those precisely. Its integrating-factor identity is local and readily adapts, but its stated theorem concerns the specific two-site source and does not logically give the arbitrary-law statement without applying the source-free ODE for new measures. Best-of-knowledge priority qualified accordingly; the narrower two-site result contributes no original credit.

## value

PASS

PASS: The robust exact modal transition is independent of the ENTIRE symmetric reset distribution outside a gap, even for mixtures or unbounded support, rather than a special fit to two reset sites. This invariance is a physically motivated structural law about stationary density shape and supplies a useful criterion when reset sources are heterogeneous. The two-site phase diagram, density and threshold are prior and receive no incremental value credit. Proof is brief because the common source-free ODE is strong; briefness does not by itself negate the motivated general quantifier.

The dated certificate retains the supplied scientific assessment, sources and limitations.
