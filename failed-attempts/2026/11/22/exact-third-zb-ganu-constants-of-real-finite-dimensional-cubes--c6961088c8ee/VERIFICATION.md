---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The geometric mean of the four squared signed norms is exactly the numerator. In dimension one their arithmetic mean is Q by sign cancellation; in dimension two replacing each squared sup norm by the sum of its two coordinate squares bounds that mean by 2Q. The displayed witnesses attain both bounds. In dimension three two sign maxima choose a common coordinate, and their scalar product of absolute values is |u²−v²|≤(S−m)², where m is the least radius and both sign-agreement classes are nonempty. The other factors are at most S. Writing t for the sum of the two larger radii and u=m/t gives the bound (1+u)/(u²+1/2) on [0,1/2], with unique maximum at (√6−2)/2. Equality in the larger-radii square bound and this scalar maximum forces the stated radius ratio. The witness has signed norms 2,2,2+a,2+a for a=√6−2. The four-coordinate sign witness gives 3, the general bound S²/Q, and zero padding gives all larger d. For the arithmetic comparator, the colliding pair's squared norms sum to at most 2(a²+t²), with a the singleton-group radius and t the sum of the other two (not necessarily ordered). Bounding the other two by (a+t)² yields ratio at most (a²+t²+at)/(a²+t²/2), maximized at a/t=(√3−1)/2; the witness with first vector (−a,−a,a) and the same other two, a=√3−1, attains it. The two three-dimensional witnesses were reproduced independently (`python3 /workspace/frozen_review_replay.py 1`); the frozen diagnostic was read, not run.

## originality

FAIL

The closely matching indexed penultimate-Walsh result 44d920273418 formally states n≥4. However, its inspected proof of the exact penultimate value and saturation applies unchanged at n=3: the only needed scalar range here is 0<q<2, and (n,N,m,q)=(3,4,2,1) satisfies every condition of the collision, derivative, and matching-construction steps. It gives the exact three-cube value and radii, not just a loose estimate or an analogy. The same-day relationship and chronology are unresolved; this decision rests on verified mechanical coverage of the substantial calculation, not priority inferred from the date. The two smaller dimensions follow by elementary arithmetic-mean and Hilbert-coordinate comparisons.

## value

FAIL

The first nonsaturated sharp geometric constant and radius rigidity are intrinsically interesting, but they are supplied mechanically by the distinct indexed formula and proof. After removing that overlap and the saturation cases, dimensions one and two use immediate coordinate/AM–GM bounds with a one- or two-input equality witness. No separate valuable, nonroutine remainder is established by those endpoint cases or by restating the arithmetic comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
