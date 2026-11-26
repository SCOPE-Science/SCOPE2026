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

Use the marked-host recurrence relative to linear forests, not unrestricted graphs. Each of the three pair-only neighbour patterns is a legal prime extension over an independent triple. Their simultaneous realization would give three vertices pairwise at distance two, impossible in a union of finite paths, rays and double rays. Thus independent triples have relative rank zero; the legal isolated extension from a nonedge, followed by the legal nonedge extension from a singleton, rules out level four at the root. For level three the nonedge branch needs all four traces. The 10, 11 and 01 witnesses form the outer ends and middle of an induced P5, and the 00 witness is necessarily a sixth vertex. Conversely in x0–x1–x2–x3–x4, the singleton x1 can take the adjacent partner x2 (traces 00,10,01 via x4,x0,x3) and the nonadjacent partner x3 (traces 00,10,01,11 via the sixth vertex,x0,x4,x2). Both inner marks in the nonadjacent branch have degree two already. The lower levels follow from availability of a vertex and of a vertex with both a neighbour and a nonneighbour. This gives the two order-six shapes and the unique four-edge minimum. For n≥6 the rank-three census subtracts components restricted to sizes at most four from all path components; the singleton EGF weight is one, every higher path weight is 1/2. The n=5 coefficient would count P5 incorrectly and is properly excluded. The all-forest coefficient is bounded below by 1/2 and above by exp(O(sqrt(n))) via the radius 1−1/sqrt(n). For the restricted EGF the radius n^(1/4) gives the log upper bound −(n/4)log n+O(n); floor(n/4) four-paths and one residual component give the matching lower bound by Stirling.

## originality

PASS

The complete exact rank theorem has a genuinely class-specific ceiling and independent-triple obstruction. The rank-at-least-three condition and consequent finite first-onset and component-based census are mathematically covered by specializing a same-day triangle-free Resultary theorem; do not count that threshold as an independent novelty. That theorem does not determine the exact upper ranks here. The frozen contribution, read as the full exact classification with enumerative consequences, survives this comparison without changing its mathematical claim. Same-day path dates do not establish manuscript priority.

## value

PASS

The ceiling is a useful exact boundary for a natural path age and holds even in infinite hosts where increasing available vertices might otherwise raise rank. The obstruction identifies precisely which legal extension blocks further rank. Combined with the lower-level tests it determines the rank of each host; the census and rarity consequences make the difference between the mere possibility and typicality of attaining that ceiling explicit. Neither ordinary path enumeration nor the earlier rank-three threshold alone establishes this upper boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
