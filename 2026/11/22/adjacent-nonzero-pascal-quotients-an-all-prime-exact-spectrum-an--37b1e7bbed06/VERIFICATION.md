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

Under Lucas eligibility, a carry through t trailing p−1 digits forces the corresponding n digits to be p−1, contributing units 1 to both entries. At the first changed nonterminal digit, (n_t,k_t)=(d,e) satisfies e<d, and the upper digits are arbitrary admissible equal-factor pairs. The quotient is b/a with (a,b)=(d−e,e+1) positive and a+b≤p. For fixed u there are p−1 pairs b=ua in the positive residue representatives; simultaneous complementation exchanges strict sides of the boundary a+b=p and the entire boundary occurs only for u=−1. Counting higher digits and summing over t gives the stated multiplicities and total, including the lone p=2 residue. For odd p, the ratio law gives the product sign mean χ_p(−1)/p by character orthogonality. The two one-coordinate signed totals are (H_p−p)Σ H_p^j: each local row lacks one unit endpoint and every upper digit contributes H_p. There are both signs among digit factors: −1 works for p≡3 mod 4, while the row p−2 factors (−1)^e(e+1) give a nonsquare for p≡1 mod 4. Thus |H_p|<Q_p and the marginal means vanish relative to the eligible total. Inverting the four exact sign totals verifies both the finite and limiting joint law. A separate enumeration by Pascal addition mod p, rather than the supplied Lucas implementation, reproduced the entire ratio histogram and each odd-prime joint-sign count at (p,r)=(2,5),(3,4),(5,3),(7,3),(11,2),(13,2).

## originality

PASS

Credit is for the evaluated unweighted ratio multiplicities at all complete cutoffs and the exact and limiting two-coordinate sign laws. Neither Lucas reduction, the use of a decisive carry digit, nor the qualitative prominence of −1 in the binomial problem is claimed as an independently new result. The strongest available distinct indexed theorem treats weighted counts with an additional trinomial coordinate and does not give the slice-specific evaluated histogram or joint signs.

## value

PASS

Adjacent entries are a canonical local statistic of the Pascal array. Unlike one-entry digit distributions, the evaluated ratio law supplies a full pair observable at every depth and shows that marginal quadratic balance is consistent with definite nonzero short-range dependence. The all-prime law quantifies the lone exceptional residue and the sign and size of the persistent correlation, not just isolated rows or re-tabulated residue counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
