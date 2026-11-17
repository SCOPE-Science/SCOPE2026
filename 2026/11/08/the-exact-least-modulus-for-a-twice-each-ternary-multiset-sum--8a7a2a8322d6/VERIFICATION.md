---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The fixed ternary family A_n={3^i-1}, i=0..n-1, is distinguished at total multiplicity 2n by k_i=2. Since total counts match, the offset -1 cancels, leaving even difference V=sum k_i3^i-(3^n-1). The minimal coin count gamma_n(M)=floor(M/3^(n-1))+s_3(M mod 3^(n-1)); all other feasible counts arise by splitting a 3^j coin into three 3^(j-1) coins, preserving parity. For N*=(3^n-3^t)/2 with n-t odd and 3^t<=2n-1, N* odd: negative multiples violate M>=2n; positive multiples h(3^n-3^t) have gamma=2n+3h-s_3(h)>2n. All smaller even N and small odd N admit a negative difference; remaining odd N yield dprime=3^n-2N with s_3(dprime)>=3 (opposite exponent parity excludes one-digit powers), producing a positive rival. Independently exhausted all weak compositions and candidate moduli for n=2..6: minima 3,13,39,117,363. The proof, not finite n, covers n>=2.

## originality

PASS

Best-of-knowledge PASS with explicit residual primary-access risk. The 2026 Fonollosa minimum-modulus theorem treats radix TWO with one copy per position and n summands, whereas this result fixes radix THREE and exactly two copies/2n summands, requiring new parity-dependent 3-adic obstruction. An earlier binary all-ones formula, even if supplied for groups, is not an implication at the distinct target multiplicity. Targeted Resultary comparisons found only this exact ternary twice-each theorem, not an independently earlier same theorem. Full Fonollosa primary article remained inaccessible via arXiv/OA and institutional VPN, so the comparison is limited to accessible abstract and authorized public material; equivalent unindexed specialization risk remains.

## value

PASS

The precise least modulus guaranteeing a unique multiset checksum is a natural numerical invariant motivated by modular uniqueness/permanent-transform constructions. Solving the nontrivial weighted radix-and-multiplicity variation for all n and sharp parity-sensitive t(n), plus explicit witnesses for every smaller modulus, goes beyond a substitution into the binary formula or finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
