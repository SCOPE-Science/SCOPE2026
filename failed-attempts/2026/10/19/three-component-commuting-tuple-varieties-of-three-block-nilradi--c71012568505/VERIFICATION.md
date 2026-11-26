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

Block multiplication leaves only the upper-right commutator u_i v_j−u_j v_i, with all Z_i free. Equivalently each column of U wedges to zero with each column of V in k^t. If each side has a nonzero column, one from each side spans a common line, and all other columns must be on that line; otherwise U=0 or V=0. This proves the union over every extension, including characteristic two. The rank-at-most-one locus is geometrically irreducible by outer-product parametrization, of dimension t+r+s−1 by its one-dimensional nonzero factorization fibers. In the permitted range both pure loci have rank-two witnesses, and a mixed rank-one witness lies in neither pure locus. Thus all three are maximal; adding rst yields the dimensions. Equality of the first two forces r=s=d, and equality with the third then gives t=2+1/(d−1), so (2,2,3) is the sole equidimensional case, of dimension 18. Over F_q the two pure loci contribute q^(rt)+q^(st)−1 centered-block-free matrices, and each of (q^r−1)(q^s−1)/(q−1) mixed row lines gives q^t−1 matrices. Multiplying by q^(rst) yields the stated all-arity exact count. No scheme assertion was needed for the frozen proof.

## originality

FAIL

The commuting equations are exactly a generalized binomial edge ideal for the complete bipartite graph K_{r,s}, with independent central variables adjoined. Rauh's 2012 preprint/2013 paper, Section 3 Lemma 5 and Theorem 7, gives a general primary decomposition that yields the exact three component ideals here, not merely a related rank argument. The dimensions, integer equidimensionality test and finite-field census are immediate calculations in this explicit decomposition, not independent substantive additions.

## value

FAIL

The Lie interpretation is instructive, but the known graph-ideal decomposition determines every component immediately. The only residual calculations are equality of three known dimensions and a disjoint count of two affine spaces plus mixed rank-one matrices. The record does not establish any further geometric or arithmetic phenomenon that survives this coverage as an independently valuable contribution, and adjoining a scheme-reducedness claim would also be covered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
