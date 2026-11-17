---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Every positive odd y satisfies y+3=2^j k with k odd, and the following odd iterate is ky; k=1 gives primitive j-cycle at y=2^j−3. For k≥3 a nonterminal arrival at 2^m−3 would force 2^m=2^jk²−3(k−1). Modulo three, m−j is even; since m>j, write m−j=2h and k>2^h, obtaining 2^j(k²−2^{2h})≥4k−2>3(k−1), contradiction. Therefore nonterminal odd values grow at least threefold and all intervening even iterates exceed the next odd value; full trajectories escape. Unique odd parts count bounded starts exactly, with leading 1/2(log2 X)^2. Independently tested numerous finite odd transitions and terminal predecessors.

## originality

PASS

Previously classified quadratic odd branches involve ±1 or symmetric maps, not n(n+3)/2; their terminal-arrival obstructions differ. Same-family plus-five work is a separate parameter with an exceptional tail, showing simple substitution does not imply the no-tail plus-three result.

## value

PASS

A complete infinite integer-dynamical classification for a natural nearby quadratic Collatz rule, including complete bounded basins, no hidden preperiodic arrivals, true full-sequence divergence and an exact sparse-basin census, is a meaningful contrast with other parameters that have exceptional tails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
