---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Walsh convolution diagonalizes K on the 2^(n-1) antipodal classes with even character degree, eigenvalue binomial sum and multiplicity C(n,2k). Fractional-cosine representation gives lambda_2k=2^(n-1)c_p(-1)^(k+1) I_(k,n-2k). For odd residual exponent m, pair consecutive pi-intervals: F(u)>0 on (0,pi/2), antisymmetry and decreasing positive h_j(u) force I>0, even m nonnegative. Thus zero nullity for 0<p<2; exact weights are forced by K invertibility after testing against all sign vectors. p=2 expansion leaves degrees 0,2 only. Independent numerical binomial spectra at n=4,7,10 and p=1,1.5,1.8 showed predicted signs; examined check_rademacher_inertia.py. Restricts quadrature nodes to original Boolean sign cube.

## originality

PASS

General Krawtchouk transform calculus is standard and Koldobsky proves uniqueness of even p-cosine representing measures for p not even integer, so standalone exact-weight uniqueness is NOT original. The independently meaningful result is the strict degree-by-degree alternating Walsh inertia for absolute sum^p on antipodal cube for ALL n and 0<p<2, not provided by the inspected references. Dai-Kosov targets approximate Lp discretization with nonzero error, not this exact spectrum.

## value

PASS

The full inertia and strict nonvanishing of a natural Rademacher absolute-moment kernel is structural spectral information not implied by approximate cubature bounds; its exact sign formula also characterizes endpoint degeneracy and finite sampling rigidity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
