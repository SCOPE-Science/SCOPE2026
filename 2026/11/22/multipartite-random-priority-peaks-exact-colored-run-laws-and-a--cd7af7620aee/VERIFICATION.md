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

In descending priority order within a color, the initial same-part run consists of all the peaks: once a second part has appeared, any later vertex has an earlier neighbor in one of these two parts. Its tail is the sum of the without-replacement same-part probabilities, including a run occupying an entire nonempty color class and zero for an empty one. Given the full color assignment the relative priority permutations are independent, and their run laws depend only on the part-by-color table, so the product law survives conditioning on that table. A vertex with B same-color neighbors is a peak with probability 1/(B+1); integrating the binomial pgf gives the exact mean. Fixed k follows from simultaneous cell laws of large numbers and convergence of the product of color laws to the stated geometric mixture. For k→∞ and n/k≫log n, the stated relative-error Chernoff bound is superpolynomial after the union bound. On this event (m)_j/(M)_j≤(m/M)^j bounds the tails by rρ^j, so conditional variances converge uniformly to the mixture variance and conditional centered third moments are bounded. Conditional Berry–Esseen and total variance apply after checking the centering: on the convex good count box all denominators in the conditional mean are Ω(n/k) and each cell derivative is O(k/n). The global clipped Hamming-Lipschitz extension and Efron–Stein give variance O(k²/n)=o(k), with squared error at most n² on the negligible bad event. Thus exact unconditional centering is valid and the variance limit follows as well. Lemma 1 of the primary paper applies with the stated recoloring rule and palette. The frozen exact-enumeration check.py was inspected, not executed; it concerns finite distributions, not the growing-k result.

## originality

PASS

Pass for the distinct contribution identified in RESULT.md's prior-work section, chiefly the k→∞, k log n=o(n) Gaussian and variance limits using the full count-table factorization. Do not credit the prior-equivalent recoloring reduction, mean formula, or fixed-palette limit as distinct. A same-day companion contains the same run interpretation, the full unconditional joint law and a stronger fixed-palette approximation; its bound even implies a Gaussian weak limit in a more restrictive range. The wider palette-growth theorem with unconditional variance and exact centering is not covered by that comparison.

## value

PASS

The growing-color theorem identifies Gaussian fluctuations and an explicit composition-dependent variance on graphs with degree proportional to n. The count-table dependence is resolved at the true sqrt(k) scale and the result reaches palette sizes much larger than the independently available product-law TV comparison supports. This is a distinct regime of a canonical stability-time statistic, not another finite distribution computation. The theorem requires fixed r, all positive limiting part proportions and k log n=o(n); it does not identify the sharp growth boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
