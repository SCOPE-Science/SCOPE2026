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

Taking the trace of a power of the rank-one product gives the off-diagonal block A=B^{circ r}; the SVD gives the full spectrum 1±s_j(A). For r<1 the constant-vector test is strict unless B is a permutation. For r>1 each nonsingleton component has all row and column sums of A strictly below one (an entry 1 would isolate a row-column pair), giving the common-ray criterion. Jensen gives the global fractional edge bound; equality in the nonnegative symmetric dilation forces degree saturation on a Perron support component, hence full uniform overlap by strict row/column Jensen. Each B_j B_j^T is irreducible, positive semidefinite and stochastic; its simple top eigenvalue gives exactly one critical branch. Differentiation with left and right constant unit vectors gives -h_j for the leading singular value. Taking the maximum over finitely many branches gives the opposite max/min entropy selections and the strict spectral gap to all nonleading branches gives the asserted local inertia.

## originality

PASS

Best-of-knowledge pass for the distinct fixed-pair classification: all overlap supports, sharp equality conditions, and component-resolved critical nullity, asymmetric slopes and inertia together. Neither the MUB counterexample nor the standard entropy differentiation identity is new. A Markov-pressure comparison applies to the symmetric dilation itself and reproduces the scalar slope, not on its own the fixed-pair classification with the sharp extremizer and signed branch multiplicities.

## value

PASS

The theorem resolves when a widely used fidelity-derived Gram matrix loses positivity on two complete bases, addressing more than a bad example. The support components identify which modes lose positivity and predict the two sides of the edge from different measurable entropies; with unequal component entropies or a shared ray the asymmetry is concrete. The sharp MUB uniqueness and the arbitrary-support classification make the answer useful despite elementary tools.

The dated certificate retains the supplied scientific assessment, sources and limitations.
