---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible verification

Use `python3 verify_wiman.py` with Python 3 and NumPy. It requires no network, external data files or nonstandard computer-algebra software. A successful run prints `WIMAN_45_STABLE_BOUNDARY_FULL_SMITH_AND_SPECTRUM_OK`.

The script reconstructs the 45 lines by projective orbit from the generators in arXiv:1609.08648, reduces modulo 19 with the specified square root of five and cube root of unity, exhausts all 990 line pairs, reconstructs 201 intersection points, and checks their 120/45/36 multiplicity census and each line's 16 incidences. Against the independently documented 201 complex points (arXiv:1407.2966), equality of the reduced distinct-point count makes this a certificate of the complex incidence data.

All Laplacian entries are explicitly constructed. For the integer Schur matrix the script checks five spectral eigenvalues and multiplicities by an exact annihilating polynomial and trace moments, together with integral projector identities identifying all triple/quadruple/quintuple incidence eigenvalues. It checks the Schur polynomials and exact determinant, evaluates the 44-by-44 fraction-free minor, and computes 24 prime-local Smith reductions (six relevant primes, four deleted vertices). Reported valuations give an integral finite critical group whose product is the exact tree count.

The finite-field construction is not treated as a proof about characteristic zero without the 201-point reduction argument. The program proves a finite numerical certificate, not an infinite-family statement or historical novelty. It does not independently establish existence of a chosen smoothing. The geometric Néron-group identification invokes the classical theorem and assumes regular split semistability with unit thickness at all nodes. Independent mathematical audit has not been performed.
