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

For n>=4 the difference of two incidence columns with two points in common gives each e_i+e_j; these span the coordinate-sum kernel, and any triple column has sum one. Thus B is onto over every characteristic-two field. The diagonal and off-diagonal entries of Q=BB^T are the two stated intersection counts, modulo two, giving I,I+J,0,J; when J occurs n is odd, so J²=J. Ranks of F,F²,F³ are 2n,n+d,2d using surjectivity/injectivity; F^5=F³ shows F²=I on im F³ and the direct complement is ker F³. On that complement the ranks of F and F² are 2(n−d) and n−d, so there are n−d size-three chains, no size-two ones and m−2n+d size-one chains. Fixed states solve Qu=u and w=B^T u: their dimension d forces exactly d size-two blocks at eigenvalue one on the 2d-dimensional recurrent summand. Over F_q the nilpotent kernel sizes and the unconstrained recurrent part yield the four cumulative exponents; the Fitting fibers give q^(N−2d) configurations per recurrent coordinate, hence the stated orbit basins. At n=4 the nilpotent part vanishes; in the residue-zero class at n>=8 it consists of size-one chains, while the other classes have positive size-three counts. In residue two there are no two-cycles. The source checker and captured output were inspected, not executed. An independently written binary power/rank check for n=4,5,6,7 reproduced ranks [8,8,8,8,8], [15,10,9,8,8], [26,12,6,0,0], [42,14,8,2,2] from F^0 through F^4 (replay: branches/3f9330f6-8de5-425f-833f-2fb35a1c4698/independent_rank_check.py); it does not replace the all-order and all-field proof.

## originality

PASS

The full-rank incidence fact, design intersection identity and linear dynamics framework are prior material. The narrower supported contribution is the exact four-residue Jordan/census classification for the complete triple-incidence graph. The strongest related exact dynamic statements treat different graphs; the shared design calculation alone is not the census.

## value

PASS

The complete triple system is a canonical uniform incidence family, and classifying extinction versus recurrence is a natural dynamical invariant. The result sharply distinguishes mod-four regimes, including total extinction, only q² recurrent states, and exponential recurrent spaces, and quantifies sharp transient times and basin populations. It is not just a rank recomputation: the incidence parity and the temporal Jordan decomposition explain those differences for all finite characteristic-two fields.

The dated certificate retains the supplied scientific assessment, sources and limitations.
