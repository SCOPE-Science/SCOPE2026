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

The primitive g on [beta,beta+1] has g(beta)=beta f(0) and g'=f on the shifted continuous interval. Polarization of the two norm forms gives -g''=eta g/y^2 with g'(beta)=(1-eta)g(beta)/beta and g'(beta+1)=0, where eta=1/s^2. The left sign comes from the atomic term and integration by parts at the lower endpoint. Under g(y)=sqrt(y) h(log(y/beta)), the input form is coercive on H^1 and the output form is the squared norm of the compact map h->(h(0),h). The input form minus a quarter of the output form is strictly positive for every nonzero h, excluding zero or imaginary wave number at a nonzero singular value. With eta=1/4+kappa^2, the left condition on h fixes the initial phase modulo pi as 2 atan(2 kappa), and the right condition adds atan(2 kappa). The resulting phase is strictly increasing from 0 to infinity. All roots j>=1 give weak and hence operator eigenvectors; the initial Robin condition leaves a one-dimensional solution space, ensuring simplicity. The phase at kappa=sqrt(3)/2 exceeds pi when T>0, giving 1<s_1<2. With the normalized atomic coordinate the atomic and continuous squared kernels sum to 1+integral_0^1 dx/(beta+x)=1+T. For fixed T, kappa_j~pi j/T gives the Schatten cutoff. For T tending to infinity at fixed j, kappa_j~pi j/T and 2-s_j~4 kappa_j^2. At small T the first root starts at sqrt(3)/2, with derivative -sqrt(3)/3, giving s_1'=1/2; fixed j>=2 instead have T kappa_j tending to (j-3/2)pi. Independent checks of the determinant in the mass coordinate and nonuniform-cell numerical compressions at three atom masses agreed at ranks 1–5; these do not replace the analytic proof.

## originality

PASS

The exact positive singular spectrum for one normalized endpoint atom, and its mass-dependent fixed-rank limits, are the supported distinct claims. The operator definition and upper norm bound are covered by general-measure Hardy theory; the squared Hilbert–Schmidt norm is an immediate kernel computation and is not relied on as an independent originality claim. The same leading edge coefficient is already known for a distinct finite Cesàro model, so the novelty is not the coefficient or inverse-logarithmic-square scale in isolation.

## value

PASS

A positive initial atom is a natural minimal departure from the atomless Hardy model, and that departure changes the compactness and creates a spectral endpoint condition involving the eigenvalue. An all-rank quantization resolves the approximation numbers and the transition between the near-Hardy norm edge and a rank-one limit. This yields more information than the prior strict norm inequality or a routine computation of the Hilbert–Schmidt norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
