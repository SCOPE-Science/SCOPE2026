---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Checked the cited Theorem 6 of arXiv:2611.22365 for the actual finite-field bilateral full shift and the definition with n >= 0. It requires a nonzero determinant and excludes every monic irreducible characteristic factor over the Laurent ring's fraction field with unit constant term. All monic factors have coefficients in the integrally closed Laurent ring. In particular even in the reducible case a unit determinant forces both linear constant terms to be units, since their product is a unit. With nonunit nonzero determinant a quadratic irreducible factor cannot obstruct, so it suffices to test roots cz^j. Factoring z^L out of A gives a polynomial matrix H supported in [0,U-L]; its monic characteristic equation makes the scaled root integral, hence polynomial, and its square has unmatched highest degree if j-L>U-L. This handles all finite Laurent stencils, including L=U; the zero map fails surjectivity. Theorem 4(1) of arXiv:2611.16746 gives width including zero times log p, with inversion of the spatial variable leaving width unchanged. In the span-one binary case the only possible unit roots are 1 and z; their two tests are polynomial identities. If both occur, the determinant is z, already excluded. Independent exact replay used the four values f(0),f(1),f(2),f(3) of each of the 16 linear maps on two-bit column vectors, with polynomial supports computed by symmetric difference and exponent convolution. The trace–determinant rows, written in increasing support bit-mask order, were 10,10,6,6,10,10,6,6; 18,2,6,6,6,6,18,2; 18,6,6,18,2,6,6,2; 18,6,18,6,6,2,6,2. The exclusion counts were 64,84,18,18 and there were 72 survivors. The five nonempty (entropy,strong-transitivity) counts in record order were 40,102,18,42,54. Acting by the six bijective maps on each pair via p∘f∘p^(-1), taking the orbit of the least unseen pair and deleting it, gave cell counts 12,17,3,10,14 and sizes 1:4, 2:6, 3:12, 6:34. Burnside checks the total: a nonscalar 2x2 invertible matrix has a cyclic vector, so its commutant consists exactly of the four linear polynomials in it. The two frozen scripts were inspected as text; finite replay supports the census, not the infinite theorems.

## originality

PASS

Best-of-knowledge pass for the evaluated joint population and onsite orbit classification. The general entropy and strong-transitivity criteria are prior art, and the finite Laurent root test is their explicit rank-two specialization, not a separate originality basis. The joint distribution and orbit refinement require a separate coefficient-incidence and conjugation calculation.

## value

PASS

This is the full smallest binary matrix-valued span-one family, not a parameter list hand-picked for the outcome. The joint table separates positive temporal entropy from strong transitivity and provides exact incidence data for testing classification algorithms; the orbit strata show which counts survive removal of redundant onsite coordinates. It is a finite baseline, not a classification of nonlinear four-symbol automata or general dynamical conjugacies. The specialized root test also avoids factorization on the stated rank-two stencil without claiming the same for higher rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
