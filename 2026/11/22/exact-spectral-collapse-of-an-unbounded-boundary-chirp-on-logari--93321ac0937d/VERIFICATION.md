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

With u=−log|z|² the density is Γ(a)⁻¹u^{a−1}e^{−u}du times Haar. Angular orthogonality and the Γ integral give the complete normalized monomials, and symbol-square integrability reduces to Γ(1−a)/Γ(a). Thus compression on polynomials is defined. Its N=n+1 diagonal moment is N^a/Γ(a) times the transform of u⁻¹ᐟ² exp(−Nu+ic/u). For positive real β=b², substitute u=x²: differentiation and inversion x↦b/(√N x) give the Gaussian integral differential equation F′=−2√N F. Holomorphy for Re β>0 and dominated convergence to −ic justify the principal-root expression, with positive phase +√(2cN). The eigenvalue list tends to zero and is p-summable in modulus for every p>0, proving a unique compact normal extension and all Schatten statements. Zero is in the full spectrum as a limit, not an omitted monomial eigenvalue. The rescaled sums are ordinary Riemann sums on finite intervals with a uniformly negligible tail by eventual monotonicity and integrability; the change y=p√(2x) gives the stated Γ constant. The continuous maximizer is x=2γ², and grid points cN approach it, giving the stated norm limit. Removing the phase gives precisely A_a N^γ, so no bounded modulus or zero-chirp extension exists.

## originality

PASS

Neither radial monomial diagonalization, the half-order Gaussian–Laplace integral nor the qualitative bounded/compact cancellation phenomenon is new. The supported distinct content is the exact quantified collapse and sharp weak-chirp norm and quasi-norm blow-up for this family. The inspected analytic-space and radial-symbol results give qualitative criteria or different models; the transform itself does not give a weak-parameter spectral sum or lattice maximum.

## value

PASS

A logarithmic radial moment model gives a quantitative benchmark for cancellation that qualitative boundedness criteria leave open. The half-order balance selects an explicitly solvable chirp with an unbounded comparison operator. The calculation separates the single dominant-mode scale from the cumulative contribution of order 1/c modes, gives sharp constants even for quasi-Schatten classes, and identifies how the regularization is lost at zero chirp.

The dated certificate retains the supplied scientific assessment, sources and limitations.
