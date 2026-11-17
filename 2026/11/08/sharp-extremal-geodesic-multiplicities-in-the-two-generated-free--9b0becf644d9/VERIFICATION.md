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

Munn element is a birooted finite Cayley subtree; every minimal representing walk crosses its s-t path edges once and all other edges twice, giving length 2m-dist(s,t). Independent excursion-order choices at each vertex yield N_T(s,s)=d_s! product_{v!=s}(d_v-1)! and N_T(s,t)=product_internal(d_v-2)! product_other(d_v-1)! for distinct endpoints; labels of departing signed edges separate word choices. The fixed-tree maximum is max_degree times product (d_v-1)!. In rank two, with counts A,B,C of degree4,3,2, the handshake identity 3A+2B+C=m-1 maximizes 4*6^A*2^B by using A=floor((m-1)/3), then at most one degree3/degree2 depending on residue. Every admissible degree sequence embeds in the Cayley tree. Independent integer exact optimization over every degree count through m=31 reproduced unique profiles and M_m; finite tree and word enumeration checker was inspected but not re-executed completely.

## originality

PASS

The full accessible prior paper The Growth of Free Inverse Monoids (Kambites et al.) gives the Munn model, Lemma 3.2 shortest length t+2k, and sphere counts of elements via rooted-tree enumeration, not the number of distinct shortest words for a fixed element or the maximum at fixed tree-edge size. Bodart–Carvalho–Monteiro (2026) introduces Green geodesic language classes and their complexity, with abstract inspected; complete v2 source could not be retrieved after arXiv/OA attempts and institutional access was blocked. No published Resultary search hit supplied the exact 4*6^k residue-dependent fixed-m maximum or degree-pattern extremizers. A broader preexisting enumeration of depth-first tree tours could imply the local factorial formula, but no evidence that it already optimizes all degree profiles; best-of-knowledge O passes subject to explicit risk.

## value

PASS

Geodesic word redundancy is a canonical invariant of free inverse monoid elements, especially after formal introduction of Green geodesic languages. The theorem gives an all-size exact maximum, growth base 6^{1/3}, complete equality-case tree degree patterns with mod-three fluctuations, and a uniform Green-class enumeration polynomial. These are motivated complete extremal classifications not evident from previously known length or element-growth formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
