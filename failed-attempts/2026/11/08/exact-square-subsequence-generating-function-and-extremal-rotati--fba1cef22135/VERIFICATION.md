---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: For any q-letter permutation P and k copies, greedily matching a root V uses exactly 1+d(V) periods, with weak descents when consecutive letters are not increasing. Matching VV requires exactly 1+2d(V)+b(V), where b is the closing weak descent; this proves iff criterion. Trace of q-by-q matrix M(u), with lower triangle weight u and upper 1, evaluates by rank-one determinant and geometric series to F=zt^2[sum_(j=0)^(q-1) B^j + q t B^(q-1)]/(1-t^2 B^q), B=1+(1-t^2)z. Every symbol appears k times, giving upper half-length q floor(k/2); cyclic strictly increasing run equality forces one longest root for even k and q rotated longest roots for odd k>=3. Independently enumerated all distinct subsequences for eleven small (q,k) profiles including q=3,k=4 values 3,9,17,15,6,1 and checked maximal roots; finite tests only supplement the general proof.

## originality

FAIL

FAIL: The published 2026-11-02 Square-subsequence spectra of cyclic permutation powers theorem has EXACT same all-(q,k,m) weak-descent iff membership rule, all-length rational generating function of the same counts, same maximum half-length and one-even/q-odd cyclic-rotation classification. The earlier GF is written using H_q(x)=sum binom(q,j+1)x^j instead of B^q but is mathematically identical because both coefficient-extract precisely the same distinct-square spectrum; both examples at q=3,k=4 agree. Relabeling a permutation period P from 0..q-1 is a bijection of distinct words and adds no new result.

## value

FAIL

FAIL: Distinct square-subsequence counts of periodic permutations are a meaningful exact combinatorial invariant, but the full enumerator, embedding criterion and rotation extremizers already appeared in the earlier published theorem at the exact same parameter range. An alternate transfer-matrix simplification supplies no separate unknown classification or mathematical consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
