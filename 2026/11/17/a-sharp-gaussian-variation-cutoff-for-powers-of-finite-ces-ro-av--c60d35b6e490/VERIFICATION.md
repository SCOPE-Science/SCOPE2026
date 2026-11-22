---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Every real x decomposes exactly into the constant vector plus signed prefix step vectors u^(t) weighted by adjacent differences, with V(x) their coefficient l1 norm. C_n fixes constants, is positive and preserves nonincreasing sequences; for any power the step output has first coordinate one and variation 1-sum_{j<=t}(C_n^m)_{n j}. Positivity makes t=1 uniquely largest for m>=1 and equality forces the other step coefficients zero; m=0 excluded from rigidity. The Markov interpretation of C_n as uniform downward transitions has absorbing state one and hitting PGF f_n(z)=z prod_{j=2}^n (j-1)/(j-z), via first-step recursion (j-z) f_j=(j-1) f_{j-1}. Thus 1-(C_n^m)_{n1}=Pr(T_n>m) for all n,m. Each G_j has mean 1/(j-1), variance j/(j-1)^2, absolute centered third moment O(1/j); Berry–Esseen for independent triangular array yields error O((log n)^-1/2) because total third moment O(log n) and s_n^2=log n+O(1). Independently exact-rational recomputation for n=2..8 and m=0..6 reproduced each matrix-power last-row entry, the geometric convolution and every step sharp norm. Finite checks corroborate; the all-n statement follows from exact algebra and Berry–Esseen.

## originality

PASS

Adell and Lekuona supply earlier power kernels and mixture formulas, potentially enough to recover the Markov marginal, and Akhmedov–Başar treat infinite bv_p. The audited new contribution is the combined finite path-variation operator norm, unique extremizers and joint dimension/power Gaussian window. The separate Resultary Gini-variation theorem for the same C_n has a complete-graph seminorm and one application, so does not dominate this path-power cutoff.

## value

PASS

The exact finite path-variation power norm and its random hitting-time representation identify a nontrivial dimension-dependent mixing scale and sharp extremizers for a canonical averaging operator. A Gaussian cutoff after log n steps with sqrt(log n) window is a meaningful natural asymptotic; it is not a routine restatement of fixed-dimensional spectral convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
