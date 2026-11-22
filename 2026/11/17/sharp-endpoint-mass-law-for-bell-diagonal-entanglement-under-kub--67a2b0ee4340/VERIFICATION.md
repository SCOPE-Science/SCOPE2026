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

Every Bell-diagonal trace-one state is a four-probability vector, separable iff its largest component≤1/2, and its standard negativity after normalization is max(0,max_i w_i/W−1/2). For scalar Kubo–Ando harmonic mixture m(a,b), the endpoints contribute c a+d b and harmonic–arithmetic inequality yields m(a,b)≤(1−θ)a+θb. For any coordinate i with input weights a_i,b_i≤1/2, output w_i≤L and sum of other outputs≥R=c(1−a_i)+d(1−b_i). Ratio L/(L+R) is nondecreasing in each a_i,b_i, and at (1/2,1/2) equals 1/(1+c+d), giving the exact universal negativity upper bound, with s=0 separately handled. The two rank-two separable inputs with common Bell projection yield nonzero output weights (1,c,d,0)/(1+c+d) and attain it. When s=1 all means are weighted arithmetic and outputs are separable; when s<1 interior harmonic mass forces strictly positive non-common components, so no strictly positive input pair attains the bound, although mixing with maximally mixed states approaches it by continuity. Independent exact rational vertex-pair checks over 6×6 Bell-octahedron boundary vertices for three harmonic representing measures confirmed the bound and sharp witness; these finite tests do not establish the theorem.

## originality

PASS

Kian arXiv:2605.26272v1 Theorem 3.3 gives the qualitative conclusion that only arithmetic Kubo–Ando means preserve separability and constructs a local-curvature non-PPT example. The full primary HTML has no sharp Bell-diagonal trace-normalized negativity bound in its inspected theorem/proof or Choi applications. Harmonic endpoint measures and Bell-diagonal PPT identities are known separately, but together do not automatically yield the sharp global optimum unless one proves ratio monotonicity and equality. The quantitative exact dependence only on c+d survives as qualified novelty; older scalar mean or Bell state optimization formulations remain a risk.

## value

PASS

The natural quantitative question after separability-preservation rigidity is how large entanglement negativity can be created by a non-arithmetic mean. The smallest commuting two-qubit entangled-capable family permits a complete answer for every Kubo–Ando mean, even nonsymmetric, with one universal maximizer and a sharp endpoint mass classification. This is a motivated exact quantum-information invariant, not a loose counterexample or mere proof that entanglement can occur.

The dated certificate retains the supplied scientific assessment, sources and limitations.
