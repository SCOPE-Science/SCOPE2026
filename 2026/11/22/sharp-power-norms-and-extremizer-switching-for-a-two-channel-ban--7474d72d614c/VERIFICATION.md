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

P,Q are complementary projections of norm one: the triangle inequality and the two-coordinate power-mean inequality bound each, and a nonzero vector in its range attains one. Their products with each other vanish and they commute with S, giving TR=RT=S and T^k=P+S^k Q. The sign isometry diag(1,−1) conjugates T to R. For H(a,b)=(a+b,a−b), put u=|a|²+|b|² and v=2 Re(a conjugate(b)). The sum (u+v)^(p/2)+(u−v)^(p/2) is bounded above by 2u^(p/2) below p=2 by concavity (reverse above p=2); then u^(p/2)≤|a|^p+|b|^p (reverse above p=2), strictly unless ab=0 for p≠2. Applying that bound to H(a,b) and using H²=2I provides the opposite bound, with equality iff a=±b. This handles complex phases. The (a,b) sequences become (a,S^k b); the sum of their individual p-powers is invariant. Comparing the two sharp bounds supplies the desired upper power norm, with p=2 exact by Parseval and p=∞ bounded by the absolute row sums. A single impulse (1,0) attains the below-2 norm including p=1, and (1,−1) at zero plus (1,1) at k attains the above-2 norm including ∞. For finite non-Hilbert p the norm gaps are sums of nonnegative terms. Below 2, equality demands a_n=±b_n on the input and a_n b_(n−k)=0 on the output. Above 2 it demands a_n b_n=0 on the input and a_n=±b_(n−k) on the output with a_n=0 where the delayed b vanishes. These give the two exact support rules, including n<k. The supplementary spectrum follows by similarity to I⊕S: the shift has norm one, and the summable functional with coefficients λ^n witnesses every |λ|<1 in its spectrum for each p, including ∞.

## originality

PASS

The two-point matrix norm, its scalar equality cases, and the Hilbert-space isometric model are not distinct claims. The supported increment is their exact application to the delayed complementary channels, including complete sequence-level compatibility, attainment at every lag, and its change across p=2. The strongest distinct indexed geometry is an extremizer result for a real skew-min problem, with material overlap in the support dichotomy, but no verified implication of this delayed-operator law.

## value

PASS

The pair is the canonical two-channel equal-weight projection splitting, motivated by testing when a Hilbert shift factorization behaves isometrically in a Banach norm. The unit shift product conceals a real loss of contractivity. Exact uniform-in-power distortion and the complete changed support pattern go beyond a single finite witness or a scalar norm calculation: they identify all extremizing sequences for this motivating model without asserting a general factorization theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
