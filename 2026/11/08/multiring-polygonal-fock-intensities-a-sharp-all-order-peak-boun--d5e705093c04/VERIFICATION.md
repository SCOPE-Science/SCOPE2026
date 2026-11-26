---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Differentiating |w-a_j|^2=r^{2n}+a_j^2-2a_jr^n cos(n theta) gives strictly signed angular log derivative away from zeros; the negative-power rays have strictly negative angular curvature, the positive-power rays cannot support maxima, and simple zeros are nondegenerate minima by their positive quadratic leading term. At the origin H/H(0)=1-|z|^2+O(|z|^3). On a negative-power ray the log derivative is -2r times R(r)/Q(r^n); the integer powers n j-2 and n j do not collide for n>=3. The 2k Descartes variations bound roots with multiplicities. Every off-origin maximum requires a + to - crossing, preceded by a distinct - to + crossing because the derivative starts negative; the exactly analytic, nonconstant radial profile excludes flat intervals and includes degenerate isolated peaks. In the construction with x=r^2/n, the sign is S(x)-x. At all samples except the last, max(c_i,x)<k and |c_i-x|>=1/4, hence the ratio bound 1-1/(4k); at the final sample x=k+1/4 the largest ratio (k-1/2)/(k+1/4) also obeys that bound. The step approximation error is <=k exp(-n/(8k))<=1/8, so 2k disjoint intervals force 2k simple roots. The mixed radial-angular derivative is zero on each symmetry ray (the angular derivative vanishes identically there), so at each of the k radial maxima the full Hessian is negative definite. Nondegenerate critical points persist by the implicit function theorem and the global bound excludes an increase. Independently evaluated the sample signs in exact rational arithmetic at (k,n)=(1,18),(2,46),(3,78),(7,226),(10,352); all alternated from minus to minus. The packaged check_multiring.py covers six finite even-degree cases; the analytic argument also handles odd n and does not infer universal validity from the check.

## originality

PASS

Best of inspected evidence, the arbitrary-k count and constructive uniform nondegenerate saturation remain distinct. Neither the Chern critical-point formulation nor the one- or two-ring Descartes mechanism should be credited as entirely new. In particular, the regular-polygon lens literature already has the single-ring radial equation, Descartes bound and exact two-root transition after rescaling.

## value

PASS

The deterministic sharp count in a natural symmetric finite-stellar-rank family is useful, especially because the witness produces an arbitrarily large number of concentric peak rings without relying on degenerate critical points or limiting parameters. The explicit finite degree condition and openness make it a reusable benchmark for peak geometry, despite sharper single- and double-ring cases and no claim of optimal thresholds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
