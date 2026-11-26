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

Over an arbitrary commutative test algebra the squares of the tail basis vectors span the next tail, by the unit leading coefficients; hence all tails are intrinsic. Triangularity and invertibility give unit diagonal entries. For i<j<n, the coefficient of e_(j+1) in the product of the images of e_i,e_j is the e_j off-diagonal entry times the j-th diagonal unit, so that entry vanishes even over nonreduced rings. In each square equation the leading term forces t_(i+1)=t_i². The terminal-coordinate equations force u_(n−1),…,u₂=0 by descending substitution, leaving u₁ arbitrary. Each nonzero skipped coefficient, a unit from K, gives t^(2^(j−1)−2^i)=1. Bézout for these exponents in R× is equivalent to t^g=1; every resulting triangular matrix is invertible and respects all products. Composition in z=u₁/t gives z+t^(2^(n−1)−1)y, identifying the action and the representing functor, not merely points. In characteristic p, write g=p^a h, p∤h; the reduced factor is μ_h and the tangent equation g·dt=0 contributes one extra dimension exactly when p divides g. Every weight is even; for odd p, every supported gap j−1−i must be a positive multiple of ord_p(2) for nonsmoothness. The maximum gap is n−3, and b_(1,r+2)=1 alone realizes resonance whenever n≥r+3. Finite-field counts follow from cyclicity and the free additive coordinate. The multiplication also gives V_i V_j=V_(max(i,j)+1); balanced power splittings yield the stated maximal nilindex.

## originality

PASS

The ordinary automorphism matrix and gcd-of-weights condition are substantially known, as is the normalized maximal-index family. The distinct supported result is the group scheme on all test rings for this nilpotent family and its sharp characteristic-dependent nonsmoothness boundary. The closest ordinary proof uses reductions valid over fields, including vanishing inferred from zero squares; that proof cannot be interpreted wholesale over nonreduced rings. A known scheme theorem with a related roots-of-unity and derivation mechanism concerns perfect, not nilpotent, evolution algebras.

## value

PASS

Passing from ordinary points to the actual stabilizer scheme detects a genuine phenomenon invisible to rational-point enumeration: the additive dimension persists while a multiplicative tangent direction appears precisely in resonant supports. The exact first possible occurrence for every odd prime and its explicit one-coefficient witness answer a natural classification question in a standard maximal-index family. The supporting all-rings proof excludes hidden nilpotent matrix coordinates, so the result adds more than a repackaging of the characteristic-zero count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
