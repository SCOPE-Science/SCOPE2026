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

The cosine output P is antisymmetric about 1/2 by the Bernstein reflection identity, so its constant and even modes vanish. Strictly decreasing samples imply P'<0 and integration against sin(pi*u) shows positive first cosine integral. At degree 4 the coefficient vector (1,c,0,-c,-1) gives the cubic polynomial 1+(-4+4c)u+(6-12c)u^2+(-4+8c)u^3. For odd k, writing h=k*pi, integration by parts gives 8(1-c)/h^2+(-48+96c)/h^4. The endpoint minima on |c|<=1 are positive for k=1 and odd k>=3. Degree elevation preserves this vector form for n<4. In the clustered limit the central tie receives zero, S_(2r)=S_(2r-1) by degree elevation, and differentiating gives -S' equal to twice the Beta(r,r) density. For S_5 the endpoint derivatives give -240/(3*pi)^4+2880/(3*pi)^6, the claimed negative raw integral. On [0,1/2] the sine weight changes from positive to negative just at 1/3; multiplying the r=3 integrand by [u(1-u)]^(r-3), increasing on this half, bounds the new integral above by its value at 1/3 times the negative base integral. Thus the sign holds for every r>=3. Uniform limit and continuity give strictly ordered examples at positive epsilon. The beta second and fourth central moments give the stated expansion with O(r^-2), with the factor of two between a positive-frequency cosine coefficient and its raw integral accounted for. The frozen numeric script was inspected, not executed; it is supplementary.

## originality

PASS

The n=5 cluster counterexample with the same input and output mode is exact prior coverage, and the cubic guarantee is a corollary of stronger prior work. The material surviving content is the uniform quantifier over every higher degree with one fixed input and first possible offending mode, together with the limiting spectral strength and the universal degree-4 fixed-input guarantee. No checked source covers that uniform statement.

## value

PASS

The result quantifies a concrete failure of the usual Bernstein circle-positivity theorem under symmetric perturbation: a single common input and its earliest possible offending mode provide witnesses at every eligible degree. The half-beta sign mechanism and limiting negative strength explain why the phenomenon is not confined to a special degree-five example or washed out at large degree.

The dated certificate retains the supplied scientific assessment, sources and limitations.
