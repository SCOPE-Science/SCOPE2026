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

Independent coordinate phases make monomial matrix entries off the diagonal vanish; block-unitary invariance makes the remaining entries scalar on each homogeneous block sector (equivalently, the tilted squared block radii have independent Gamma laws with shape k_j+κ_j). Fix a monomial of block degrees κ and tilt the product measure by its normalized squared modulus. In every unused block the first normalized coordinate squared modulus is exponential of mean and variance one, so the centered variables Y_j are orthonormal in the tilted L². Inserting one particle multiplies the tilting density by 1+Y_j. Bessel gives the square-summability, and hence convergence to zero, of the eigenvalue differences for each bounded symbol. This does not require uniform convergence over bounded symbols or over κ. The pointwise-in-κ insertion property defines a unital, self-adjoint, sup-norm-closed subalgebra; diagonal operator norm is the sup norm. A compact element has eigenvalues tending to zero on each orthonormal inserted sequence, thereby vanishing at every fixed sector. The same vectors and the fixed sector give the norm lower bound max(|1−c|,|c|), attained by I/2. Finite-prefix restrictions of a generator come from integrating its symbol over the independent tail, giving inclusion in the finite-coordinate envelope also for the generated algebra. The restriction of P_κ is zero or a singleton. For an independent check of singleton membership, in a finite prefix the block-j symbol exp(−||z_Ij||²/u_j) has eigenvalues 2^(−k_j−d) at block degree d; each such eigenvalue is isolated, giving the level projection by continuous functional calculus. Multiplying the finitely many level projections gives the singleton. Thus the inclusion is strict for the actual algebra in Problem 1, without asserting a solution to its separate linear-closure question. This is an analytic proof; no numerical test is required or used.

## originality

PASS

The primary source explicitly leaves the infinite product sector projection outside its available membership results and asks the envelope equality question. The present obstruction is for the generated norm-closed algebra and gives an attained distance, not just non-representability by one symbol. Priority for the compactness consequence considered alone remains qualified by an unavailable older article.

## value

PASS

Resolves the explicitly posed finite-coordinate-envelope equality problem in the negative and proves the conjectured nonmembership for each specified projection. It further gives exact operator-norm separation and excludes all nonzero compact elements of the relevant algebra. The insertion invariant explains the difference between finite and infinite Gaussian block models beyond a single counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
