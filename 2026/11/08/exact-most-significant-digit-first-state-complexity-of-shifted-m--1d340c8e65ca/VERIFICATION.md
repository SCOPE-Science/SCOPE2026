---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Frozen RESULT.md proof reconstructs every possible MSD right context. A length-l suffix r either has valuation nu_b(r+d)<l independent of the prefix, or r=(-d) mod b^l yields l+nu_b(n+q_l); offsets q_j=ceil(d/b^j) stabilize at 1 after K steps. Suffixes of lengths j recover all coordinates Phi(n), so equality of Phi is exactly Myhill–Nerode equivalence. Differences q_i-q_j have b-adic valuation <K; H<=K separates their marked low-order residues. Missing trie branches give fixed signatures; active leaves give m arbitrary residues in one coordinate; constructive n=b^e-q_i realizes every leaf signature. Hence the finite union equals the unbounded minimal state set and the O((log(c+2))^2) bound follows. Independent 896 parameter cases checked direct finite signatures against formula; finite checks are corroboration, not proof.

## originality

PASS

Earlier Resultary 2026/10/25 work determines the LSD-first shifted valuation complexity exactly, but reversing input direction changes right contexts and can change state counts (the source gives MSD=9 versus LSD=8 at b=m=2,c=10). Moradi–Rampersad–Shallit full arXiv HTML discusses general automata for arithmetic relations, Thue–Morse shifts, linear subsequences and generic bounds; no equivalent exact offset-trie valuation classification was found in §§3–4. An older general automaton minimization algorithm is not itself an explicit all-shift formula.

## value

PASS

Minimal MSD-first memory of shifted ruler sequences is a natural exact invariant of automatic sequences and the input direction matters. The explicit low-order valuation-signature trie avoids arbitrary brute-force state minimization, works for every radix and composite modulus, and yields an effective polylogarithmic shift bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
