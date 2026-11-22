---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

The normalized original-column squared Frobenius projection losses are exactly 1 and t². Each Gaussian sketch row gives a two-dimensional centered normal quadratic form with eigenvalues of opposite signs, trace 1-t² and determinant -t²(1-rho²); diagonalization gives independent chi-square_k variables and beta threshold theta. Orthogonality maximizes theta (and expected loss); I_z(alpha,alpha)<=z for alpha>=1 and z<=1/2 proves strict mean <2 for every input k>=2; the k=1 asymptotic diverges and k=2 approaches 2. For k=4 the beta CDF polynomial and rational derivative give w*=(5+2sqrt(7))/3 and value (17+7sqrt(7))/27; the small-beta tail proves the t^(2-k) asymptotics for fixed |rho|<1. All hypotheses k>=1, t>1, |rho|<1 and projection-vs-SVD normalization checked. Independent symbolic reconstruction and direct quadrature and Monte Carlo checks corroborate only finite instances, not the infinity claim.

## originality

FAIL

The entire central probability law is a literal zero-mean Gaussian-product-sum sign special case of Gaunt (2024), Theorem 2.1/Corollary 2.12. Substitution U=g-tb, V=g+tb gives sign of the wrong-pivot sketched norm difference and r=(1-t²)/D, exactly theta=(1+r)/2. Expected projection loss follows by a two-point multiplication; 1-versus-2 sketch-row qualitative threshold and k=4 global constant follow by routine beta specialization and one-variable differentiation. Earlier November 2 Resultary QR first-pivot theorem gives same exact orthogonal beta law for any k, and earlier/same-day Gaussian CUR vs CPQR result gives q=2 diagonal mean-loss threshold. No independent mathematical newness remains under strong-coverage/corollary principle, despite differing engineering terminology.

## value

FAIL

A worst-case Gaussian sketch budget for first QR pivot is a mathematically natural and practically interpretable quantity; however, the submitted purported new mathematical content consists of a direct instance of a published exact Gaussian product-sign theorem, a known exact q-moment calculation for diagonal CPQR, and textbook beta-polynomial/one-variable optimizations. No new structural lemma, hard gap, nontrivial extension of the probabilistic distribution, or independent valuable mathematical invariant beyond their immediate consequences is established. Reproducibility, a convenient sharp constant, and a credible engineering interpretation alone do not make this covered special-case calculation a distinct new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
