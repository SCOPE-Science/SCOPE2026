---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The integrated feature kernel is as stated and canonical because E[H_t(U)]=0; its mean diagonal is ∫u(2u−1)²du−1/30=2/15. In the cube of the centered kernel expansion, a lone diagonal at an independent vertex vanishes by centering, and an unmarked vertex appearing in only one pair term vanishes by conditional degeneracy. The surviving triple diagonal, two diagonals on a pair, diagonal with doubled pair, tripled pair, and triangle have coefficients n, 12 binom(n,2), 24 binom(n,2), 8 binom(n,2), and 48 binom(n,3). Independent exact-rational integration reproduces the five contractions 86677/13513500, 15931/11583000, 280583/121621500, 225809/162162000, and 502883/324324000 in order; the two variance contractions are 169/8100 and 109/8100. Coefficient comparison after expanding the binomial counts gives the stated all-size cumulant, not just agreement at sampled sizes. Substitution and differentiation give γ′(x) with sign opposite to P(x)=149806549x²−355004333x+20427855, where P(3)=303673797, P′(3)=543834961 and P″=299613098. Skewness is positive at every integer n≥1; exact squared comparisons give γ₂>γ₁, and γ₂²−γ₃²=14038148030846784406/158775012314273730375>0. Therefore the sequence decreases strictly from n=2, has its unique integer maximum there, and stays above its limit for every n≥2. The asymptotic limit and the reported small-sample figures are consistent with the formulas.

## originality

PASS

The primary paper's cumulant of identical constant value belongs to its limiting law, while the closest distinct catalogue finding supplies exact variance and mixed second-order dependence of the same statistic. Neither statement supplies the two finite-size corrections, the diagonal and repeated-pair cubic contractions or the exact integer maximum. Generic canonical-kernel counting is a method, not the evaluated contractions. The pass is limited to the finite-n third cumulant and skewness conclusion, not the statistic, its variance, or its limiting cumulant.

## value

PASS

A published limiting-cumulant approximation motivates measuring the exact small-sample departure for this specific statistic. The evaluated cubic contractions and size-two maximum show a nonmonotone initial change and a strictly one-sided approach thereafter, with skewness still about 6.19% above its limiting value at n=10. This is a useful finite-sample description that cannot be read from the known variance and limiting third cumulant. It does not infer exact critical values or calibration improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
