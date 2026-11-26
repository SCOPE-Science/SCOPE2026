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

Parseval for the sum of the Poisson kernels gives 2 sum_{m>=1} u^m |S_m|² with u=r². Root-of-unity filtering gives the exact reference value. The angular second-order coefficient has the positive squared Fourier perturbations and a subtraction n m²||epsilon||² in the zero residue class only; pairing real conjugate modes yields kappa=n(A_k+A_{n-k}-2A_0), including the even Nyquist normalization, with Hessian 2 kappa. All angular derivatives converge for u<1, and rotation invariance reduces the remainder to the centered perturbation. Independently checked the hyperbolic residue identity: with x=-log(u), t=nx/2 and a=k/n, the generating function for the residue difference is -2 sinh(at)sinh((1-a)t)/sinh(t); differentiating twice gives kappa=-(n³/2)G_a''(t). For the parallel sum vw/(v+w), its negative-semidefinite Hessian is a negative rank-one form and both partials are positive, so the strict second-derivative signs of tanh(at) and tanh((1-a)t) imply G_a''<0. The first nonzero residue term gives the small-u hierarchy; the cubic term -a²(1-a)²t³/3 gives k²(n-k)²(1-u)/2 at the other end. At fixed n the finite set of curves has distinct minimizing frequency types in the two limits, so a switch occurs, with no uniqueness established. Bounded independent replay: python /workspace/branches/replay_frozen.py 5 checks a symbolic Taylor coefficient and compares exact differentiated pair-kernel curvatures to direct residue sums at five sizes and four radii, including endpoint order tests; it is not used for general positivity. The mathematical formulas are unchanged by the repair. The repaired slogan correctly distinguishes the highest distinct frequency at odd n from the even Nyquist frequency.

## originality

PASS

Pass specifically for the exact angular quadratic spectrum and forced reversal of the minimizing frequency for every n>=5, not for the minimizing configuration. The original prior-work discussion missed a dominating qualitative result: the exact pair potential is strictly completely monotone in squared chord distance, so Cohn–Kumar universal optimality already gives regular-polygon minimality globally within equiradial angular placement. The corrected RESULT.md explicitly adds this reduction and credits the prior theorem; the corrected slogan describes the surviving spectral contribution. The degree-four exact theory is a close genuine overlap at an excluded degree, not assumed earlier based on the catalogue date. Available sources do not establish an equivalent spectrum or reversal for the claimed degrees; residual risks remain.

## value

PASS

Beyond prior knowledge of the minimizer, exact eigenvalues give sharp local conditioning and diagnose which angular deformation costs least. Their opposite frequency hierarchies at small and large radius establish a genuine qualitative change in spectral response that global optimality alone misses. This supplies an explicit benchmark in phase distortion and circular kernel energy without claiming transition uniqueness, uniformity across growing degree, or radial stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
