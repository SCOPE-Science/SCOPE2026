---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The matching decomposition into paired horizontal cycle dimers and, at even n, precisely two opposite alternating rail matchings is bijective. Setting y_i=a_i b_i r_i r_{i+1}, the signed sum equals (product r_i)tr(product [[1,y_i],[1,0]]) plus the two possible alternating-rail signs; their product is product y_i. Lucas parity forces odd multipliers when 3∤n; for 6|n the total count and every single-edge incidence count are even, so all amplitudes vanish mod4 by character expansion. Six exact base-length sign words attain the 1/2/4 bounds, two zero seeds give 3|n cancellation, and four length-six identity transfer blocks preserve trace and product sign for every larger n, proving all-order sharpness. Distinct y and freely chosen r,a yield at least 2^(2n)4^k zero frequencies. Independently recomputed four block products and two zero seeds from actual Python-code formulas. Exhaustive short transforms in package corroborate but do not prove all n.

## originality

PASS

A bipartite matching-detection Fourier transform is not the Boolean Walsh transform of fixed graph perfect-matching incidence masks. Even prisms have extra rail alternations with product coupling absent in simple cycle signed matching counts. Unsigned totals and detection uncertainty do not dominate sharp signed all-frequency minima. An older signed dimer transfer solution could in principle already contain the result; the relevant 2020 paper full text was not available in this run. Prior unsigned prism enumeration does not force the individual signs or sharp nonzero amplitudes. The odd-cycle signed classification is already covered elsewhere, yet even-prism alternating-rail analysis supplies a genuinely additional component.

## value

PASS

Sharp Boolean Fourier invertibility and pseudoinverse spectral gaps for a natural infinite graph family; even-prism alternating rails create a new mod-four obstruction not reducible to the prior odd-cycle signed matching problem. Exact sign-block propagation and an exponential zero family are coherent structural information, not an arbitrary small census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
