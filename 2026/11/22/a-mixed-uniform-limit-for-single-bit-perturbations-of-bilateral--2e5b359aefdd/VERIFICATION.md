---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The mapping from the word to its first bit and successive XOR boundaries is a bijection, so the boundaries are independent fair bits. An interior flip toggles the two adjacent boundaries. If they differ, the run symbols and number of runs are unchanged and at most two adjacent run lengths vary; the fixed pairing can rewrite at most two tokens. If the boundaries agree, replace a consecutive block of one run by three, or three runs by one, leaving a common prefix of a runs and suffix of b runs. Write K for the original edited run index and R for the original run count; (a,b)=(K-1,R-K) for a split and (K-2,R-K-1) for a merge. The last depth nonterminal in both lists is D=floor((a+b)/2), which never exceeds max(a,b). Up to min(a,b) both sides agree. Beyond min(a,b)+3 and through D, the longer side is unchanged and both lists on the shorter side have passed the replaced block. There the two compared original run indices differ by two, in one contiguous interval of depths. At most three local depths and one common terminal handoff are excluded. Since binary symbols alternate, and the stored split separates the paired runs, a bulk mismatch is exactly an unequal pair of lengths. The bulk interval length is R/2-min(K,R+1-K)+O(1) with truncation. On an infinite fair-bit coupling, run lengths are i.i.d. geometric with mass 2^(-l) at l>=1, so a two-index length comparison mismatches with probability 2/3. Its indicators have an SLLN (split indices into three independent residue-class subsequences), and the maximum prefix-sum deviation up to n+2 is o(n) by the same SLLN. Taking differences proves the needed uniform interval estimate at data-dependent endpoints and in either direction. The finite truncation of the last run affects only O(1) comparisons. The uniform prefix boundary law likewise gives R/n->1/2 and K/n-P/(2n)->0. Conditional on every interior P, equal boundaries occur with probability 1/2; this exact independence from P plus the unconditional uniform error bounds gives the joint limit J|U-1/2|/3 for an independent fair Bernoulli J and uniform U on [0,1]. Hence the mixture is a half atom at zero and half uniform on [0,1/6]. H_n/n is uniformly bounded, giving the stated mean limit 1/24.

## originality

PASS

The Flashback source provides the deterministic token representation, token-count stability and skeleton-preserving edit locality, and separately gives random one-word token counts. It does not state the coupled same-depth distance distribution. The linear-scale random edit effect and its exact mixture and mean require a distinct shift and renewal calculation. No earlier equivalent was located in the bounded comparison.

## value

PASS

This gives a quantitative stability benchmark for a specific reversible representation where total token count can look stable despite content realignment. It cleanly separates local and macroscopic regimes and gives both the full leading-order law and an explicit mean. Those facts are not captured by routine edit-distance or run-count estimates; downstream compression performance is not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
