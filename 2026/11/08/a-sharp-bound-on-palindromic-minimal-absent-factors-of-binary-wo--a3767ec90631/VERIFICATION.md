---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

The theorem is for distinct palindromic ordinary minimal absent contiguous factors of binary length-n linear words, including missing one-letter words. For any word containing both letters, each missing palindrome p of length at least 2 has present proper prefix P(p); map p to the endpoint of the earliest P(p) occurrence. Equal-length collisions force equal prefixes, hence equal palindromes. For shorter p length r and longer q length s with equal endpoint, P(p) is a proper suffix of P(q). If p and q have the same outside letter, the last r letters of q form p, so by reversal p is a prefix of q and appears inside its present P(q), contradiction. If outside letters differ and endpoint t<n, both completion letters 0,1 would be forbidden by absence of p,q, contradiction. At endpoint n, an occurring suffix S(q)=q[2..s] must end before n (otherwise P(q)=S(q) makes q constant, incompatible with differing outside letters and the suffix P(p)); its interior contains P(p), yielding an earlier occurrence of P(p), contradiction. Thus an injection into n positions. For monochromatic words exactly the missing singleton and opposite constant (n+1)-letter run occur as MAWs, giving 2≤n for n≥2. For n≥3 the existing 01^(n−2)0 family has exactly n explicit missing palindromes: 00, 101, 1^(n−1), and 01^k0 for 1≤k≤n−3. Each has occurring length-minus-one prefix and suffix, all distinct; n=2 has 2 on 00 and n=1 has 2 on 0 or 1. No larger alphabet, circular or scattered absence is claimed. Fresh independent Python enumerated every length 1..12 binary word and directly generated palindromes of each length ≤n+1, checking both maximal proper factors, maxima n for n≥2 and exactly 2 at n=1, exactly two maximizers for n≥3 through 12, and no earliest-endpoint collision for any two-symbol word. Crucially the source tree was reconstructed from eight pinned Git blob SHAs and matches the assignment tree SHA 00cf789739326296c047dc76b4142a6a52e4b24e. These finite checks corroborate, not replace, the all-n proof.

## originality

PASS

Best-of-knowledge: the exact global maximum n for the ordinary (all proper contiguous factors occurring) palindromic subset and the first-occurrence endpoint injection are not mathematical consequences of the inspected 2009/2014 structural and algorithmic MAW theorems, of the 2017 asymptotic lower-bound witness, or of the distinct 2022 interior-only minimal absent palindromic word (MAPW) invariant. The 2022 Mieno et al. definition has an absent palindrome with an occurring interior, not necessarily occurring length-(|p|-1) prefix and suffix, and yields |MAPW|=|DPal|+3 for binary words, hence at most n+4; it does not establish this exact n bound for the stricter ordinary-minimal subset. Closest published block-power result explicitly uses that different Mieno definition; the three-marker/four-run exact ordinary MAW findings classify restricted families and do not establish the unrestricted palindromic maximum. The extremizing word 01^(n-2)0 and its n-2 bridge absences are old (Almirantis 2017); neither the family nor asymptotic linear growth is claimed new. No failed search was treated as priority proof.

## value

PASS

An exact worst-case size for the reversal-symmetric component of an ordinary factor antidictionary is a natural invariant: palindrome-filtered negative patterns play a role distinct from positive palindromic complexity and interior-only MAPWs. Earlier generic O(σn) enumeration results and the known asymptotic witness leave the optimal exact binary coefficient unidentified. The n theorem is parameter-uniform, attained, and explained by a nontrivial endpoint charging argument; it is neither a finite recomputation nor a renamed general bound. This supplies a precise capacity bound for a natural restricted family of missing motifs without claiming a new general algorithm, biological significance, or classification of all maximizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
