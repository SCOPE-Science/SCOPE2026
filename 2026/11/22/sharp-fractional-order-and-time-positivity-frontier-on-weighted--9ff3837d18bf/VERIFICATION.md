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

Trace and the principal minors give λ₊+λ₋=2S and λ₊λ₋=3Q. From the two spectral projectors on the complement of the constant vector, an edge w has heat entry (1−exp(−qt))/3 + B_w(exp(−pt)−exp(−qt)), with p=λ₊^α, q=λ₋^α and B_w=(λ₋/3−w)/(λ₊−λ₋). The identity (S²−3Q)−(S−3w)²=−3(w−w′)(w−w″) orders the cut λ₋/3 between the least and second-least weights, with equality at the least exactly for a tied minimum. Thus only a unique weakest edge can be negative; the repeated-eigenvalue equal-weight case has a single nontrivial exponential and is strictly positive for t>0. For weakest-edge B=B_m>0 set A=B+1/3. Its derivative is exp(−qt)[Aq−Bp exp(−(p−q)t)], whose bracket is strictly increasing. It is nonnegative at zero exactly for α≤α*, and then strictly positive for t>0, including at the order endpoint. At α=1 the derivative at zero is m>0. Above α* the derivative has exactly one zero, with the stated logarithmic time, and k(t) rises thereafter to 1/3 from a strict negative minimum; it crosses zero once at the stated implicit root. Diagonals are positive by the spectral projections; row sums are one, so the only negative pair gives the claimed row norm amplification, whose unique peak precedes recovery. The equal-stronger family gives eigenvalues 3−2ε,3 and ratio 3 in the numerator of α*. For fixed C>1 the other family has λ₋=3−3δ/2+O(δ²) and λ₊=2C+1−δ/2+O(δ²), giving numerator log(1/δ)+log(4(C−1)/3)+O(δ) and the stated denominator up to O(δ). The profile, not a separately stated height formula, gives the peak height. The script verify_triangle.py was read, not executed; its floating-point checks do not establish the quantifiers in the theorem.

## originality

PASS

Qualified pass for the explicit weighted-triangle order and time formulas, exact transient amplification and its peak, and the two distinct conductance-degeneracy laws together. The qualitative unique-recovery statement is not credited as wholly distinct: for a unique minimum a same-day weighted-star result gives the sign pattern by exact spectral reparametrization. Its available indexed statement does not give the triangle amplification and peak formulas or the two singular conductance limits. The same-day records are not chronologically ordered by the evidence.

## value

PASS

An explicit all-order and all-time positivity test on the smallest complete network where superunit powers can produce transient negative heat. The exact row-norm profile quantifies the failure of contractivity, and the two conductance limits show how rapidly the critical order becomes inaccessible near a tie in two natural regimes. The contribution is confined to these quantitative weighted-triangle results, not to the already overlapping generic occurrence of a recovery interval.

The dated certificate retains the supplied scientific assessment, sources and limitations.
