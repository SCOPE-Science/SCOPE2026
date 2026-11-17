---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For length-n source and ordered palindromic duplicate lengths k then ell, the two legal start counts multiply to bound descendants by (n−k+1)(n+k−ell+1). On an all-distinct-letter word, every original first occurrence remains first after insertions, so the final word uniquely partitions into copy gaps. If two gaps are occupied, their unequal sizes k,ell identify the first gap and site, then recover the intermediate word and second site. If only one gap, its index identifies the first duplication; the h copies before second insertion give pairwise distinct outputs: for 1<=h<hprime compare at gap position h, and compare h=0 separately using ell>=2. Therefore no two histories collide. Exact independent enumeration checked 369 legal (n,k,ell) triples and 7227 outputs. Boundary counterexamples for ell=1 and ell=k correctly delimit the theorem. This is a uniform proof for q>=n, not just the finite enumeration.

## originality

PASS

All distinct-letter sources have collision-free histories for ordered unequal prescribed duplication lengths (with second length >=2), whereas the closest full fixed-equal-length sphere theorem has unavoidable commuting-disjoint collisions and a strictly smaller formula. The source alphabet/length and ordered-history scopes were compared explicitly. The inaccessible full Zabokritskiy general treatment is acknowledged as a possible historical risk.

## value

PASS

Exact descendant sphere size and history ambiguity are fundamental to duplication-channel combinatorics and coding. The unequal-length ordered regime has a genuinely different collision mechanism than fixed-length duplication; reconstructing both sites yields an exact extremum for every n,k,ell over large enough alphabets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
