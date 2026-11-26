---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

If commuting rank-one operators have a nonzero common product, their images coincide; both operators kill that line by square-zero, contradicting the nonzero product. In a nonempty clique each covector therefore kills the image span U, giving containment in C(U). The images and covectors of the full C(U) span U and U⊥ respectively, so no new vertex can commute with all its members, and U is recovered from the clique. Dividing the nonzero vector/covector factor count by q−1 gives the sizes; minimizing q^r+q^(n−r) gives exactly the stated middle ranks. For the polynomial use the unique image/covector span pair (U,W), with W≤U⊥. The number of pairs is [n choose r]_q[n−r choose s]_q. In fixed smaller spans of dimensions i,j all subsets contribute (1+z)^((q^i−1)(q^j−1)/(q−1)); inversion on the product of the two subspace lattices isolates the exact spans with the displayed coefficients. The empty clique is included separately. The argument uses finite-field algebra in every characteristic. Fresh direct matrix-product enumeration over F₂ gives coefficients (1,21,42,14) at n=3 and (1,105,1260,3780,5460,5040,3150,1290,315,35) at n=4, including the empty clique.

## originality

FAIL

The assigned mathematical claims are demonstrably covered in the present catalog by a distinct indexed record, not merely a similar title or a reference to the identical frozen item. The November 1 record proves the same maximal-clique classification and computes every coefficient of the same clique polynomial. Its one-span tuple formula becomes the subset formula by Stirling inversion; the frozen two-span version refines intermediate summands without adding a different final invariant. The November 2 double-flag formula also covers that intermediate refinement by specializing all ranks to one. These findings are about equivalent indexed coverage, not historical priority: the matching records have later catalog dates than the assigned source, and this audit does not claim they anticipated it.

## value

PASS

The theorem answers a natural classification question for an incidence graph and gives a uniform size distribution for all cliques, beyond local graph statistics. Distinguishing true matrix vertices from scalar classes and using exact spans to avoid overcounting makes it useful as a mathematical description of the graph. This assessment of the question and complete answer does not give credit for novelty over the verified catalog coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
