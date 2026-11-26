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

The mathematical claim is the rank and global injectivity of the generator map on a known admissible support for an unknown law Q. A susceptible's pool has N-1 members including I infectives. Summing first and second inclusion indicators gives E[l^2]=TI/(N-1)+T(T-1)I(I-1)/((N-1)(N-2)). With known beta, the rates at I=1 and I=2 and S>0 recover M1 and M2 even at N=3; the reverse implication includes recoveries. Put p=1-eta. There is a one-word row-operation error in RESULT.md line 39: ADD the second row to the third to get t^(p+1), not subtract. With correct row reduction, divide each column by its positive t^p to obtain [t^(eta-1),1,t]^T. For eta not 1 or 2, t^(eta-1) has strictly nonzero second derivative of fixed sign on t>0, so no three distinct points are collinear. At eta=1 or 2 this row duplicates one of the other two, and 1 and t give rank two for at least two distinct columns. This also covers singleton and two-size supports. For the joint moments multiply each column of [1,t,1/t]^T by t to get ordinary Vandermonde rows up to permutation. In every deficient case a nonzero kernel vector has zero sum and can perturb any strictly positive law in both directions; this is global noninjectivity, not a claim that every boundary law is individually ambiguous. The two rational pairs have means 2 and inverse means 1/2 as claimed. The wording 'known ... law Q' in the first paragraph should say 'unknown' as made explicit by the inverse problem and scope. Independently checked 60 exact subset-enumeration expectations, the curvature formula, the joint determinant (s-r)(t-r)(t-s)/(rst), and a finite set of noninteger exponents; replay python3 -B /workspace/branches/independent_replay.py 2. Frozen check.py was inspected, not executed.

## originality

FAIL

The rank classification and pooled-protocol recovery are mechanically implied, not just related to an earlier model. Muslim's primary source already proves the exact same generator-to-power-moment equivalence for general q and gives the actual prescribed-support matrix and rank/nullspace criterion. At q=2 the matrix entries are exactly 1,t^(1-eta),t^(2-eta). Positive column scaling turns the classification into the elementary test for when t^(eta-1) is affine at three distinct positive points; it is affine exactly at exponents zero and one, and otherwise has fixed-sign nonzero second derivative. The combined experiment puts the two opposite power rows beside normalization; positive column scaling gives the ordinary 3-row Vandermonde. The prior need not tabulate the two numbers or print the paired experiment for both advertised increments to be direct consequences. This is substantive prior coverage by implication, not a failure from a search miss.

## value

FAIL

The focal sampling inverse problem and the two normalizations are motivated, and the examples are useful illustrations. But once the existing exact normalized moment map is used, the exceptional points are merely collisions of row exponents, and the joint recovery is the ordinary three-point Vandermonde exercise after rescaling. The record adds no non-routine invariant or obstruction to the prior identification theorem. There is no separately valuable unproved remainder to repair here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
