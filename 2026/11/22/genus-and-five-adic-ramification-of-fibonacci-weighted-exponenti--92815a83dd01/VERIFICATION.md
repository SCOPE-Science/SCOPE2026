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

Reconstructed the proof for every k ≥ 2 in characteristic zero. Binet expansion followed by formal logarithms gives valuations m_j = (−1)^(j+1) binom(2k,j) at x = [ (−1)^j α^(2k−2j) ]^(−1), where α is the positive golden ratio. Distinct absolute values give distinct points; Galois conjugation pairs j with 2k−j and fixes only j=k. The valuations sum to zero, so infinity is unramified. At the simple pole j=0 the reciprocal equation is Eisenstein over the geometric discrete valuation ring, proving degree and geometric connectedness. The k=2 row is prime to five; for k≥3 the central coefficient starts at 20<25 and grows by a factor <4, hence all valuations have ν₅<k−1 and all 2k+1 points branch. Tame Kummer inertia has index N/gcd(N,m_j), with total different N−gcd(N,m_j) above each branch point. Riemann–Hurwitz gives the stated genus; the fixtures k=2,3,4,7 give respectively 6,54,432,101556. Lucas's congruence counts full inertia, and all j≤2k obey the digit inequalities exactly when all digits below the leading digit are four: if a lower digit is smaller, one can decrease the leading digit of j relative to 2k and exceed that lower digit. Parity forces the leading digit to be two or four. This yields the two claimed progressions and the maximal-genus formula. Kummer carries are at most the digit length minus one, so each term in the correction sum is at most 2k. Finally, the normal closure is Q(x,G_k,ζ_N): it contains all conjugates, and their ratios generate the roots of unity. Geometric irreducibility preserves degree N over Q(ζ_N)(x), and the cyclotomic action fixing x,G_k splits and conjugates the cyclic generator by the natural units.

## originality

PASS

Pass for the family-specific geometric profile and its all-index arithmetic classification, not for the equation, degree, or general Kummer theory. The equation makes the inertia and normal closure accessible by standard arguments, and the geometric invariants are not independent new cover-theoretic principles. The inspected same-family and broader statements establish algebraicity and degree, not the quantified five-adic ramification and maximal-genus classification.

## value

PASS

For the natural infinite family coming from even Fibonacci moments, the result gives more than translating one known polynomial into a generic genus formula. It resolves uniformly whether branch candidates survive normalization, counts full inertia by digits, and identifies exactly when the maximal genus occurs along two exponential progressions. This is useful family-specific information even though the arithmetic closure and cover-theoretic ingredients are standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
