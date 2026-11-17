---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Exact cumulant K=λ(e^{bt}-1-bt)+s t²/2 gives sharp variational c/b=sup_x theta h(x)/[x(1+theta h(x))]. The factorial convolution for h(x)=2(e^x-1-x-x²/2)/x² gives a strictly decreasing coefficient-ratio sequence for (xh’−h)/h²; weighted coefficient covariance proves strict monotonicity from 3/4 to zero, hence threshold and uniqueness. Small-x inversion yields x=(40/3)ε+O(ε²), c/b=theta/3+(5/9)ε²+O(ε³); large-x stationary asymptotics yield x=L+3log L−log2 and b/c=L+3log L+1−log2+o(1). Independent exact sequence and parameter checks passed 220 bounded tests; analytic monotonicity handles all x.

## originality

FAIL

The published October 18 theorem A sharp Gaussian-noise transition for optimal sub-gamma scales gives the identical fixed-jump Poisson+Gaussian variance-exact model, local/interior 1/3 Gaussian-to-Poisson ratio threshold, unique optimizer and exact high-noise inverse-log expansion. The published October 26 unequal-jump phase-surface theorem further explicitly includes its b_negative=0 Gaussian endpoint p=theta, giving both exact 40/3 critical optimizer and 5/9 quadratic excess. Thus the COMPLETE final theorem, including expansions, is already implied by the two prior results.

## value

FAIL

The exact Gaussian-dilution transition and asymptotics are mathematically motivated quantities, but they were already computed in prior analytic results. The submitted fixed-jump rederivation supplies no new structural lemma, sharp unknown invariant, or non-implied classification relative to those sources; correctness and reproducibility do not make it new mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
