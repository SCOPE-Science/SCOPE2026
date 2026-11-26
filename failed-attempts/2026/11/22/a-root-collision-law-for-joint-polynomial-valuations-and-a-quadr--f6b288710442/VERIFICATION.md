---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For each simple residue root the Hensel lift α is unique and the factor f(x)/(x−α) is a unit on its root disk. Thus outside the root disks the valuation is zero, and within one it measures agreement with its centre. Different residue disks are disjoint. Two balls at depths t,s intersect exactly when their centres agree through min(t,s); then the intersection is the deeper ball and contains p^{k−max(t,s)} residues modulo p^k. This gives both exact finite tails and the stated Haar tails. In the mixed tail series the diagonal at m=min(t,s) contributes (zw)^{m−1}p^{−m}; the two off-diagonals multiply this by z/(p−z) and w/(p−w). Geometric summation over m≤d yields the PGF, with no convergence problem on the closed unit bidisk even at d=∞. At z=w=1 the mixed-tail sum is (p+1)Σ(1−p^{−d_a})/(p−1)^2. Subtracting the marginal product gives the formula. For split quadratics, r=0 is negative and r=2 is positive even at minimal d=1. For r=1 the numerator is −4·3^{−d} at p=3 and at least (p²−4p−1)/p>0 for p≥5. Coinciding lifts as well as empty root sets are consistent with the formulas in RESULT.md.

## originality

FAIL

There is positive prior-implication evidence, not merely a search limitation. Zúñiga-Galindo's explicit weighted root-tree generating function (math/0204360v1, §§4–5, notably Lemma 5.1) covers the bivariate law by assigning multiplicities m,n to the two factors of a rationally split product. The transfer to arbitrary simple Hensel lifts needs only disjoint translations of sufficiently deep residue disks, not a new zeta-function calculation. Its explicit vertex terms specialize to the two-colour shell law, and the covariance and quadratic sign alternatives are direct summation and comparison of those terms. The frozen comparison considers product sums at fixed weights, not this arbitrary-multiplicity reduction. The stronger prior need not state the specific covariance wording.

## value

FAIL

The dependence question is natural and the sign description is useful exposition, but this exact law is mechanically supplied by the pre-existing explicit weighted-tree evaluation: the specialization has only single-colour stalks and at most one bifurcation per residue. The proposed additional boundary is a geometric moment sum and substitution of r=0,1,2 into that same known law. No independent non-routine unknown exact fact is established beyond this specialization; the finite check and alternate proof add neither.

The dated certificate retains the supplied scientific assessment, sources and limitations.
