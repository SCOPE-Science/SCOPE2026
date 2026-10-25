---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The integer-slab vertices are exactly binary vectors with weights a,...,b: perturb fractional coordinates, using integer endpoint sums when a slab bound is active. For an exchangeable binary vector with random weight K, mean mu, variance V and R=E[K(n-K)], its covariance is C=(V/n)H + R/(n(n-1))(I-H). Any vertex-supporting distribution with (x-m)^T C^{-1}(x-m)<=n for all vertices yields the unique minimum-volume ellipsoid { (x-m)^T(nC)^{-1}(x-m)<=1 } via the trace/determinant AM-GM certificate; equality forces both center and shape. When D=(n/2-a)(b-n/2)>=n/4, a mixture of extreme and central layers has mean n/2 and V=n/4, giving C=I/4 and all vertex contacts. Otherwise, optimize p(1-p)(A_a+p Delta)^(n-1) with A_k=k(n-k), Delta=A_b-A_a: strict log concavity gives the unique p in (0,1) and stationary polynomial A_a+(n Delta-2A_a)p-(n+1)Delta p^2=0. Stationarity makes the Mahalanobis orbit radii q(a)=q(b)=n; q(k)-n=eta(k-a)(k-b), eta=1/V-(n-1)/R. Reflecting if necessary to a+b<=n, the stationary identity (n-2mu)R=(n-a-b)(R-(n-1)V), together with strict concavity of log(VR^(n-1)) and its negative derivative at mu=n/2 when D<n/4, proves eta>0. Hence all interior allowed ranks lie strictly inside and exactly endpoints contact. The asserted principal axes, volume and balanced threshold follow directly. A new independent symbolic/bisection checker verified endpoint identities algebraically, 7,769 slabs and 81,583 layer inequalities for n=2..35, with 17,820 strict interior rank comparisons, and independently compared broad theorem chord candidates for 776 non-spherical slabs n<=19. These checks corroborate, not prove, the infinite statement. The n=2/simplex, a=0 or b=n, b=a+1, centered-slab and exact D=n/4 boundaries were examined.

## originality

FAIL

The published 2026-10-11 result Exact Löwner ellipsoids of arbitrary rank-selected Boolean polytopes (3c04f47dc8c3, original pinned RESULT.md blob 8cbcaeb068beaf0d279bb4d566017f346a00801e) already determines the unique ambient-Euclidean Löwner ellipsoid, center, squared semiaxes, volume and exact contact ranks for every full-dimensional rank set S. Taking S={a,a+1,...,b} gives precisely the present polytope. Its moment-polygon cube test specializes to (n/2-a)(b-n/2)>=n/4, and its candidate-pair determinant formula on the extreme pair is literally p(1-p)(A_a+p(A_b-A_a))^(n-1), with identical quadratic p equation and shape V H+R/(n-1)(I-H). The submitted positivity/factorization proof establishes that the extreme pair wins in the interval case, hence the rest of the submitted classification is a specialization of the published stronger procedure. This is scientific coverage, not an allegation of copied work: the submitted source commit 2026-10-11T13:08:56Z preceded the more general source commit 13:09:12Z by sixteen seconds and both were indexed at 13:31Z.

## value

PASS

Consecutive cardinality slabs are natural concrete 0–1 polytopes including truncated cubes and uniform-matroid independence bodies. The sharp D=n/4 spherical-versus-anisotropic transition gives an interpretable exact contact-orbit phase diagram, complete center and eigenaxis formulas in all dimensions, and a particularly simple balanced thickness threshold (b-a)^2=n. These data provide a useful benchmark for convex geometry and exact D-optimal-design calculations, rather than an arbitrary unmotivated small-instance invariant. Value does not restore originality: this class and all exact parameters are already determined by the stronger published rank-selected theorem. The claim is a useful specialization; it should not be accepted as a separate novel finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
