---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The prime-tail interval argument is correct: if each prime p_j in a tail satisfies 1+p_j^(-r)<=T_j, consecutive prime-power-scaled intervals overlap, including the infinite-exponent limit in the closure. A greedy selection leaves multiplicative error at most T_j tending to one. Defant's Lemma 2.1 excludes prime indices 1, 2, 4 from the consecutive-prime ratio bound; its Theorem 2.2 proof gives F_3<F_4 and F_j increasing strictly to zeta(r) for j>=5. Thus the checked p=7 inequality completes the tail for p>=5. The eight inequalities were independently certified at the real interval's worst-case endpoints: direct sum over n coprime to 6 through 3000 plus rigorous integral bounds per residue class, and exact floor-root arithmetic. The eight strict lower slacks in the order isolated gap, seven tail, eleven tail, higher three powers, lower and upper two-power bands, and the two joins, exceed respectively 595733,16694645,20302235,105503478,62563922,79659460,7713055,99783208 times 10^(-9), allowing equality with these rounded-down lower bounds. The replay also checks 33,605 prime gaps in Defant's finite range. Monotonicity of the Euler tails and the power step 1+z^2/(1+z) justifies combining the appropriate endpoints throughout the closed real parameter interval. Adding exponent-zero and positive-exponent bands for 3 and then for 2 gives the stated union, with endpoints at infinite exponents interpreted in the closure. Membership in the lower interval is exactly gcd(n,6)=1 because any integer with a factor 2 or 3 has sum at least 1+3^(-r), strictly above W. The complementary density, like the lower one, follows from counting residue classes.

## originality

FAIL

Zubrilina's Lemma 4.7 proof already gives the exact three-band union before the last possible overlap is resolved. On the whole subregime where 3 alone is mighty, the two upper bands automatically merge. This gives the submitted endpoints throughout a stronger regime, and the integer membership and densities follow immediately from the endpoints. The submitted short decimal interval checks that it lies in this subregime; it does not add a distinct range classification.

## value

FAIL

One-gap regimes and exact component densities are worthwhile objectives, and the integer arithmetic makes the explicit example reproducible. But this particular narrow decimal bracket has no shown transition, extremal significance, or independent application, and its topology, endpoints, and densities follow from the stronger published decomposition and the routine checks placing the bracket in its regime. The certificate is not a new boundary, structural invariant, or demonstrated correction of the primary theorem. No independently valuable remainder requiring a repair was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
