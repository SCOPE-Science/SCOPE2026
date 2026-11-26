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

Independently rederived the linearized symbol of the matched PDE. In angular Fourier coordinates, sI−M has diagonal s+Γ_m+d_m k², with Γ=(0,1,3,4,3,1), d_0=1, d_m=1−r otherwise. Each off-diagonal shift from m to m±1 contributes ikp(1−r−rδ_{m0})exp(±iθ)/2. In the determinant the only nonconstant angular terms are the two full six-cycles: all other permutations use diagonal entries and disjoint adjacent transpositions whose phases cancel. The six-cycles have permutation sign −1 and i⁶=−1, giving exactly +k⁶p⁶(1−r)^5(1−2r)cos(6θ)/32 in the characteristic polynomial. Its s-derivative at the simple root (s,k)=(0,0) is 36. This yields the claimed coefficient with the opposite sign and denominator 1152. The diagonal k² term and the two transpositions involving mode zero give the stated a₂. The determinant is real and polynomial in k² and cos(6θ); the simple-root implicit expansion is uniform on the compact angular range at fixed r,p. At r=1/2 the transport column of angular mode zero vanishes, so its uniform orientation vector has eigenvalue −k² at every wavevector, regardless of any crossings. The heading–bisector difference and its sign follow. The archived finite eigensolver compares the branch at sample parameters, not an exact symbolic proof; the determinant derivation proves the result without executing it. RESULT.md's reference to an 'infinite-wave-number-limit argument' in its verification paragraph is a wording slip, not the small-k argument actually used.

## originality

PASS

Credit the continuum model and its isotropic fourth-order reduction as prior. The inspected sources do not evaluate the sixfold sixth-order coefficient of the exact time-dependent density branch for general occupancy or state its exact uniform-vector cancellation at half filling. The assessed contribution is this spectral refinement, not the model, the selection rule alone, or the known fourth-order closure.

## value

PASS

This resolves where spatial symmetry first permits the exact density mode to distinguish headings from bisectors in the existing triangular-lattice continuum model, and determines which direction wins at fixed small wave number on each side of half filling. It identifies the occupancy boundary where anisotropy vanishes exactly for the uniform branch and gives a benchmark missing from the isotropic fourth-order model. This is a meaningful local spectral invariant, not a claim about nonlinear phase selection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
