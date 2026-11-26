---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A concept is uniquely determined by its extent and every extent is an intersection of columns, including the empty intersection G. A proper coatom can be obtained only if some chosen supra-coatom column is that coatom; conversely all coatoms meet-generate the full power set. This includes r=1 and m=0. Each of the r disjoint coatom types has per-column probability t and 0<rt≤1, so exclusion of j types has probability (1−jt)^m. Inclusion–exclusion and ordered choices of k missed types give the probability and factorial moments (r)_k(1−kt)^m. In the critical window mt²≤(log r+O(1))/r, so for each fixed k the factorial moment tends to e^(−kc); the Poisson law is moment-determinate, and convergence of the zero mass follows by considering the distribution function at 1/2. Above threshold, the mean number missed is at most exp(log r−mt)→0. Below, the same logarithm expansion for k=1 gives a diverging mean, and (1−2t)^m≤(1−t)^(2m) makes distinct missed indicators negatively correlated or uncorrelated, so variance is at most the mean. This establishes all claimed probabilities for varying p without endpoint bounds. Independent weighted enumeration of exact extent intersections at p=1/3 and p=3/4 agreed with saturation and all factorial moments in four dimensions, including empty and single-object cases (e.g. r=3,m=4,p=1/3 gives 512/59049). Frozen reference 3 misattributes the 2020 paper to Dürrschnabel et al.; its authors are Felde, Hanika, and Stumme. This bibliographic error does not affect correctness of the formulas.

## originality

FAIL

Boolean saturation is the known full-size contranominal-scale criterion, and the rest is the uniform coupon collector with an independent null draw. The exact formula is direct occupancy inclusion–exclusion, and the whole varying-p critical window is a routine binomial thinning of the classical Poisson empty-urn limit. This is demonstrable implication, not a claim that the complete formula has already appeared with identical notation in formal-concept literature.

## value

FAIL

Boolean saturation is a motivated event for concept enumeration, but the exact threshold here is a routine application of two known facts. The coatom representation, null atom, and time change leave no new occupancy phenomenon, structural difficulty, or novel exact invariant after thinning. It is useful as an explanatory application, not as a separate research finding under the stated standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
