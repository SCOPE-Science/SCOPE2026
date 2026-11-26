---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For linear indexed words the pair-count balance forces equality of endpoints by the divergence identity; on a closed path a divergence-free integer current vanishing on the cotree must vanish also on the tree. Orthogonality on the cotree torus gives the stated trace of H(θ)^{n−1}, including all q roots. The Hermitian eigenvalues are in [2−q,q], and equality at q in the triangle/Rayleigh bound requires all phases to be a vertex gauge; the star fixes this gauge, leaving exactly the zero point on the torus. Independently checking the Hessian, for a unit vector u the quadratic form of qI−H is ∑_{edges ij}|u_i−e^{iθ_ij}u_j|² with zero angles on the star. At zero the single minimizing vector is uniform up to phase; its analytic continuation has real and imaginary first variations. The leading energy minimizes a nonnegative real-gradient square and the imaginary-gradient square with imposed cochain Jθ/√q. The real gradient can vanish; projecting the imaginary residual onto the cycle space gives θ^T J^T P J θ/q. Both bounds follow by expanding the analytic minimizer and testing the minimizing first-order trial vector. Conjugation eliminates odd orders. The fundamental-cycle Gram matrix I+C^TC has determinant q^{q−2} by the complete-graph Laplacian on the nonroot vertices and Sylvester's identity. The spectral gap and positive Hessian justify Gaussian localization with determinant factor; dividing by q^{n}, not q^{n−1}, accounts for the additional 1/q. The binary H has constant eigenvalues 2,0 and gives the exact formula for n≥2 (n=1 is separately all letters). In the ternary cycle the three currents of a closed walk coincide, so the net signed increment is three times that common current; zero signed sum also implies closure. Counting balanced increments gives precisely the stated central trinomial sum including n=1. The supplied exhaustive and transfer programs plus verification notes were inspected, not run; the all-q result is supported by the analytic argument in RESULT.md lines 30–86.

## originality

FAIL

The general return-probability local central limit theorem for walks on crystal lattices covers the principal asymptotic under an equivalent exact model. This is not a priority judgment based on an inaccessible article or on nearby word-class counts. For q≥3 take the maximal free abelian cover of K_q with cotree coordinates from a star and give the simple walk holding probability 1/q. A uniform length-n word corresponds to L=n−1 of these steps with uniform start over base vertices. Its balanced-pair event is exactly return to the same lift: the base endpoint is the same and the integral cycle current is zero. Star triangles give all coordinate generators, verifying the full deck lattice Z^d. The covariance in these coordinates is elementary: correct the oriented edge increments J by a vertex coboundary to get the divergence-free representative PJ, which makes the corrected increments martingale differences. Stationary directed edges each have probability 1/q² (holding steps contribute zero), so Σ=2J^TPJ/q². The stationary mass of each base vertex is 1/q. The aperiodic crystal-walk return LLT gives (1/q)(2π L)^{−d/2}(det Σ)^{−1/2}; using the elementary fundamental-cycle Gram determinant q^{q−2} gives exactly the frozen constant. Alternatively remove the holding steps: the nonholding walk has period two (zero current forces an even number of traversals in total and a two-step reversal is possible). The period factor two cancels with the asymptotic even-parity probability one half under binomial mixing at time L(q−1)/q. Thus this implication does not depend on a loop convention for the prior theorem. The binary and ternary formulas are trivial endpoint and balanced-increment counts, with the latter not asserted new in the record. No separate nonmechanical remainder is supported.

## value

FAIL

Counting reversal-balanced words is a natural question and the Fourier proof is clear, but the claimed exact constant is the standard crystal-walk return constant on a complete base, with the standard full-cycle covolume. No new periodicity obstruction, adaptation beyond the existing reversible finite-base LLT, or further independent invariant is needed. The binary and ternary checks are basic consequences of endpoint balance and zero signed increment. The package works as an illustration of the return theorem, not as a separate nonmechanical finding under the stated standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
