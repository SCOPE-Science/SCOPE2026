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

Phase covariance reduces twice the numerical radius to the Jacobi spectral supremum. Translate the defect to 0,1; within each parity the half-lines are nested compressions with dense union. The periodic tail has essential upper edge S=u+v by Floquet theory (or the test vectors on long constant stretches at the band maximum and the row-sum bound). For c<=u, comparison on absolute values with the unperturbed Jacobi operator gives the matching upper bound at every finite depth. For c>u the larger root lambda of F_u(z)=c z^2-(u^2+c^2)z+c(u^2-v^2) lies above S because F_u(S)=-S(c-u)^2. It is reproduced by the reflected positive decaying mode with central value 1, adjacent value r=(lambda-c)/v and cell ratio rho=uv/(c lambda-u^2). Indeed (lambda-c)(c lambda-u^2)=c v^2 gives lambda r=v+u rho and lambda rho=(u+v rho)r. Both r>0 and 0<rho<1; the positive-eigenfunction quadratic-form identity rules out higher spectrum. The half-line truncation loses exactly one boundary term in the eigenvector Rayleigh relation, with size O(rho^m) and retained norm bounded below. If a<b<c, both larger roots are between S and 2c, and F_a(z)-F_b(z)=(b^2-a^2)(z-2c) makes the a-replacement root strictly larger. For a<c<=b the other phase sits at S, establishing the full dichotomy, including equality cases and a=b. The worked example recomputes to 1.563137556011 for the even limit.

## originality

PASS

The supported contribution is the fixed-c unequal-background pair of exact limiting radii, their strict ordering/dichotomy and the geometric estimate. The homogeneous case and a stronger statement about the finite-depth plateau are established. There is genuine mathematical overlap with the companion quartic-window proof; the companion expressly credits the fixed-c limit as existing work and does not present it as its new result. That overlap is not evidence of an independent earlier discovery, and the shared date does not determine priority.

## value

PASS

A defect displaced to infinity converges locally back to the unperturbed coefficients, yet the numerical radius need not converge, because the translated spectral defect remembers the lattice phase. The exact criterion and ordering identify precisely when that failure happens, and the decay bound sets the finite-distance scale of the two limits. These are natural global spectral questions for the first nonconstant periodic background, not parameter-picked examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
